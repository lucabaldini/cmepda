#include <any>
#include <iostream>
#include <vector>
#include <unordered_map>
int main()
{
    typedef std::unordered_map<std::any,std::any> pydict;
    pydict dict = {{"hello",1.3},{3,75},{10,"yes"},{true,false}};
    for(auto [k,v] : dict) {std::cout << k << " " << v << "\n";} 
}


