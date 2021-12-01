#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include "../fileReader.h"
#include "../stringUtils.h"
using namespace std;

void getBinaryFromString(string str, char* bin) {
    for(int i = 0; i < 36; i++) {
      bin[i] = '0';
    }

    int j = 35; 
    for(int i = str.size() - 1; i >= 0; i--, j--) {
      bin[j] = str.at(i);
    }
}


void overwriteBits(char* first, char* second, char* result) {
    for(int i = 35; i >= 0; i--) {
      if (first[i] != 'X') {
        result[i] = first[i];
      } else {
        result[i] = second[i];
      }
    }
}


void decToBin(unsigned long int dec, char* bin) {
  for(int i = 35; i >= 0; i--) {
    if (dec !=  0) {
      bin[i] = (dec % 2) + '0';
      dec = dec / 2;
    } else {
      bin[i] = '0';
    }
  }
}


unsigned long int binToDec(char* bin) {
  unsigned long int res = 0;
  int j = 0;
  for(int i = 35; i >= 0; i--, j++) {
    if (bin[i] == '1') {
      res += pow(2, j);
    }
  }
  return res;
}


void part1(vector<string> lines) {
  map<unsigned long int, unsigned long int> memory;
  char mask[36];

  for(int i = 0; i < lines.size(); i++) {
    if (lines[i].find("mask") != string::npos) {
      getBinaryFromString(lines[i].substr(lines[i].find("=") + 2, lines[i].size() - 1), mask);
      continue;
    }

    int value = getNumberFromString(lines[i].substr(lines[i].find("=") + 2, lines[i].size() - 1));
    char bin[36];
    decToBin(value, bin);
    
    char result[36];
    overwriteBits(mask, bin, result);

    unsigned long int resDec = binToDec(result);
    
    unsigned long int memoryAddress = getNumberFromString(lines[i].substr(lines[i].find("[") + 1, lines[i].find("]") ));
    memory[memoryAddress] = resDec;
  }

  unsigned long int sum = 0;
  for(auto const& x : memory) {
    sum += x.second;
  }

  cout << sum << endl;
}


void decode(char* mask, char* other, char* result) {
  for(int i = 35; i >= 0; i--) {
    if (mask[i] == '1' || mask[i] == 'X') {
      result[i] = mask[i];
    } else if (mask[i] == '0') {
      result[i] = other[i];
    } 
  }
}


void part2(vector<string> lines) {
  map<unsigned long int, unsigned long int> memory;
  
  char mask[36];

  for(int i = 0; i < lines.size(); i++) {
    if (lines[i].find("mask") != string::npos) {
      getBinaryFromString(lines[i].substr(lines[i].find("=") + 2, lines[i].size() - 1), mask);
      continue;
    }

    unsigned int memAddress = getNumberFromString(lines[i].substr(lines[i].find("[") + 1, lines[i].find("]") ));
    char memAddressBin[36];
    decToBin(memAddress, memAddressBin);
 
    char result[36];
    decode(mask, memAddressBin, result);
    
    unsigned int value = getNumberFromString(lines[i].substr(lines[i].find("=") + 2, lines[i].size() - 1));
    
    int ctr = 0;
    for(int i = 0; i < 36; i++) {
      if (result[i] == 'X') ctr++;
    }

    vector<unsigned long int> all;
    for(int i = 0; i < pow(2, ctr); i++) {
      char tmp[36];
      int k = 35;
      decToBin(i, tmp);

      char copyArr[36];
      copy(begin(result), end(result), begin(copyArr));
      
      for(int j = 35; j >= 0; j--) {
        if (copyArr[j] == 'X') {
          copyArr[j] = tmp[k];
          k--;
        }
      }
      unsigned long  int t = binToDec(copyArr);
      all.push_back(t);

    }
    for(int i = 0; i < all.size(); i++) {
      memory[all[i]] = value; 
    }

  }

  unsigned long int sum = 0;
  for(auto const& x : memory) {
    sum += x.second;
  }

  cout << "sum: " <<  sum << endl;


}


int main() {
  vector<string> lines = readFile("input2.txt");
  
  part1(lines);
  part2(lines);
  
  return 0;
}
