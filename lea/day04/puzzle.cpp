#include <iostream>
#include <vector>
#include <string>
#include <regex>
#include "../fileReader.h"
#include "../stringUtils.h"
using namespace std;

string getMeasuring(string str) {
  smatch matches;
  if (regex_search(str, matches, regex("(in|cm)")) ) {
    return matches[0].str();
  }
  return "";
}

bool isEyeColor(string str) {
  smatch matches;
  return regex_search(str, matches, regex("amb|blu|brn|gry|grn|hzl|oth"));
}


bool valid(string line, string prefix) {
   int tmp = line.find(prefix + ":");
   if (tmp == string::npos) return false;
   
   smatch matches;
   int whitespace = line.find_first_of(" ", tmp);  
   string value = line.substr(tmp + 4 , (whitespace - (tmp + 4)));

   if (prefix == "byr" && checkStringContainsOnlyDigits(value, 4) 
    && (getNumberFromString(value) >= 1920 && getNumberFromString(value) <= 2002) ) {
      return true;
   } else if (prefix == "iyr" && checkStringContainsOnlyDigits(value, 4) 
    && (getNumberFromString(value) >= 2010 && getNumberFromString(value) <= 2020) ) {
      return true;
   } else if (prefix == "eyr"  && checkStringContainsOnlyDigits(value, 4)
    && (getNumberFromString(value) >= 2020 && getNumberFromString(value) <= 2030)) {
      return true;
   } else if (prefix == "hgt") {
      int number = getNumberFromString(value);
      string measure = getMeasuring(value);
      if ( (measure == "cm" && number >= 150 && number <= 193) || (measure == "in" && number >= 59 && number <= 76) ) { 
        return true;
      }
   } else if (prefix == "hcl" && isHexColor(value)) {
      return true;
   } else if (prefix == "ecl" && isEyeColor(value)) {
      return true;
   } else if (prefix == "pid" && checkStringContainsOnlyDigits(value, 9)) {
      return true;
   }

   return false;
}


int main() {
  vector<string> lines = readFile("input.txt");

  int counter = 0;

  for(int i = 0; i < lines.size(); i++) {
    string line = lines[i];
    while (!lines[i+1].empty()) {
      line += " " + lines[i+1] + " ";
      i++;
    }
    
    if (valid(line, "byr") && valid(line, "iyr") && valid(line, "eyr") && valid(line, "hgt")
      && valid(line, "hcl") && valid(line, "ecl") && valid(line, "pid") ) {
      counter++;
    }
  }
   cout << "Valid passwords: " << counter << endl;
}
