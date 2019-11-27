#include <iostream>
#include <map>

using namespace std;
int main()
{
  map<int,float> dict;
  dict[10]=-1.;
  dict[7]=1.13;
  cout << "item 2 : " << dict[2] << endl;
  //hate this below? you will love C++17!
  for(map<int,float>::const_iterator it=dict.begin(); it!=dict.end() ; it++){
    cout << it->first << " => " << it->second << endl;
  }
  
}


