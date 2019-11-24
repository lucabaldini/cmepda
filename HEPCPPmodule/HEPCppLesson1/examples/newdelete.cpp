#include <iostream>
class Test {
 public:
    Test() {std::cout << "created " << this << std::endl; }
    ~Test() {std::cout << "deleting " << this << std::endl; }
};

int main(){
    Test a;
    {
        Test b;
        Test *c = new Test();
        Test *d = new Test();
        delete d;
    std::cout<<"==last line of inner scope" << std::endl;
    }

std::cout<<"==last line of main" << std::endl;
}





