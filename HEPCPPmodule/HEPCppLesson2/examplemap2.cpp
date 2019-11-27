#include <iostream>
#include <map>
int main ()
{
  std::map<char,int> mymap;

  // first insert function version (single parameter):
  mymap.insert ( std::pair<char,int>('a',100) );
  mymap.insert ( std::pair<char,int>('z',200) );

  std::pair<std::map<char,int>::iterator,bool> ret;
  ret = mymap.insert ( std::pair<char,int>('z',500) );
  if (ret.second==false) {
    std::cout << "element 'z' already existed";
    std::cout << " with a value of " << ret.first->second << '\n';
  }
  
  std::map<char,int>::iterator found=mymap.find('a');
  if(found != mymap.end() )
  {
      std::cout << "Found with value " << found->second << std::endl;
  } else {
      std::cout << "Not found :-( " << std::endl;
  }  
}


