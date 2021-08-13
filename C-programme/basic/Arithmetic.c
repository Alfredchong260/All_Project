#include <stdio.h>

int main()
{
    /* int x = 2 / 3 + 4 + 5 - 3; */
    /* int y = 5 % 2; */
    /* printf("%i\n", y); */

    int piecesOfPizze = 5;
    int numberOfEaters = 2;
    int leftOver = piecesOfPizze % numberOfEaters;

    printf("%i\n", leftOver);

    return 0;
}
