#include<iostream>
#include<tuple> 
#include<map>
using namespace std; 
int main() 
{ 
  map<float,int> m {{1.3,2},{9.5,10}};
  for(auto & kv : m) {
    float k; int v;
    tie(k,v) = kv;
    cout << k << "-> " << v << endl;
  }
} 


