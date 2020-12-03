#include <iostream>
#include <vector>
#include <string>
#include "../fileReader.h"
using namespace std;

int checkSlopes(int right, int down, vector<string> lines) {
  int treeCounter = 0; 
  int current = right;
  
  for(int i = down; i < lines.size(); i += down) {
    while ((current + right)  > lines[i].size())  lines[i] = lines[i] + lines[i];

    if (lines[i][current] == '#') treeCounter++;
    current += right;
  }
  return treeCounter;
}


int main() {
  vector<string> lines = readFile("input.txt");
  int first = checkSlopes(1, 1, lines);
  int second = checkSlopes(3, 1, lines);
  int third = checkSlopes(5, 1, lines);
  int fourth = checkSlopes(7, 1, lines);
  int fifth = checkSlopes(1, 2, lines);

  cout << first * second * third * fourth * fifth << endl;
  return 0;
}
