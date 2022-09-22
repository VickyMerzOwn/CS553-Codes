#include <iostream>

using namespace std;

char encrypt(char plain_text, int key)
{
    char cipher_text;

    if (plain_text >= 'a' && plain_text <= 'z')
    {
        cipher_text = plain_text + key;

        if (cipher_text > 'z')
        {
            cipher_text = cipher_text - 'z' + 'a';
        }

        return cipher_text;
    }
    else if (plain_text >= 'A' && plain_text <= 'Z')
    {
        cipher_text = plain_text + key;

        if (cipher_text > 'Z')
        {
            cipher_text = cipher_text - 'Z' + 'A';
        }

        return cipher_text;
    }
    else
    {
        printf("%c is not a valid character.", plain_text);
        return 0;
    }
}

char decrypt(char cipher_text, int key)
{
    char plain_text;

    if (cipher_text >= 'a' && cipher_text <= 'z')
    {
        plain_text = cipher_text - key;

        if (plain_text < 'a')
        {
            plain_text = plain_text + 'z' - 'a';
        }

        return plain_text;
    }
    else if (cipher_text >= 'A' && cipher_text <= 'Z')
    {
        plain_text = cipher_text - key;

        if (plain_text > 'Z')
        {
            plain_text = plain_text + 'Z' - 'A';
        }

        return plain_text;
    }
    else
    {
        printf("%c is not a valid character.", cipher_text);
        return 0;
    }
}

int main()
{
    char msg[128];
    int choice;
    int key;

    cout << "Enter your message: ";
    cin >> msg;
    cout << "Enter your key: ";
    cin >> key;
    cout << "\n\n\nPress:\n1: For encryption\n2: For Decryption\nAnd hit Enter\n\n\n";
    cin >> choice;

    for (int i = 0; i < 128; i++)
    {
        if (choice == 1)
        {
            msg[i] = encrypt(msg[i], key);
        }
        else if (choice == 2)
        {
            msg[i] = decrypt(msg[i], key);
        }
        else
        {
            cout << "Please run again and enter a valid choice (1 or 2)";
            return 0;
        }
        cout << msg[i];
    }
    return 0;
}