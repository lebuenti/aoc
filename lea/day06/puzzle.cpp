#include <iostream>
#include <string>
#include <vector>
#include "../fileReader.h"
using namespace std;

int countQuestions(int questions[]) {
  int yesCounter = 0;
  for (int k = 0; k < 26; k++) {
    if (questions[k] != 0) yesCounter++;
   }
   return yesCounter;
}

int countSameYesses(int questions[], int amountGroupMembers) {
  int yesCounter = 0;
  for (int k = 0; k < 26; k++) {
    if (questions[k] == amountGroupMembers) {
      yesCounter++;
    }
  }
  return yesCounter;
}

int updateQuestions(int questions[]) {
  for(int k = 0; k < 26; k++) {
    questions[k] = 0;
  }
  return 0;
}


int main() {
  vector<string> lines = readFile("input.txt");

  int yesCounter = 0;
  int questions[26] = {0};
  int groupCounter = 0;
  int allYesses = 0;

  for(int i = 0; i < lines.size(); i++) {

    if (lines[i].empty()) {
      yesCounter += countQuestions(questions);
      allYesses += countSameYesses(questions, groupCounter);
      groupCounter = 0;
      updateQuestions(questions);
    } else {
      groupCounter++;
      for (int j = 0; j < lines[i].length(); j++) { 
         int pos = (lines[i].at(j) - '0') - 49;
         questions[pos]++;
       }
    }
  }


  cout << "part 1: " << yesCounter << endl;
  cout << "part 2: " << allYesses << endl;

  return 0;
}
