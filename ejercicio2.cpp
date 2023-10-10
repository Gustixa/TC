#include <stdio.h>
#include <time.h>

void my_function(int n)
{
    if (n <= 1)
    {
        return;
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            // printf("Sequence\n");
            break;
        }
    }
}

int main()
{
    int n_values[] = {1, 10, 100, 1000, 10000, 100000, 1000000};
    int num_values = sizeof(n_values) / sizeof(n_values[0]);

    printf("n\tTime (seconds)\n");

    for (int i = 0; i < num_values; i++)
    {
        int n = n_values[i];
        clock_t start = clock();
        my_function(n);
        clock_t end = clock();
        double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;
        printf("%d\t%f\n", n, elapsed_time);
    }

    return 0;
}
