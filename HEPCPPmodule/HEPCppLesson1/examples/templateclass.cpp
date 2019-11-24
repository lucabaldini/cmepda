#include <iostream>

template <class T>
class Vector3D {
 public:
    T norm2() {return x*x+y*y+z*z; }
    T x;
    T y;
    T z;
};

int main(){
    Vector3D<double> vd;
    Vector3D<float> vf;
    std::cout << sizeof(vd) << " vs " << sizeof(vf) << std::endl; //24 vs 12
    vd.x=2; vd.y=0; vd.z=0;
    std::cout << vd.norm2() << std::endl; //4
}


