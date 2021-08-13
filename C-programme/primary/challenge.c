#include <stdio.h>
#include <math.h>

int main()
{
    double x;
    double y;

    printf("This will calculate the hypotenuse of a right triangle. \n");

    printf("Enter the first value : ");
    scanf("%lf", &x);

    printf("Enter the second value : ");
    scanf("%lf", &y);

    double z = sqrt((x * x) + (y * y));

    printf("The hypotenuse of is %f\n", z);

    return 0;
}
