#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
  ifstream infile("input.txt");

  string line;
  int amountLines = 0;
  while (getline(infile, line)) {
    amountLines++;
  }
  infile.close();
  
  infile.open("input.txt");
  int numbers [amountLines];
  int i = 0;
  while( getline(infile, line) ) {
    numbers[i] = stoi( line );
    i++;
  }
  infile.close();

  for(int i = 0; i < amountLines; i++) {
    for(int j = 0; j < amountLines; j++) {
      if (i == j) continue;
      if (numbers[i]+numbers[j] == 2020)  cout << "two number" <<  numbers[i]*numbers[j] << endl;
      for (int k = 0; k < amountLines; k++) {
        if (j == k) continue;
        if (numbers[i] + numbers[j] + numbers[k] == 2020) cout << "three numbers" << numbers[i] * numbers[j] * numbers[k] << endl;
      }
      
    }

  }

  return 0;
}
