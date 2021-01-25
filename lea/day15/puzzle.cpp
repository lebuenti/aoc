#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

long long int calculate(vector<int> input) {
  map<long long int, vector<long long int>> times;
  for(int i = 1; i <= input.size(); i++) {
    vector<long long int> tmp{i, -1};
    times.insert(pair<long long int, vector<long long int>>(input[i-1], tmp)); 
  }

  long long int curr = input[input.size() - 1];
  
  for(int i = input.size() + 1; i <= 30000000; i++) {
    if (times[curr][1] == -1) {
      curr = 0;
    } else {
      curr = times[curr][0] - times[curr][1];
    }

    if (times.find(curr) != times.end()) {
      times[curr][1] = times[curr][0];
      times[curr][0] = i;
    } else {
      vector<long long int> tmp{i, -1};
      times.insert(pair<long long int, vector<long long int>>(curr, tmp)); 
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
 // cout << "0,3,6: " << calculate(input) << endl;
  //cout << "1,3,2: " << calculate(input1) << endl;
  //cout << "2,1,3: " << calculate(input2) << endl;
  //cout << "1,2,3: " << calculate(input3) << endl;
  //cout << "2,3,1: " << calculate(input4) << endl;
  //cout << "3,2,1: " << calculate(input5) << endl;
  //cout << "3,1,2: " << calculate(input6) << endl;
  cout << "18,8,0,5,4,1,20: " << calculate(inputPuzzle) << endl;

  return 0;

}
