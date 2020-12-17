#include <iostream>
#include <string>
#include <vector>
#include "../fileReader.h"
using namespace std;

int max(int x, int y) {
  if (x > y) return x;
  if (x < y) return y;
  return x;
}

int min(int x, int y) {
  if (x > y) return y;
  if (x < y) return x;
  return x;
}


bool hasSameEntries(vector<string> first, vector<string> second) {
  if (first.size() != second.size()) return false;
  for(int i = 0; i < first.size(); i++) {
    if (first[i] != second[i]) return false;
  }
  return true;
}

int amountOccupiedSeats(int row, int col, vector<string> current) {
  int occupiedCtr = 0;  
  for(int l = max(0, row - 1); l < min(current.size(), row + 2); l++) {
    for(int k = max(0,col - 1); k < min(current[row].size(), col + 2); k++) {  
      if (l == row && k == col) continue;
      if (current[l].at(k) == '#'){
        occupiedCtr++;
      }
    }
  }
  return occupiedCtr;
}

int main() {
  vector<string> lines = readFile("input2.txt");
  
  vector<string> current = lines;
  vector<string> next = lines;


 
  do {
    current = next;

    for(int i = 0; i < current.size(); i++) {
      for(int j = 0; j < current[i].size(); j++) {
        
        if (current[i].at(j) == 'L') {
          int occupiedCtr = amountOccupiedSeats(i, j, current);
          if (occupiedCtr == 0) {
            next[i].at(j) = '#';
          }
        } else if (current[i].at(j) == '#') {
          int occupiedCtr = amountOccupiedSeats(i, j, current); 
          if (occupiedCtr >= 4) { 
            next[i].at(j) = 'L';
          }
        }
        //cout << next[i].at(j);
      }
      //cout << endl;
    }
    //cout << endl;

  } while (!hasSameEntries(current, next));

  int ctr = 0;
  for (int i = 0; i < current.size(); i++) {
    for (int j = 0; j < current[i].size(); j++) {
      if (current[i].at(j) == '#') ctr++;
    }
  }

  cout << "occupied seats: " << ctr << endl;
  return 0;
}
