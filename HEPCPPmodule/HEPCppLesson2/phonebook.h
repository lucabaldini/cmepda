#ifndef PHONEBOOK_H
#define PHONEBOOK_H

#include <string>
#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <fstream>
#include <algorithm> 
#include <sstream>

class PhoneBookEntry {
 public:
     PhoneBookEntry(){}
     PhoneBookEntry(const std::string & nam, const std::string & num,  const std::string mail) :
	     name(nam), phoneNumber(num), email(mail) {}
     void print(){
	std::cout << " ---- " << name << " ------------------------" << std::endl;
	std::cout << email << std::endl << phoneNumber <<std::endl;
        for(std::map<std::string,std::string>::const_iterator it = additionalPhones.begin();
		it != additionalPhones.end(); it++){
		std::cout << it->first << " " << it->second << std::endl;
	}
     }
     bool operator<(const PhoneBookEntry & other) { return name < other.name; } 
     // no data hiding, let's keep it simple
     std::string name;
     std::string phoneNumber;
     std::map<std::string,std::string> additionalPhones;
     std::string email;
};


class PhoneBook {
	public:
	   PhoneBook(){}

	   void addEntry(const PhoneBookEntry & entry) { entries.push_back(entry);}
	   std::pair<PhoneBookEntry ,bool>  findByName(const std::string name) { 
		for(size_t i=0;i<entries.size();i++){
			if(entries[i].name == name) return std::pair<PhoneBookEntry ,bool>(entries[i],true);
		}
		return std::pair<PhoneBookEntry,bool>(PhoneBookEntry(),false);
	   }
	   void printAll(){
		for(size_t i=0;i<entries.size();i++) entries[i].print();
	   }
	   void addItalianPrefixToAllNumbers(){
		   std::transform(entries.begin(),entries.end(),entries.begin(), addItalianPrefix);
	   }

	   static PhoneBookEntry addItalianPrefix(const PhoneBookEntry & e)
	   {
		PhoneBookEntry en=e;
		if(en.phoneNumber.length() == 0) return en ; 
		if(en.phoneNumber[0] != '+')
		{
			en.phoneNumber="+39"+en.phoneNumber;
		}
		return en;
	   }

	   void save() {
		   std::ofstream myfile;
		myfile.open ("phonebook.txt");
		for(size_t i=0;i<entries.size();i++){
		  myfile << entries[i].name << "," << entries[i].phoneNumber << ","  << entries[i].email << std::endl;
		}
  		myfile.close();
	   }
	   void load() {
		   std::string line;
		   std::ifstream myfile_in ("phonebook.txt");
		  if (myfile_in.is_open())
		  {
		    PhoneBookEntry e;
		    std::string entry;
		    while ( std::getline (myfile_in,entry))
		    {
			std::vector<std::string> fields;
			std::string field;
			std::stringstream sstr(entry);
			while(std::getline(sstr,field,',')) fields.emplace_back(field);
			e.name=fields[0];
			e.phoneNumber=fields[1];
			e.email=fields[2];
		    }
		    myfile_in.close();
		  }

		  else std::cout << "Unable to open file";
	  }

	   void sort(){
		std::sort(entries.begin(),entries.end());
	   }
	private:	   
	   std::vector<PhoneBookEntry> entries;


};

#endif
