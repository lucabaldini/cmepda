#include <iostream>
struct Complex { float i,r;};

template <class T>
class Vector3D {
 public:
    float norm2() {return x*x+y*y+z*z; }
    T x;    T y;    T z;
};

template <>  //specialization 
float Vector3D<Complex>::norm2() {return -x.i*x.i+x.r*x.r-y.i*y.i+y.r*y.r-z.i*z.i+z.r*z.r;}

int main(){
    Vector3D<Complex> v;   
    v.x.r=1;v.x.i=0;
    v.y.r=0;v.y.i=1;
    v.z.r=0;v.z.i=0;   // (1,i,0)
    std::cout << v.norm2() << std::endl; // 0
}



