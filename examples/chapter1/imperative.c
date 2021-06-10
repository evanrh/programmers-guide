#include <stdio.h>

void do_something(int a) {
   return;
}

int main(void) {
   int a = 0;
   do_something(a);
   printf("a is: \n", a);
   return 0;
}
