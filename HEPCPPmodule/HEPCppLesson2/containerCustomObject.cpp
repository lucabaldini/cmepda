#include <vector>
#include <map>
class Particle{
  public:
     Particle(float px, float py, float pz) : px_(px), py_(py), pz_(pz) {} 
     float px_,py_,pz_, mass_, tau_;
     };
bool operator<(const Particle & p1, const Particle &p2)
{
    if(p1.px_ < p2.px_) return true;
    if(p1.py_ < p2.py_) return true;
    if(p1.pz_ < p2.pz_) return true;
    if(p1.mass_ < p2.mass_) return true;
    return (p1.tau_ < p2.tau_);
}
int main()
{
   std::vector<Particle> myParticles;
   myParticles.push_back(Particle(1.,2,100));

  //without the operator< above it would say:
  //error: no match for 'operator<' (operand types are 'const Particle' and 'const Particle')   
   std::map<Particle,std::vector<Particle>> decays;
   decays[Particle(3,4,5)]=myParticles;
}



