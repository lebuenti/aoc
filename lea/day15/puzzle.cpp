#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int part1(vector<int> input) {
  map<int, vector<int>> times;
  for(int i = 1; i <= input.size(); i++) {
    vector<int> tmp{i, -1};
    times.insert(pair<int, vector<int>>(input[i-1], tmp)); 
  }

  int curr = input[input.size() - 1];
  
  for(int i = input.size() + 1; i <= 2020; i++) {
    if (times[curr][1] == -1) {
      curr = 0;
    } else {
      curr = times[curr][0] - times[curr][1];
    }

    if (times.find(curr) != times.end()) {
      times[curr][1] = times[curr][0];
      times[curr][0] = i;
    } else {
      vector<int> tmp{i, -1};
      times.insert(pair<int, vector<int>>(curr, tmp)); 
    }
  }

  return curr;
}


int main() {

  vector<int> input{0,3,6};
  vector<int> input1{1,3,2};
  vector<int> input2{2, 1, 3};
  vector<int> input3{1,2,3};
  vector<int> input4{2,3,1};
  vector<int> input5{3,2,1};
  vector<int> input6{3,1,2};
  vector<int> inputPuzzle{18,8,0,5,4,1,20};
  cout << "part1" << endl;
  cout << "0,3,6: " << part1(input) << ", correct:" << "436" << endl;
  cout << "1,3,2: " << part1(input1) << ", correct:" << "1" << endl;
  cout << "2,1,3: " << part1(input2) << ", correct:" << "10" << endl;
  cout << "1,2,3: " << part1(input3) << ", correct:" << "27" << endl;
  cout << "2,3,1: " << part1(input4) << ", correct:" << "78" << endl;
  cout << "3,2,1: " << part1(input5) << ", correct:" << "438" << endl;
  cout << "3,1,2: " << part1(input6) << ", correct:" << "1836" << endl;
  cout << "18,8,0,5,4,1,20: " << part1(inputPuzzle) << ", correct:" << "253" << endl;

  cout << endl;
  cout << "part2" << endl;
  return 0;

}
