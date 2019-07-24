#include <stdio.h>

/* Function prototype for host fun. */
void cube(double (*)(double), double, double *);

double fun1(double);  // Function prototype for first guest function
double fun2(double);  // Function prototype for second guest function

int main()
{
  double x, res1, res2;

  /* Input value of x */
  printf("\nx = ");
  scanf("%lf", &x);

  /* Evaluate cube of value of first guest function at x */
  cube(fun1, x, &res1);

  /* Evaluate cube of value of second guest function at x */
  cube(fun2, x, &res2);

  /* Output results */
  printf("\nx = %8.4f  res1 = %8.4f  res2 = %8.4f\n", x, res1, res2);

  return 0;
}


void cube(double (*fun)(double), double x, double *result)
{

  double y;

  y = (*fun)(x);       // Evaluate guest function at x
  *result = y * y * y; // Cube value of guest function at x

  return;
}

double fun1(double z)
{
  /*
    First guest function
  */

  return 3.0 * z * z - z;
}

double fun2(double z)
{
  /*
    Second guest function
  */

  return 4.0 * z - 5.0 * z * z * z;
}
