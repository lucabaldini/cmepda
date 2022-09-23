#include "phonebook.h"
#include <iostream>

int main(){
 PhoneBook directory;
 directory.addEntry(PhoneBookEntry("Luca","0502222222", "luca@unipi.it"));

 PhoneBookEntry andrea = PhoneBookEntry("Andrea Rizzi","050 2214326", "andrea.rizzi@unipi.it");
 andrea.additionalPhones["Cellulare"]="00000";
 directory.addEntry(andrea);
 
 std::pair<PhoneBookEntry, bool> queryResult = directory.findByName("Andrea");
 if(queryResult.second){
	std::cout<< queryResult.first.phoneNumber << std::endl;
	queryResult.first.print();
 }
 directory.printAll();
 directory.sort();
 directory.addItalianPrefixToAllNumbers();
 directory.save();
 directory.load();
 directory.printAll();
  
}
