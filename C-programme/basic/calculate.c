#include <stdio.h>

int main()
{
    int radius;

    printf("Please enter a radius :");
    scanf("%i", &radius);

    double area = 3.14159 * (radius * radius);
    printf("The area of the circle is %f and the radius is %i", area, radius);

    return 0;
}
