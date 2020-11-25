#include <map>
#include <iostream>
#include <string>
using namespace std;
int main()
{
  map<string,int> m { {"red",1},{"blue",2}};
  for (auto & [k, v] : m) {
	  v+=1;
  }
  for (auto [k, v] : m) {
	  cout << k << "->" << v << std::endl;   
  }
}

