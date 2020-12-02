#include <iostream>
#include "../fileReader.h"
#include <string>
using namespace std;

int amountPatternMatches(string str, char pattern) {
  int amount = 0;
  for(int i = 0; i < str.size(); i++) {
    if (str[i] == pattern) amount++;
  }
  return amount;
}

bool patternMatches(string str, char pattern, int pos) {
  return (str[pos] == pattern);
}

int main() {
  vector<string> input = readFile("input.txt");

  int amountMatches = 0;
  int amountMatches2 = 0;

  for(int i = 0; i < input.size(); i++) {
    int posColon = input[i].find(':');
    string password = input[i].substr(posColon+2);
    
    string tmp = input[i].substr(posColon - 1, 1);
    char pattern = tmp[0];

    int posHyphen = input[i].find('-');
    int first = stoi( input[i].substr(0, posHyphen) );
    int second = stoi( input[i].substr(posHyphen + 1, posColon - 1) );

    int amount = amountPatternMatches(password, pattern);
    if (amount >= first && amount <= second) amountMatches++;

    if ( (patternMatches(password, pattern, first-1) && !patternMatches(password, pattern, second-1)) 
        || (!patternMatches(password, pattern, first-1) && patternMatches(password, pattern, second-1)) ) {
          amountMatches2++;
    } 
  }
  cout << "Puzzle 1: " << amountMatches << endl;
  cout << "Puzzle 2: " << amountMatches2 << endl;
  return 0;

}

