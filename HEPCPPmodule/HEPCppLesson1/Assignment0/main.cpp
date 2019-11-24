#include "tools.h"

int main(){
  printSomething();
}
/*
$ gcc tools.cpp -fpic -c
$ gcc -shared -o libtools.so tools.o
$ g++ main.cpp -ltools -L.
$ LD_LIBRARY_PATH=. ./a.out
*/
