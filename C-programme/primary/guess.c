#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int maxValue = 5;
    // Generate random number
    srand(time(NULL));
    int randomNumber = rand() % 6;

    printf("%d\n", randomNumber);

    printf("Guess a number 0 - 5 : ");
    int input;
    scanf("%d", &input);

    printf("You guessed %d", input);
    printf("The correct answer is %d\n", randomNumber);

    if (input == randomNumber) 
    {
        printf("You Win\n");
        return 0;
    }
    else {
        printf("You Lose\n");
        return 0;
    }

    printf("Thank for playing");
    return 0;
}
