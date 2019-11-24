#include <iostream>

// Volume of a cube.
int Volume(int s) {
  return s * s * s;
}

// Volume of a cylinder.
double Volume(double r, int h) {
  return 3.1415926 * r * r * h;
}

//Would not compile
//Volume of a prism
//int Volume(double area, int h) {
//  return area*h;
//}
 //In function 'int Volume(double, int)':
//15:30: error: ambiguating new declaration of 'int Volume(double, int)'
//9:8: note: old declaration 'double Volume(double, int)'

int main() {
  std::cout << Volume(10) << std::endl;
  std::cout << Volume(2.5, 8)<< std::endl;

}


