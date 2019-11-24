#include "fourvector.h"
#include <iostream>
int main()
{
 FourVector p4_a(0,50.,7.,100.);
 FourVector p4_b(0,50.,7.,100.);
 std::cout << p4_a.m() << " " << p4_a.pt() << std::endl;
 std::cout << (p4_a+p4_b).m() << " " << (p4_a+p4_b).pt() << std::endl;
}
