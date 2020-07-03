#include <stdio.h>

extern int *fn1(int a, int b, char *c[]); 
register int ff; 

int fn2() { 
  static unsigned long int k = 1, i; 
  for(i = 0; i < 10; i++) { 
    k=(k-1)*i;
  } 
} 


int main() {
  int var = - 5;
  char *myvect[] = {"Winter", "Summer"}; 
  var = + 7; 
    
  while(fn1(2,3, myvect) != 0) { 
    ff++; 
  } 
  return ff; 
}
