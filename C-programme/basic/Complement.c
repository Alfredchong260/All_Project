#include <stdio.h>

int main()
{
    char name[31];

    printf("Please enter your name :");
    scanf("%s", name);

    printf("Hello %s\n", name);

    return 0;
}
