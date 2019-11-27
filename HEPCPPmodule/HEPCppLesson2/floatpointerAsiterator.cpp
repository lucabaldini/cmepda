#include <iostream>

int main ()
{
  float a[] = {10,2,4,5};
  typedef float * floatiterator ;
  floatiterator begin= a;
  floatiterator end= a+4;

  for(floatiterator it=begin; it!=end;it++){
    std::cout << *it << " at position " << (it-begin) << std::endl;
  }

}


