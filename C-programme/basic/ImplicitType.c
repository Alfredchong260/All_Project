#include <stdio.h>

// Add . to a constant
// Explicit type casting
int main()
{
    int x = 17;
    int people = 2;

    double y = (double) x / people;

    printf("%f\n", y);

    double c = 25 / 2 * 2;
    double d = 25 / 2 * 2.0;

    printf("c : %f\n", c);
    printf("d : %f\n", d);
    return 0;
}

