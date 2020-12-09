#include <iostream>
#include <string>
#include <map>
using namespace std;

class Bag {
  private:
    string color;
    map<string, int> innerBags;
  public:
    Bag(string color, map<string, int> innerBags) {
      this->color = color;
      this->innerBags = innerBags;
    }

    string getColor() {
      return this->color;
    }

    map<string, int> getInnerBags() const {
      return this->innerBags;
    }

    bool canContain(string color) {
      return (this->innerBags.count(color) > 0);
    }

    void print() {
      cout << this->color << endl;
      for (auto const& b : this->innerBags) {
        cout << " --" << b.second << "--" << b.first << endl ;
      }
    }
};
