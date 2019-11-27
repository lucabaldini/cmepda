#include <iostream>
using namespace std;
class Test{ 
    public:
        Test() {std::cout << "Creating " << this << std::endl;}
        ~Test() {std::cout << "Deleting " << this << std::endl;}
};
double division(int a, int b) {
   if( b == 0 ) {
      throw "Division by zero condition!";
   }
   return (a/b);
}

int main () {
   int x = 50;
   int y = 1.;
   double z;
   try {
      Test * t = new Test();; 
      z = division(x, y);
      delete t;
   } catch (const char* msg) {
     cerr << msg << endl;
     cerr << "I will set z to zero in this case" << endl;
     z=0;
   }
   cout << z << endl;
   return 0;
}
