#include <iostream>
#include <string>
#include <vector>
#include "../fileReader.h"
#include "Graph.h"
#include <map>
using namespace std;

int main() {
  vector<string> lines = readFile("input3.txt");
  vector<int> numbers;

  Graph g = Graph();
  for(int i = 0; i < lines.size(); i++) {
    numbers.push_back(stoi(lines[i]));
    Node* n = new Node(stoi(lines[i]));
    g.addNode(n);
  }
  
  std::sort(numbers.begin(), numbers.end());
  
  for (int i = 0; i < numbers.size(); i++) {
    Node* n = g.findNodeByVal(numbers[i]);
    
    for(int j = i + 1; j < numbers.size(); j++) {
      if (numbers[j] <= (n->getValue() + 3)) {
        Node* s = g.findNodeByVal(numbers[j]);
        n->addSuccessor(s);
      } else {
        break;
      }
    }
  }
  
  Node* from = g.findNodeByVal(numbers[0]);
  Node* to = g.findNodeByVal(numbers[numbers.size() - 1]);
  map<int, int> differences = g.getJoltDifferences(from, to);
  differences[1]++;
  differences[3]++;

  cout << "1: " << differences[1] << ", 2:" << differences[2] << ", 3: " << differences[3] << endl;
  cout << "multiply: " << differences[1] * differences[3] << endl;
  return 0;
}
