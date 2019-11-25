#include "fourvector.h"
#include <iostream>
int main()
{
 
 VectorXYZT<float> p4_a(0,50.,7.,100.);
 VectorPtEtaPhiMass<double> p4_b(50,0.5,1.7,10.);
 std::cout << p4_a.m() << " " << p4_a.pt() << std::endl;
 std::cout << p4_b.m() << " " << p4_b.pt() << std::endl;
 std::cout << (p4_a+p4_b).m() << " " << (p4_a+p4_b).pt() << std::endl;
}
