#include <stdio.h>

int main()
{
    int x, y;
    x = y = 5;

    int z = 20;
    y = 2;
    x = -y + z;

    printf("%i\n", x);
    
    return 0;
}
