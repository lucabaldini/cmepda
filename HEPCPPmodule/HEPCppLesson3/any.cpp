#include <any>
#include <iostream>
#include <vector>
#include <string>
int main()
{
    
    // any type
    std::any a = 1;
    std::cout << a.type().name() << ": " << std::any_cast<int>(a) << '\n';
    a = 3.14;
    std::cout << a.type().name() << ": " << std::any_cast<double>(a) << '\n';
    a = true;
    std::cout << a.type().name() << ": " << std::any_cast<bool>(a) << '\n';
    
    a.reset();
    if (!a.has_value())  {  std::cout << "no value\n";   }

    std::vector<std::any> v={1.2,"hello",7,true};
    for(auto a : v) {std::cout << a.type().name() << "\n";} 
}


