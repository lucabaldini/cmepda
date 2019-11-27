#include <vector>
#include <algorithm>
#include <iostream>
int main()
{
   float a[] = {5.,3.1,1.0,7.32};
   std::vector<float> v(a,a+4);
   sort(v.begin(),v.end());
   for(size_t i=0;i<v.size();i++) std::cout << v[i] << std::endl;
   sort(v.rbegin(),v.rend());
   for(size_t i=0;i<v.size();i++) std::cout << v[i] << std::endl;
   sort(v.begin(),v.end(), std::greater<float>());
   for(size_t i=0;i<v.size();i++) std::cout << v[i] << std::endl;
}



