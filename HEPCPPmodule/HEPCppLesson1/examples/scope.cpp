#include <iostream>
int main()
{
 int a= 1;
 int b= 10;
 std::cout << a << std::endl;
 std::cout << b << std::endl << std::endl;
 {
     int a=100; 
     b=1000; 
     int c=10000;
     std::cout << a << std::endl;
     std::cout << b << std::endl;
     std::cout << c << std::endl << std::endl;
 }
 std::cout << a << std::endl;
 std::cout << b << std::endl;
 //Would not compile:
 //std::cout << c << std::endl; //error: 'c' was not declared in this scope
}
/*
1
10

100
1000
10000

1
1000*/
