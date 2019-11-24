#ifndef TWOBODIES_H
#define TWOBODIES_H
#include "particle.h"
#include <iostream>
class TwoBodiesDecayedParticle : public Particle {
   public:
	TwoBodiesDecayedParticle(const Particle & p1, const Particle &p2,int pid=0, float tau=0) : 
		Particle(p1+p2,pid,tau),m_p1(p1), m_p2(p2) {}
	void print() const {
	    std::cout << "Combined pt and mass" << std::endl ;
	    std::cout << pt() << " " << m() << std::endl;
	    std::cout << "Particle 1" << std::endl ;
	    std::cout << m_p1.pt() << " " << m_p1.m() << " " << m_p1.pid() << std::endl;
	    std::cout << "Particle 2" << std::endl ;
	    std::cout << m_p2.pt() << " " << m_p2.m() << " " << m_p2.pid() << std::endl;

	}
   private:
	Particle m_p1;
	Particle m_p2;
};
#endif
