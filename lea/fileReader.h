#include <fstream>
#include <string>
#include <vector>
using namespace std;

vector<string> readFile(string path) {
  ifstream infile(path);
  
  string line;
  vector<string> buffer;
  while (getline(infile, line)) {
    buffer.push_back(line);
  }
  infile.close();

  return buffer;
}
