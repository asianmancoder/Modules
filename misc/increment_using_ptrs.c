#include <stdio.h>

int main(void) {
  int i;
  int n;
  int *ptr = &i;
  int *incr = &n;

  printf("Enter an integer here: ");
  scanf("%d", &i);
  printf("Enter an integer to increment by: ");
  scanf("%d", &n);

  (*ptr) += (*incr);
  printf("The incremented value of integer i is: %d", i);

  return 0;
}
