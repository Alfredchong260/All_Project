#include <stdio.h>

int main()
{
    int pizzaToEat = 123;
    pizzaToEat ++;
    int output = pizzaToEat --;

    printf("%i\n", output);
    printf("%i\n", pizzaToEat);

    pizzaToEat = pizzaToEat + 100;
    printf("%i\n", pizzaToEat);
    return 0;
}
