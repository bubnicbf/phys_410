#include <stdio.h>
#include <math.h>

int main()
{
  double a, b, c, d, x1, x2;

  /* Read input data */

  printf("\na = ");
  scanf("%lf", &a);
  printf("b = ");
  scanf("%lf", &b);
  printf("c = ");
  scanf("%lf", &c);

  /* Perform calculation */
  d = sqrt(b * b - 4. * a * c);
  x1 = (-b + d) / (2. * a);
  x2 = (-b - d) / (2. * a);

  /* Display output */
  printf("\nx1 = %12.3e   x2 = %12.3e\n", x1, x2);

  return 0;
}

