#include <iostream>
#include <fstream>
using namespace std;

int main () {
  ofstream myfile;
  myfile.open ("example.txt");
  myfile << "One line in a  file.\n";
  myfile << "Another line in a  file.\n";
  myfile.close();
  
  string line;
  ifstream myfile_in ("example.txt");
  if (myfile_in.is_open())
  {
    while ( getline (myfile_in,line) )
    {
      cout << line << '\n';
    }
    myfile_in.close();
  }

  else cout << "Unable to open file"; 
  return 0;
}

