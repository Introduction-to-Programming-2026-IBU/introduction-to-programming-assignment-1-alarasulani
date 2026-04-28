#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);

    long temp = number;
    int length = 0;

    while (temp > 0)
    {
        temp /= 10;
        length++;
    }

    int sum_doubled = 0;
    int sum_rest = 0;
    temp = number;

    for (int i = 0; i < length; i++)
    {
        int digit = temp % 10;
        if (i % 2 == 0)
        {
            sum_rest += digit;
        }
        else
        {
            int product = digit * 2;
            sum_doubled += product / 10 + product % 10;
        }
        temp /= 10;
    }

    if ((sum_doubled + sum_rest) % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    temp = number;
    while (temp >= 100)
    {
        temp /= 10;
    }
    int first2 = temp;
    int first1 = first2 / 10;

    if (length == 15 && (first2 == 34 || first2 == 37))
    {
        printf("AMEX\n");
    }
    else if (length == 16 && first2 >= 51 && first2 <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if ((length == 13 || length == 16) && first1 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID");
    }
}
