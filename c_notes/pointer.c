#include <stdio.h>

int main() {
  int u = 5;
  int v;
  int *pu; // Declare pointer to an integer variable
  int *pv; // Declare pointer to an integer variable

  pu = &u; // Assign address of u to pu
  v = *pu; // Assign value of u to v
  pv = &v; // Assign address of v to pv

  printf("\nu = %d  &u = %X  pu = %X  *pu = %d", u, &u, pu, *pu);
  printf("\nv = %d  &v = %X  pv = %X  *pv = %d\n", v, &v, pv, *pv);

  return 0;
}
