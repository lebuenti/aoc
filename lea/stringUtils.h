#include <string>
using namespace std;

char pop(string& str) {
  char res = str.at(0);
  str.erase(0,1);
  return res;
}

bool checkStringContainsOnlyDigits(string str, int size) {
  smatch matches;
  return (str.size() == size && regex_search(str, matches, regex("^\\d+$")));
}

int getNumberFromString(string str) {
  smatch matches;
  if (regex_search(str, matches, regex("\\d+"))) {
    return stoi(matches[0].str());
  }
  return -1;
}

bool isHexColor(string str) {
  smatch matches;
  return regex_search(str, matches, regex("^#([0-9a-f]{6}|[a-f]{6})$"));
}
