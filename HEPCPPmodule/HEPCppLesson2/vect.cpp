#include <vector>

int main()
{
  std::vector<float> v(100,-1372);
  float a[100];
  
  v[1]=75.;
  a[1]=75;
  
  //vectors can be copied!
  std::vector<float> anotherv=v;
  
  //vectors can be resized!
  v.resize(120);
  v[105]=19;
  
  //we can append to vectors
  v.push_back(1273);

  v[100000]=1;
//Segmentation fault (core dumped)

  v.at(100000)=1;
//terminate called after throwing an instance of 'std::out_of_range'
//  what():  vector::_M_range_check: __n (which is 100000) >= this->size() (which is 121)
//Aborted (core dumped)

}
