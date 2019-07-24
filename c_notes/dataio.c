#include <stdio.h>

int k = 3;
double x = 5.4, y = -9.81;

FILE *output;

int main()
{
  output = fopen("data.out", "w");
  if (output == NULL)
    {
      printf("Error opening file data.out\n");
    }

  fprintf(output, "k = %3d  x + y = %9.4f  x*y = %11.3e\n", k, x + y, x*y);

  fclose(output);
}

