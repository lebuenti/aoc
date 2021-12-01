#include <iostream>
#include <string>
#include <vector>
#include "../fileReader.h"
#include "../stringUtils.h"
using namespace std;

void part1(char direction, int number, int* x, int* y, int* currentAngle) {
    if (direction == 'R' || direction == 'L') {
      if (direction == 'L') number = 360 - number;
      *currentAngle = (*currentAngle + number) % 360;
      return;
    }
     
    if ( (direction == 'F' && (*currentAngle == 360 || (*currentAngle >= 0 && *currentAngle < 90))) || direction == 'N') {
      *y += number;
    } else if ( (direction == 'F' && *currentAngle >= 90 && *currentAngle < 180) || direction == 'E') {
      *x += number;
    } else if ( (direction == 'F' && *currentAngle >= 180 && *currentAngle < 270) || direction == 'S') {
      *y -= number;
    } else if ( (direction == 'F' && *currentAngle >= 270 && *currentAngle < 360) || direction == 'W') {
      *x -= number;
    }
}


void part2(char direction, int number, int* xWayp, int* yWayp, int* xShip, int* yShip) {
  if (direction == 'N') {
    *yWayp += number;
  } else if (direction == 'S') {
    *yWayp -= number;
  } else if (direction == 'E') {
    *xWayp += number;
  } else if (direction == 'W') {
    *xWayp -= number;
  }

  if (direction == 'F') {
    *xShip += number * *xWayp;
    *yShip += number * *yWayp;
  } 

  if (direction == 'L' || direction == 'R') {
    if (direction == 'L') number = 360 - number;
    
    for (int i = 1; i <= (number/90); i++) {
      int tmp = *xWayp;
      *xWayp = *yWayp;
      *yWayp = tmp * (-1);
    }
  }
}


int main() {
  vector<string> lines = readFile("input2.txt");
 
  //part 1
  int xP1 = 0;
  int yP1 = 0;
  int currentAngleP1 = 90;

  //part 2
  int xWaypoint = 10;
  int yWaypoint = 1;
  int xShip = 0;
  int yShip = 0;
  
  for(int i = 0; i < lines.size(); i++) {
    int number = getNumberFromString(lines[i]);
    char direction = lines[i].at(0);

    part1(direction, number, &xP1, &yP1, &currentAngleP1);
    part2(direction, number, &xWaypoint, &yWaypoint, &xShip, &yShip);
  }

  if (yP1 < 0) yP1 = yP1 * (-1);
  if (xP1 < 0) xP1 = xP1 * (-1);

  if (xShip < 0) xShip *= (-1);
  if (yShip < 0) yShip *= (-1);

  cout << "Manhatten Distance part 1: " << xP1 + yP1 << endl;
  cout << "Manhatten Distance part 2: " << xShip + yShip << endl;
  return 0;
}
