import gurobipy as gp
from gurobipy import GRB
from base_conversions import dec2hex


class MILP:
    def __init__(self, rounds):
        self.model = gp.Model("MILP_Sypher004_cryptanalysis")
        self.rounds = rounds
        self.sboxes = []
        self.difference_bits = []
        self.difference_bits_permuted = []
        # self.premap = [7, 8, 6, 12, 9, 10, 13, 11, 1, 15, 14, 2, 3, 5, 0, 4]
        self.premap = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]
        # print(self.difference_bits)

    def add_variables(self):
        for i in range(6):
            diff_layer = []
            for j in range(16):
                var = "x" + dec2hex(i) + dec2hex(j)
                x = self.model.addVar(vtype=GRB.BINARY, name=var)
                diff_layer.append(x)
            self.difference_bits.append(diff_layer)

    def permute_difference_bits(self):
        self.difference_bits_permuted.append(self.difference_bits[0])
        for difference_bits in self.difference_bits[1:5]:
            permuted = [0] * 16
            for i in range(16):
                permuted[self.premap[i]] = difference_bits[i]
            # print(permuted)
            self.difference_bits_permuted.append(permuted)
        self.difference_bits_permuted.append(self.difference_bits[5])

    def add_sboxes(self):
        for i in range(self.rounds):
            sbox_layer = []
            for j in range(4):
                var = "a" + str(i) + str(j)
                sbox_layer.append(self.model.addVar(vtype=GRB.BINARY, name=var))
            self.sboxes.append(sbox_layer)

    def add_constraints_sbox_operation(self):
        for i in range(self.rounds):
            for j in range(16):
                self.model.addConstr(
                    self.difference_bits_permuted[i][j] - self.sboxes[i][j // 4] <= 0
                )

    def add_constraints_input_sbox_operation(self):
        for i in range(self.rounds):
            for j in range(4):
                self.model.addConstr(
                    sum(self.difference_bits_permuted[i][4 * j : 4 * j + 4])
                    - self.sboxes[i][j]
                    >= 0
                )

    def add_constraints_indiff_outdiff(self):
        for i in range(self.rounds):
            inp = self.difference_bits_permuted[i]
            out = self.difference_bits[i + 1]
            for j in range(4):
                self.model.addConstr(
                    4 * sum(inp[4 * j : 4 * j + 4]) - sum(out[4 * j : 4 * j + 4]) >= 0
                )
                self.model.addConstr(
                    4 * sum(out[4 * j : 4 * j + 4]) - sum(inp[4 * j : 4 * j + 4]) >= 0
                )

    def set_constraint_min_active_sbox(self):
        constr = None
        for a_layer in self.sboxes:
            for a in a_layer:
                if not constr:
                    constr = a
                else:
                    constr += a
        self.model.addConstr(constr >= 1)

    def set_objective_function(self):
        self.objective = None
        for a_layer in self.sboxes:
            for a in a_layer:
                if not self.objective:
                    self.objective = a
                else:
                    self.objective += a

        # print(objective)
        self.model.setObjective(self.objective, GRB.MINIMIZE)

    def run(self):
        self.add_variables()
        self.permute_difference_bits()
        self.add_sboxes()
        self.add_constraints_sbox_operation()
        self.add_constraints_input_sbox_operation()
        self.add_constraints_indiff_outdiff()
        self.set_constraint_min_active_sbox()
        self.set_objective_function()
        self.model.optimize()
        print(self.sboxes)
        # print(self.difference_bits)
        self.model.write("milp_sypher004.lp")


s = MILP(5)
s.run()
