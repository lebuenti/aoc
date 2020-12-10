#include <iostream>
#include <string>
#include <vector>
#include "../fileReader.h"
#include "../stringUtils.h"
#include <map>
using namespace std;
int first(vector<vector<string>> instructions) {
  int acc = 0;
  int i = 0;

  while(true) {
    if (instructions[i][0] == "done") {
      break;
    }

    char vz = instructions[i][1].at(0);  
    int number = getNumberFromString(instructions[i][1]);
    if (vz == '-') number = number * (- 1);
    
    if (instructions[i][0] == "acc") {
      acc += number;
    } else if (instructions[i][0] == "jmp") {
      i += number - 1;
    }

    instructions[i][0] = "done";

    i = (i + 1) % instructions.size();
  }

  return acc;
}

int second(vector<vector<string>> instructions, int checkPos) {
  int acc = 0;
  int i = 0;

  if (instructions[checkPos][0] == "nop") {
    instructions[checkPos][0] = "jmp";
  } else if (instructions[checkPos][0] == "jmp") {
    instructions[checkPos][0] = "nop";
  }

  while(true) {
    if (instructions[i][0] == "done") {
      return 0;
    }

    char vz = instructions[i][1].at(0);  
    int number = getNumberFromString(instructions[i][1]);
    if (vz == '-') number = number * (- 1);

    
    if (instructions[i][0] == "acc") {
      acc += number;
    } else if (instructions[i][0] == "jmp") {
      i += number - 1;
    }

    instructions[i][0] = "done";
    if (i == (instructions.size() - 1)) break;

    i = (i + 1) % instructions.size();
  }

  return acc;
}

int main() {
 vector<string> lines = readFile("input2.txt");
 vector<vector<string>> instructions;
  
  for(int i = 0; i < lines.size(); i++) {
    int whiteSpacePos = lines[i].find(" ");
    vector<string> tmp;
    tmp.push_back(lines[i].substr(0, whiteSpacePos));
    tmp.push_back(lines[i].substr(whiteSpacePos + 1, lines[i].size()));
    instructions.push_back(tmp);
  }

  vector<vector<string>> tmp;
  tmp = instructions;
  cout << "acc: " << first(tmp) << endl;

  int secondAcc = 0;
  for(int i = 0; i < lines.size(); i++) {
    vector<vector<string>> copy = instructions;

    if (copy[i][0] == "acc") continue;
    if (copy[i][0] == "nop" && copy[i][1] == "+0") continue;

    secondAcc = second(copy, i);
    if (secondAcc != 0) break;
  }

   cout  << "acc2: " << secondAcc << endl;
}
