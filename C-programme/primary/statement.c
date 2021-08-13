#include <stdio.h>
#include <stdbool.h>

int main()
{
    bool x = true;
    int temp;

    printf("Do you want to execute if statement? 1 is true, 0 is false : ");
    scanf("%d", &temp);

    x = temp;

    // if statement
    if (x) // true as long as not zero!
    {
        printf("Hello World!\n");
    }
    
    printf("The end\n");

    
    // Switch statement

    int slices;
    printf("How many pizza slices you eat (tell the truth) : ");
    scanf("%d", &slices);
    int caloriesperSlice = 250;

    switch (slices)
    {
        case 1:
            printf("You did a bad job! Try to eat 2 next time\n");
            break;

        case 2:
            printf("You did an OK job!\n");
            break;

        case 3:
            printf("You did a good job!\n");
            break;

        case 4:
            printf("You did a great job\n");
            break;
        default:
            printf("Enjoy your heart disease\n");
            break;
   } 

   printf("You have %d calories.", caloriesperSlice * slices);

    return 0;
}
