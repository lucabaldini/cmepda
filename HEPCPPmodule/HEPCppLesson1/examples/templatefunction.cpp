#include <iostream>

template <class theType> 
theType minimum(const theType &a, const theType &b) {
return (a<b)?a:b;
}

int main()
{
    std::cout << minimum(2.7,3.4) << std::endl;
    std::cout << minimum<int>(2.7,3.4) << std::endl;
}
/*
2.7
2
*/
