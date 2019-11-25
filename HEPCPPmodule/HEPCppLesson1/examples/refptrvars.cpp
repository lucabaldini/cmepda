#include <iostream>  
int main() {  
 float a=0;
 float b=a;
 float * ap = &a;
 float & ar = a;
 const float * acp = &a;
 const float & acr = a;
 std::cout << a << " " << b <<  " " << *ap << " " << ar
           << " " << *acp << " " << acr << std::endl;
 a=1.0;
 std::cout << a << " " << b <<  " " << *ap << " " << ar
           << " " << *acp << " " << acr << std::endl;
 *ap=2;
 std::cout << a << " " << b <<  " " << *ap << " " << ar
           << " " << *acp << " " << acr << std::endl;
 ar=3;
 std::cout << a << " " << b <<  " " << *ap << " " << ar
           << " " << *acp << " " << acr << std::endl;
 ap=&b;           
 std::cout << a << " " << b <<  " " << *ap << " " << ar
           << " " << *acp << " " << acr << std::endl;
/*
0 0 0 0 0 0
1 0 1 1 1 1
2 0 2 2 2 2
3 0 3 3 3 3
3 0 0 3 3 3
*/
// Illegal statements (would not compile)
// ar=&b;  //error: cannot convert 'float*' to 'float' in assignment
//*acp=4;  //error: assignment of read-only location '* acp'
// acr=4;   //error: assignment of read-only reference 'acr'
} 
