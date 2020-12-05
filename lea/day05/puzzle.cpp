#include <iostream>
#include "../fileReader.h"
#include "../stringUtils.h"
#include <vector>
#include <cmath>
#include <string>
using namespace std;

int binarySearch(string next, double l, double r) {
    //cout << "l: " << l << " r: " << r << " next: ";

    double m = floor( (r+l) / 2 );
    if (next.empty()) return m;

    char nxt = pop(next);
    //cout << nxt << " m: " << m << endl;
    
    if (nxt == 'F' || nxt == 'L') {
      return binarySearch(next, l, m);

    } else if (nxt == 'B' || nxt == 'R') {
      return binarySearch(next, m + 1, r);

    } else {
      cerr << "wrong char: " << nxt << endl;
      exit(4);
    }
}

bool isMoreThanOneEmpty(int row[], int n) {
  int counter = 0;
  for(int i = 0; i < n ; i++) {
    if (row[i] == 0) counter++;
  }
  return counter > 1;
}

int main() {
  vector<string> lines = readFile("input.txt");
  int biggest = 0;
  int flight[128][8] = {{0}};

  for(int i = 0; i < lines.size(); i++) {
    string decodedRow = lines[i].substr(0, lines[i].size()-3);
    int row = binarySearch(decodedRow, 0.0, 127.0);
    
    string decodedSeat = lines[i].substr(lines[i].size()-3, lines[i].size());
    int seat = binarySearch(decodedSeat, 0.0, 7.0);
    
    flight[row][seat] = 1;
    if ((row * 8 + seat) > biggest) biggest = row * 8 + seat;
  }

  cout << "biggest seat id: " << biggest << endl;

  for (int i = 1; i < 127; i++) {
    if (isMoreThanOneEmpty(flight[i], 8)) continue;
    
    for (int j = 0; j < 8; j++) {
      if (flight[i][j] == 0) {
        cout << "your seat id: " << i * 8 + j << endl;
      }  
    }
  }

  return 0;
}
