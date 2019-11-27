#include <iostream>
#include <vector>
#include <algorithm>
class Complex{
    public:
    Complex(float real, float img) : r(real),i(img) {}
    float r; float i;
};
std::ostream& operator<<(std::ostream & o,const Complex &c) { return o << "Real " << c.r << " Img " << c.i;}

class CompareReal{
    public:
        bool operator() (const Complex & a, const Complex &b) {return a.r<b.r;}
};

struct CompareImg{
 bool operator()(const Complex & a, const Complex &b) {return a.i<b.i;}
};

int main()
{
   std::vector<Complex> v;
   v.push_back(Complex(1,2));
   v.push_back(Complex(2,1));
   v.push_back(Complex(3,3));
   sort(v.begin(),v.end(),CompareReal());
   for(size_t i=0;i<v.size();i++) std::cout << v[i] << std::endl;
   sort(v.begin(),v.end(),CompareImg());
   for(size_t i=0;i<v.size();i++) std::cout << v[i] << std::endl; 
}



