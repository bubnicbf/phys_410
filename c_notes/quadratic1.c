#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main()
{
  double a, b, c, d, e, x1, x2;

  /* Read input data */

  printf("\na = ");
  scanf("%lf", &a);
  printf("b = ");
  scanf("%lf", &b);
  printf("c = ");
  scanf("%lf", &c);

  /* Perform calculation */
  e = b * b - 4. * a * c;

  if (e < 0.)
    {
      printf("\nError: roots are complex\n");
      exit(1);
    }

  /* Test for a = 0. */
  if (a == 0.)
    {
      printf("\nError: a = 0.\n");
      exit(1);
    }

  /* Perform calculation */
  d = sqrt(e);
  
  x1 = (-b + d) / (2. * a);
  x2 = (-b - d) / (2. * a);

  /* Display output */
  printf("\nx1 = %12.3e   x2 = %12.3e\n", x1, x2);

  return 0;
}

