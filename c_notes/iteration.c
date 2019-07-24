#include <stdio.h>
#include <math.h>
#include <stdlib.h>

/* Set max. allowable no. of iterations */
#define NITER 30

int main()
{
  double a, b, eps, x, x0, dx = 1., d;
  int count = 0;

  /* Read input data */
  printf("\na = ");
  scanf("%lf", &a);
  printf("b = ");
  scanf("%lf", &b);
  printf("eps = ");
  scanf("%lf", &eps);

  /* Read initial guess for x */
  printf("\nInitial guess for x = ");
  scanf("%lf", &x);
  x0 = x;

  while (dx > eps) // Start iteration loop: test for convergence
    {
      /* Check for too many iterations */
      ++count;
      if (count > NITER)
	{
	  printf("\nError: no convergence\n");
	  exit(1);
	}

      /* Reject complex roots */
      d = b - a * x * x;
      if (d < 0.)
	{
	  printf("Error: complex roots - try another initial guess\n");
	  exit(1);
	}

      /* Perform iteration */
      x = pow(d, 0.2);
      dx = fabs( (x - x0) / x );
      x0 = x;

      /* Output data on iteration */
      printf("Iter = %3d  x  = %8.4f   dx = %12.3e\n", count, x, dx);
    }
  return 0;
}

    
 
