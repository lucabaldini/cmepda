// Example program
#include <iostream>
#include <string>
#include <math.h>
class Circle {
    public:
	Circle(){}
	Circle(float r) : radius_(r) {}
  	void setRadiusFromArea(float area) {radius_=sqrt(area);}
        void setRadius(float r) {radius_=r;}
        float area() const { return radius_*radius_*3.14159; }
        float radius() const {return radius_; }
    private:
        float radius_;
        
};

int main()
{
  Circle c;
  c.setRadius(3);
  const Circle & cr=c;
  std::cout << cr.area() << std::endl;
  c.setRadiusFromArea(314);
  std::cout << cr.radius() << std::endl;
 //would not compile:
 // cr.setRadiusFromArea(314);
 //error: passing 'const Circle' as 'this' argument of 'void Circle::setRadiusFromArea(float)' discards qualifiers 
}


