#include <string>
using namespace std;

char pop(string& str) {
  char res = str.at(0);
  str.erase(0,1);
  return res;
}
