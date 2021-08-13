#include <stdio.h>

int main()
{
    printf("The number of eggs :");

    int eggs;
    scanf("%i", &eggs);

    double dozen = eggs / (double)12;

    printf("You have %f dozen of eggs.\n", dozen);

    return 0;
}
