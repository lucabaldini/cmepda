#include "TMath.h"
float func(Float_t px, Float_t py, Float_t pz){
  return px*TMath::Sin(py)/TMath::Log(pz+1);
}
