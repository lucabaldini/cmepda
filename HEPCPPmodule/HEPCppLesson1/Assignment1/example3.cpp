#include "particle.h"
#include "twobodies.h"
#include <iostream>
int main()
{
 Particle photon1(FourVector(0,50.,7.,100.), 22,1e99);
 Particle photon2(FourVector(0,30.,7.,100.), 22,1e99);
 TwoBodiesDecayedParticle pi0(photon1,photon2);
 pi0.print();
}
