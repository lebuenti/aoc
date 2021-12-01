#include <iostream>
#include <fstream>
#include <string>
#include <vector> 

#include "../fileReader.h"
using namespace std;

int main() {
  vector<string> buffer  = readFile("input.txt");

  int numbers [buffer.size()];
  for(int i = 0; i < buffer.size(); i++) {
    numbers[i] = stoi( buffer[i] );
  }


  for(int i = 0; i < buffer.size(); i++) {
    for(int j = i+1; j < buffer.size(); j++) {
      if ((numbers[i] + numbers[j]) == 2020)  cout << i << " and " << j << " -> " <<  numbers[i] * numbers[j] << endl;
      for (int k = j+1; k < buffer.size(); k++) {
        if ((numbers[i] + numbers[j] + numbers[k]) == 2020) cout << i << " and " << j << " and " << k <<  " -> " << numbers[i] * numbers[j] * numbers[k] << endl;
      }
    }
  }

  return 0;
}

