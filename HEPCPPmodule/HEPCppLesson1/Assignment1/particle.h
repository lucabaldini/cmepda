#ifndef PARTICLE_H
#define PARTICLE_H
#include "fourvector.h"
class Particle : public FourVector {
   public:
	Particle(const FourVector & p4,int pid,float tau) : FourVector(p4),m_pid(pid),m_tau(tau) {}
	int pid() const {return m_pid;}
	int tau() const {return m_tau;}

   private:
	int m_pid;
	float m_tau;

};
#endif
