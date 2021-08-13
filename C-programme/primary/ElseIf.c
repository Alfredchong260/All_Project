// This project will hold until start the loops concept
#include <stdio.h>

int main()
{
    printf("Choose a menu options:\n");
    printf("1. Add patient\n");
    printf("2. View patient\n");
    printf("3. Search patient\n");
    printf("4. Exit\n");

    int input;
    printf("Please type in your number : ");
    scanf("%d", &input);

    // if statement
    if (input == 1)
    {
       printf("Adding a patient\n");
    }

    else if (input == 2)
    {
        printf("Viewing a patient\n");
    }

    else if (input == 3)
    {
        printf("Searching a patient\n");
    }

    else if (input == 4)
    {
        printf("Exiting\n");
        printf("Do you want to save? Y/N : ");
        char q;

        getchar();
        scanf("%c", &q);

        if (q == 'Y' || q =='y')
        {
            printf("Saving changes\n");
        }
        else if (q == 'N' || q == 'n')
        {
            printf("Fine whatever\n");
        }
        else {
            printf("Invalid input, please check and re-enter\n");
        }
    }

    else
    {
        printf("Your input is not valid, please check and re-enter\n");
    }


    //switch statement
    /* switch (input) */
    /* { */
    /*     case 1: */
    /*         printf("Adding patient\n"); */
    /*         break; */
    /*     case 2: */
    /*         printf("Viewing patient\n"); */
    /*         break; */
    /*     case 3: */
    /*         printf("Searching patient\n"); */
    /*         break; */
    /*     case 4: */
    /*         printf("Exiting\n"); */
    /*         break; */
    /*     default: */
    /*         printf("Invalid number, please check and try again\n"); */
    /*         break; */
    /* } */
    return 0;
}
