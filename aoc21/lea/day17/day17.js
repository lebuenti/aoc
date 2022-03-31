"use strict";

const reader = require("../util");
const exampleInput = "./lea/day17/exampleInput.txt";
const input = "./lea/day17/input.txt";

const part1And2 = () => {
  const i = reader.readDataAsString(input);

  const x = i.split("x=")[1].split("y=")[0];
  const y = i.split("y=")[1];
  const minX = parseInt(x.split("..")[0]);
  const maxX = parseInt(x.split("..")[1]);
  const minY = parseInt(y.split("..")[1]);
  const maxY = parseInt(y.split("..")[0]);

  let highest = 0;
  let counter = 0;

  for (let x = 1; x !== Math.max(Math.abs(minX), Math.abs(maxX)) + 1; x++) {
    for (let y = maxY; y !== Math.max(Math.abs(minY), Math.abs(maxY)); y++) {
      let tmpHighest = highest;
      let velocity = { x: x, y: y };
      let pos = { x: 0, y: 0 };

      while (true) {
        pos.x += velocity.x;
        pos.y += velocity.y;

        if (pos.y > tmpHighest) {
          tmpHighest = pos.y;
        }

        if (pos.x >= minX && pos.x <= maxX && pos.y >= maxY && pos.y <= minY) {
          counter++;
          if (tmpHighest > highest) {
            highest = tmpHighest;
          }
          break;
        } else if (pos.y < maxY) {
          break;
        }

        velocity.y--;

        if (velocity.x > 0) {
          velocity.x--;
        } else if (velocity.x < 0) {
          velocity.x++;
        }
      }
    }
  }

  console.log("highest pos", highest);
  console.log("counter", counter);
};

part1And2();
