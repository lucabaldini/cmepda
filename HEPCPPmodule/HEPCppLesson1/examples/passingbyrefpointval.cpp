#include <iostream>

void myFunction(int a, int *ap, int &ar, const int * acp, const int & acr){
    a+=1;
    (*ap)+=1;
    ar+=1;
//would not compile:
//    (*acp)+=1;
//    acr+=1;
//    7:11: error: assignment of read-only location '* acp'
//8:8: error: assignment of read-only reference 'acr'
}
int main()
{
    int a=10;
    int b=20;
    int c=30;
    int d=40;
    int e=50;
    myFunction(a,&b,c,&d,e);
    std::cout << a << " " << b << " " << c << " " << d << " " << e << std::endl;
    //10 21 31 40 50
    myFunction(60,&b,c,&d,e); // works
    //would not work
    //myFunction(a,&b,60,&d,e); 
    //error: invalid initialization of non-const reference of type 'int&' from an rvalue of type 'int'
    myFunction(a,&b,c,&d,60); //works!!
    
}
