#include <stdio.h>

int main()
{
    /* int max; */
    /* printf("Set the times you want to repeat : "); */
    /* scanf("%d", &max); */

    /* for (; max > 0; max = max - 2) */
    /* { */
    /*     printf("%d\n", max); */
    /* } */

    /* for (int i = 0; i < 11; i ++) */
    /* { */
    /*     for (int j = i; j >= 0; j--) */
    /*     { */
    /*         printf("%d ", j); */
    /*     } */
    /*     printf("\n"); */
    /* } */

    for (int i = 0; i < 10; i ++)
    {
        for (int j = 0; j <= i; j ++ )
        {
            printf("%d * %d = %d  ", i, j, i * j);
        }
        printf("\n");
    }
    return 0;
}
