#include <iostream>
#include <fstream>
using namespace std;

int main () {
  ofstream myfile;
  myfile.open ("example.txt");
  myfile << 1.3 << " " << 2.7 << std::endl;
  myfile << 100 << " " << 20 << std::endl;
  myfile.close();
  
  string line;
  ifstream myfile_in ("example.txt");
  if (myfile_in.is_open())
  {
    float a,b;
    while ( myfile_in >> a >> b )
    {
      cout << a << " " << b << '\n';
    }
    myfile_in.close();
  }

  else cout << "Unable to open file"; 
  return 0;
}

