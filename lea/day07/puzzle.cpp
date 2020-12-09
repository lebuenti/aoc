#include <iostream>
#include <string>
#include <map>
#include <vector>
#include "../fileReader.h"
#include "../stringUtils.h"
#include "Bag.h"
using namespace std;

string getOuterBag(string line) {
  int outerBagPos = line.find("bags");
  string outerBag = line.substr(0, outerBagPos - 1);
  return outerBag;
}

map<string, int> getInnerBags(string line) {
  string tmp = line;
  map<string, int> bags;

  int posContain = tmp.find("contain");
  tmp.erase(0, posContain + 8);

  while (tmp.find("bag") != string::npos) {
    int number = getNumberFromString(tmp);
    if (number >= 0) {
      int numberPos = tmp.find(to_string(number));
      tmp.erase(0, numberPos + (to_string(number).size()) + 1);
    }

    int nextBagPos = tmp.find("bag");
    string nextBag = tmp.substr(0, nextBagPos - 1);

    tmp.erase(0, nextBagPos + 4);
    if (number > 1) tmp.erase(0, 1);

    if (nextBag.find("no other") == string::npos) {
       bags.insert( pair<string, int>(nextBag, number));
    }
  }
  return bags;
}

bool searchInnerBags(vector<Bag> bags, map<string, int> current, string searched) {
   vector<Bag> childrenBag;
   for (auto const& c : current) {
      for(int i = 0; i < bags.size(); i++) {
        if (bags[i].getColor() == c.first && bags[i].canContain(searched)) {
          return true;
        } else if (bags[i].getColor() == c.first) {
          childrenBag.push_back(bags[i]);
        }  
      }
   }

   //search with children from childrenBag
   for (int i  = 0;  i < childrenBag.size(); i++) {
      if (childrenBag[i].getInnerBags().size() > 0) {
        if (searchInnerBags(bags, childrenBag[i].getInnerBags(), searched)) {
          return true;
        }
      }
   }

   //last children has no child
   return false;
}

int countShinyGoldBags(vector<Bag> bags, map<string, int> current) {
   if (current.size() == 0) return 1;

   map<Bag*, int> childrenBag;
   for (auto const& c : current) {
     for(int i = 0; i < bags.size(); i++) {
        if (bags[i].getColor() == c.first) {
          childrenBag.insert(pair<Bag*, int>(&bags[i], c.second));
        }  
      }
   }
   
   map<Bag*, int>::iterator it;
   int res = 0;
    for (it = childrenBag.begin(); it != childrenBag.end(); it++) {
      int t = countShinyGoldBags(bags, (it->first)->getInnerBags());
      if (t > 1) res += it->second + it->second * t;
      else res += it->second * t;
    }
    
    return res;
}

int main() {
  vector<string> lines = readFile("input2.txt");
  vector<Bag> bags;

  for(int i = 0; i < lines.size(); i++) {
    string outerBag = getOuterBag(lines[i]);
    map<string, int> innerBags = getInnerBags(lines[i]);
    Bag bag = Bag(outerBag, innerBags);
    bags.push_back(bag);
  }

  int shinyGoldCtr = 0;
  int amountBags = 0;
  
  for(int i = 0; i < bags.size(); i++) {
    if (bags[i].getColor() == "shiny gold") {
      amountBags = countShinyGoldBags(bags, bags[i].getInnerBags());
      continue;
    }

    if (bags[i].canContain("shiny gold")) {
      shinyGoldCtr++;
    } else {
      map<string, int> innerBags = bags[i].getInnerBags();
      if (searchInnerBags(bags, innerBags, "shiny gold")) shinyGoldCtr++;
    }
  }
  cout << "Amount: " << amountBags << endl;
  cout << "Ctr: " << shinyGoldCtr << endl;
  return 0;
}
