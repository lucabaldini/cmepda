#include<iostream>
#include<tuple> 
#include<algorithm>
using namespace std; 

int main() 
{ 
    std::tuple <float, float, float> a; 
    a = make_tuple(1., 10., 15.5); 
  
    cout << "The initial values of tuple are : "; 
    cout << std::get<0>(a) << " " << std::get<1>(a); 
    cout << " " << std::get<2>(a) << endl; 
  
    // Use of get() to change values of tuple 
    std::get<0>(a) = 'b'; 
    std::get<2>(a) =  20.5; 
  
    cout << "The modified values of tuple are : "; 
    cout << std::get<0>(a) << " " << std::get<1>(a); 
    cout << " " << std::get<2>(a) << endl; 
    
    char c; int i; float f;
    std::tie(c,i,f) = a;
    cout << c << " " << i << " " << f << endl;
} 


