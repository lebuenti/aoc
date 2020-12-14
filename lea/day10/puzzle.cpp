#include <iostream>
#include <string>
#include <vector>
#include "../fileReader.h"
#include "Graph.h"
#include <map>
using namespace std;

int main() {
  vector<string> lines = readFile("input3.txt");
  vector<int> numbers = {0};

  //create graph
  Graph g = Graph();
  Node* first = new Node(0);
  g.addNode(first);
  for(int i = 0; i < lines.size(); i++) {
    numbers.push_back(stoi(lines[i]));
    Node* n = new Node(stoi(lines[i]));
    g.addNode(n);
  }
  std::sort(numbers.begin(), numbers.end());
  numbers.push_back(numbers[numbers.size() - 1] + 3);
  Node* last = new Node(numbers[numbers.size() - 1]);
  g.addNode(last);

  //add successors
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

  long int numbersOfPaths = g.getAmountOfPaths(from, to);

  cout << "number of jolts: " << differences[1] * differences[3] << endl;
  cout << "amount paths : " << numbersOfPaths << endl;
  return 0;
}
