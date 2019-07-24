#include <stdio.h>
#include <stdlib.h>

/* Prototype for function factorial() */
double factorial(int);

int main()
{
  int j;

  /* Print factorials of all integers between 0 and 20 */
  for (j = 0; j <= 20; ++j)
    printf("j = %3d    factorial(j) = %12.3e\n", j, factorial(j));

  return 0;
}

double factorial(int n)
{
  /*
    Function to evaluate factorial (in floating-point form)
    of non-negative integer n.
  */

  int count;
  double fact = 1.;

  /* Abort if n is negative integer */
  if (n < 0)
    {
      printf("\nError: factorial of negative integer not defined\n");
      exit(1);
    }

  /* Calculate factorial */
  for (; n > 0; --n) fact *= (double) count;

  /* Return value of factorial */
  return fact;
}

