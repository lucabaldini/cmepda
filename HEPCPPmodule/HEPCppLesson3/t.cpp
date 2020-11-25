#include <iostream>
#include <tuple>
#include <utility>
 
int add(int first, int second) { return first + second; }
 
template<typename T>
T add_generic(T first, T second) { return first + second; }
 
auto add_lambda = [](auto first, auto second) { return first + second; };
 
int main()
{
    // OK
    std::cout << std::apply(add, std::make_tuple(1, 2,3)) << '\n';
 
}
