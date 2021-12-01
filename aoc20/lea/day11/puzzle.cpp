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


vector<string> part1(vector<string> current, vector<string> next) {
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
     }
   }
  return next;
}


int amountVisibleOccupiedSeats(int row, int col, vector<string> current) {
  int occupiedCtr = 0;

  bool r = false, l = false;
  for(int c = 1; c < current[row].size(); c++) {
    if (!l) {
      if (col - c < 0) {
        l = true;
      } else {
        if (current[row].at(col - c) != '.') {
          if (current[row].at(col - c) == '#') occupiedCtr++;
          l = true;
        }
      }
    }
    if (!r) {
      if (col + c >= current[row].size()) {
        r = true;
      } else {
        if (current[row].at(col + c) != '.') {
          if (current[row].at(col + c) == '#') occupiedCtr++;
          r = true;
        }
      }
    }
    if (r && l) break;
  }

  bool u = false, d = false, dul = false, dur = false, ddl = false, ddr = false;
  for(int r = 1; r < current.size(); r++) {
    if (!u) {
      if (row - r < 0) {
        u = true;
      } else {
        if (current[row-r].at(col) != '.') {
          if (current[row-r].at(col) == '#') occupiedCtr++;
          u = true;
        }
      }
    }
    if (!d) {
      if (row + r >= current.size()) {
        d = true;
      } else {
        if (current[row+r].at(col) != '.') {
          if (current[row+r].at(col) == '#') occupiedCtr++;
          d = true;
        }
      }
    }
    if (!dul) {
      if (row-r < 0 || col-r < 0) {
        dul = true;
      } else { 
        if (current[row-r].at(col-r) != '.') {
          if (current[row-r].at(col-r) == '#') occupiedCtr++;
          dul = true;
        }
      }
    }
    if (!dur) {
      if (row-r < 0 || col+r >= current[row].size()) {
        dur = true;
      } else {
        if (current[row-r].at(col+r) != '.') {
          if (current[row-r].at(col+r) == '#') occupiedCtr++;
          dur = true;
        }
      }
    }
    if (!ddl) {
      if (row+r >= current.size() || col-r < 0) {
        ddl = true;
      } else {
        if (current[row+r].at(col-r) != '.') {
          if (current[row+r].at(col-r) == '#') occupiedCtr++;
          ddl = true;
        }
      }
    }
    if (!ddr) {
      if (row+r >= current.size() || col+r >= current[row].size()) {
        ddr = true;
      } else {
        if (current[row+r].at(col+r) != '.') {
          if (current[row+r].at(col+r) == '#') occupiedCtr++;
          ddr = true;
        }
      }
    }
    if (u && d && dul && dur && ddl && ddr) break;
  }

  return occupiedCtr;
}

vector<string> part2(vector<string> current, vector<string> next) {
  for(int i = 0; i < current.size(); i++) {
    for(int j = 0; j < current[i].size(); j++) {
        if (current[i].at(j) == 'L') {
          int occupiedCtr = amountVisibleOccupiedSeats(i, j, current);
          if (occupiedCtr == 0) {
            next[i].at(j) = '#';
          }
        } else if (current[i].at(j) == '#') {
          int occupiedCtr = amountVisibleOccupiedSeats(i, j, current); 
          if (occupiedCtr >= 5) { 
            next[i].at(j) = 'L';
          }
        }
     }
   }
  return next;
  
}

int main() {
  vector<string> lines = readFile("input2.txt");
  
  vector<string> current = lines;
  vector<string> next = lines;

  do {
    current = next;
    //next = part1(current, next);
    next = part2(current, next);
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
