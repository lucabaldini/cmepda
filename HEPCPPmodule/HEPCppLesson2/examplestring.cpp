#include <iostream>
#include <string>
int main()
{
 std::string s("Hello");
 s+=std::string(" ");
 s+="World";
 std::cout << s << std::endl;
 std::string replacement("Universe");
 std::string toreplace("World");
 if(replacement == toreplace){
    std::cout << "There is nothing to replace!" << std::endl;  
 }else if(s.find(toreplace)==std::string::npos) {
    std::cout << "Cannot find "<< toreplace << std::endl;  
 } else {
    s.replace(s.find(toreplace),toreplace.size(),replacement);
    std::cout << s << std::endl;
 }
}



