#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Function prototypes
bool is_valid_key(string key);

int main(int argc, string argv[])
{
    // STEP 1: Validate command-line arguments
    if (argc != 2 || !is_valid_key(argv[1]))
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    string key = argv[1];

    // STEP 2: Get the plaintext from the user
    string plaintext = get_string("plaintext:  ");

    // STEP 3: Encrypt and print ciphertext
    printf("ciphertext: ");

    int len = strlen(plaintext);

    for (int i = 0; i < len; i++)
    {
        char c = plaintext[i];

        if (isalpha(c))
        {
            int position;
            if (isupper(c))
            {
                position = c - 'A';
            }
            else
            {
                position = c - 'a';
            }

            char substituted = argv[1][position];

            if (isupper(c))
            {
                printf("%c", toupper(substituted));
            }
            else
            {
                printf("%c", tolower(substituted));
            }
        }
        else
        {
            printf("%c", c);
        }
    }

    printf("\n");
    return 0;
}

bool is_valid_key(string key)
{
    // TODO: Check length is 26
    if (strlen(key) != 26)
    {
        return false;
    }

    bool seen[26] = {false};

    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
        {
            return false;
        }

        int index = tolower(key[i]) - 'a';

        if (seen[index])
        {
            return false;
        }
        seen[index] = true;
    }

    return true;
}
