"use strict";

const readDataAsLine = require("../util");
const exampleInput = "./lea/day15/exampleInput.txt";
const input = "./lea/day15/input.txt";

class Node {
  constructor(label, x, y) {
    this.label = label;
    this.x = x;
    this.y = y;
  }

  toString() {
    return this.label + " (" + this.x + "|" + this.y + ")";
  }

  static fromG(G, x, y) {
    return new Node(G[y][x], x, y);
  }
}

const getNodeWithMinDistance = (nodes, distances) => {
  let min = Infinity;
  let node = undefined;

  nodes.forEach((n) => {
    let distance = distances[n];
    if (distance < min) {
      min = distance;
      node = n;
    }
  });
  return node;
};

class Queue {
  constructor() {
    this.values = [];
  }

  add(node, prio) {
    if (this.values.length === 0) {
      this.values.push({ node: node, distance: prio });
    } else {
      for (let i = 0; i < this.values.length; i++) {
        if (this.values[i].distance > prio) {
          this.values.splice(i, 0, { node: node, distance: prio });
          break;
        } else if (i === this.values.length - 1) {
          this.values.push({ node: node, distance: prio });
          break;
        }
      }
    }
  }

  isNotEmpty() {
    return this.values.length > 0;
  }

  pop() {
    const res = this.values.splice(0, 1);
    return res[0];
  }
}

const calculateNeighbours = (u, input) => {
  let nodes = [];
  if (input[u.node.y - 1] && input[u.node.y - 1][u.node.x]) {
    nodes.push(
      new Node(parseInt(input[u.node.y - 1][u.node.x]), u.node.x, u.node.y - 1)
    );
  }
  if (input[u.node.y] && input[u.node.y][u.node.x - 1]) {
    nodes.push(
      new Node(parseInt(input[u.node.y][u.node.x - 1]), u.node.x - 1, u.node.y)
    );
  }
  if (input[u.node.y] && input[u.node.y][u.node.x + 1]) {
    nodes.push(
      new Node(parseInt(input[u.node.y][u.node.x + 1]), u.node.x + 1, u.node.y)
    );
  }
  if (input[u.node.y + 1] && input[u.node.y + 1][u.node.x]) {
    nodes.push(
      new Node(parseInt(input[u.node.y + 1][u.node.x]), u.node.x, u.node.y + 1)
    );
  }
  return nodes;
};

const fasterDijkstra = (source, input) => {
  let previous = [];
  let distance = [];
  let Q = new Queue();

  distance[source] = 0;
  Q.add(source, 0);

  while (Q.isNotEmpty()) {
    let u = Q.pop();

    const neighbours = calculateNeighbours(u, input);
    neighbours.forEach((v) => {
      let alt = distance[u.node] + parseInt(v.label);

      const distV = distance[v] == null ? Infinity : distance[v];

      if (alt < distV) {
        distance[v] = alt;
        previous[v] = u.node;
        Q.add(v, alt);
      }
    });
  }

  return { distance: distance, previous: previous };
};

const part2 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);
  let biggerInput = [];
  for (let k = 0; k < 5; k++) {
    for (let i = 0; i < puzzleInput.length; i++) {
      let newLine = "";
      for (let j = 0; j < 5; j++) {
        let chars = puzzleInput[i].split("");
        let res = chars.map((c) => {
          const tmp = parseInt(c) + j + k;
          return (((tmp - 1) % 9) + 1).toString();
        });
        const s = res.join("");
        newLine += s;
      }
      biggerInput.push(newLine);
    }
  }

  const srcNode = new Node(biggerInput[0][0], 0, 0);
  let idk = fasterDijkstra(srcNode, biggerInput);

  let S = [];
  let u = Node.fromG(biggerInput, biggerInput[0].length-1, biggerInput.length-1);
  while (u != null) {
    S.splice(0,0,u);
    u = idk.previous[u.toString()];
  }
  const total = S.reduce((acc, curr) => acc += parseInt(curr.toString()[0]), -srcNode.label);
  console.log('total risk', total);
};

const part1 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);

  const srcNode = new Node(puzzleInput[0][0], 0, 0);
  let idk = fasterDijkstra(srcNode, puzzleInput);

  let S = [];
  let u = Node.fromG(puzzleInput, puzzleInput[0].length-1, puzzleInput.length-1);
  while (u != null) {
    S.splice(0,0,u);
    u = idk.previous[u.toString()];
  }
  const total = S.reduce((acc, curr) => acc += parseInt(curr.toString()[0]), -srcNode.label);
  console.log('total risk', total);
};

// part1();
part2();
