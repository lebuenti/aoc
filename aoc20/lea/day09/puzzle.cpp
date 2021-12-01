#include <iostream>
#include <string>
#include <vector>
#include "../fileReader.h"
using namespace std;

bool isValid(vector<long unsigned int> numbers, int pos, int begin, int end) {
  for(int i = begin; i < end; i++) {
    for (int j = i + 1; j < end; j++) {
      if (numbers[i] + numbers[j] == numbers[pos]) {
        return true;
      }
    }
  }
  return false;
}

int findWeakness(vector<long unsigned int> numbers, int invalidPos) {
  int from = 0;
  int to = 0;

  for(int i = 0; i < invalidPos; i++) {
    int ctr = 0;
    int tmp = 0;
    from = i;
    for (int j = i; j < invalidPos; j++) {
      tmp += numbers[j];
      ctr++;
      if (ctr >= 2 && tmp == numbers[invalidPos]) {
        to = j;
        goto found;
      } else if (ctr >= 2 && tmp > numbers[invalidPos]) {
        break;
      }
    }
    if (i == invalidPos - 1 && tmp != numbers[invalidPos]) {
      cerr << "No weakness found" << endl;
      exit(4);
    }
  }

  found:
  int min = numbers[from];
  int max = numbers[from];
  for(int i = from; i <= to; i++) {
    if (numbers[i] > max) max = numbers[i];
    if (numbers[i] < min) min = numbers[i];
  }
  return max + min;

}

int main() {
  vector<string> lines = readFile("input2.txt");
  vector<long unsigned int> numbers;
  for (int i = 0; i < lines.size(); i++) {
    numbers.push_back(stol(lines[i]));
  }

  int invalidPos = 0;

  int begin = 0;
  int end = 26;
  for(int i = end; i < lines.size(); i++) {
    if (!isValid(numbers, i, begin, end )) {
      invalidPos = i;
      break;
    }
    begin++;
    end++;
  }

  int weakness = findWeakness(numbers, invalidPos);

  cout << "first invalid: " << numbers[invalidPos] << endl;
  cout << "weakness : " << weakness << endl;

  return 0;
}
