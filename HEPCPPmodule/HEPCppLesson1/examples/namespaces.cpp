#include <iostream>
namespace myVars {
    int a=1;
    float b=7;
}

int main()
{ 
   std::cout << myVars::a << std::endl;
   
// not compiling:
// std::cout << a << std::endl;
/*In function 'int main()':
8:15: error: 'a' was not declared in this scope
8:15: note: suggested alternative:
3:9: note:   'myVars::a'*/

  using  myVars::a;
  std::cout << a << std::endl;
  using namespace myVars;
  std::cout << a << " " << b << std::endl;
}


