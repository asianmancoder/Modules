#include <stdio.h>
#include <stdlib.h>


int main() {
  int *ptr;
  int sum = 0;
  int n;
  int e;

  printf("How many elements? ");
  scanf("%d", &n);
  int arr[n];
  ptr = arr;

  printf("The element int values will start from? ");
  scanf("%d", &e);

  for(int i = 0; i < n; i++) {
    *(ptr + i) = e;
    e++;
  }

  for(int a = 0; a < n; a++) {
    printf("%d\n", ptr[a]);
  }

  return 0;
}
