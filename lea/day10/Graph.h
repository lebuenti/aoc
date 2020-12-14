#include <vector>
#include <iostream>
#include <map>
using namespace std;

class Node {
  private:
    int value;
    vector<Node*> successors;
  public:
    Node(int value) {
      this->value = value;
    }

    Node* addSuccessor(Node* node) {
      this->successors.push_back(node);
      return this;
    }

    int getValue() const {
      return this->value;
    }

    vector<Node*> getSuccessors() {
      return this->successors;
    }

    int print() {
      cout << to_string(this->value) << " -> ";
      for(int i = 0; i < this->successors.size(); i++) {
        cout << this->successors[i]->getValue() << " -> ";
      }
      cout << endl;
      return 0;
    }

    bool operator< (const Node& node) const {
        return (node.getValue() < this->getValue());
    }

    bool isLeaf() {
      return this->successors.size() == 0;
    }

};

class Graph {
  private:
    vector<Node*> nodes;
  public:
    Graph() {}

    Graph* addNode(Node* node) {
      this->nodes.push_back(node);
      return this;
    }

    Node* findNodeByVal(int val) {
      for(int i = 0; i < this->nodes.size(); i++) {
        if (nodes[i]->getValue() == val) {
          return nodes[i];
        }
      }
      return NULL;
    }

    vector<Node*> getNodes() {
      return this->nodes;
    }

    int print() {
      for(int i = 0; i < this->nodes.size(); i++) {
        this->nodes[i]->print();
      }
      return 0;
    }

    vector<Node*> getPath(Node* from, Node* to, map<Node, bool> visited, vector<Node*> path) {
     if (visited[(*from)] == true) return path;
     
     if (visited.find((*from)) != visited.end()) {
        visited[(*from)] = true;
     } else {
        visited.insert( pair<Node, bool>((*from), true));
     }
     path.push_back(from);

     if (from == to) return path;
     
     for(int i = 0; i < from->getSuccessors().size(); i++) {
        path = getPath(from->getSuccessors()[i], to, visited, path);
        if (path[path.size() - 1] == to) return path;
     }

     path.pop_back();
     return path;
    }


    map<int, int> getJoltDifferences(Node* from, Node* to) {
      map<Node, bool> visited;
      vector<Node*> path;

      vector<Node*> nodes = this->getPath(from, to, visited, path);
      map<int, int> differences;
      for (int i = 1; i <= 3; i++) {
        differences.insert( pair<int, int> (i, 0));
      }

      for(int i = 1; i < nodes.size(); i++) {
        int tmp = nodes[i]->getValue() - nodes[i-1]->getValue();
        
        differences[tmp] = differences[tmp] + 1;
      }

      return differences;
    }


    int calculateAmountOfPaths(Node* from, Node* to, int res) {
      //cout << from->getValue() << " -> ";
      if (from == to) {
        res = res + 1;
        //cout << endl;
        return res;
      }

      for(int i = 0; i < from->getSuccessors().size(); i++) {
        res = calculateAmountOfPaths(from->getSuccessors()[i], to, res);
      }

      return res;
    }


    int getAmountOfPaths(Node* from, Node* to) {
      return calculateAmountOfPaths(from, to, 0);     
    }

};
