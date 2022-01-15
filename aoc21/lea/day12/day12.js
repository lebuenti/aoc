const readDataAsLine = require("../util");
const exampleInput = "./lea/day12/exampleInput.txt";
const input = "./lea/day12/input.txt";

const backtracing = (node, visitedNodes, adjacencyList, allpaths) => {
  const currentVisited = [...visitedNodes, node];

  if (node === "end") {
    return [currentVisited];
  }

  const next = adjacencyList.get(node);

  for (let n of next) {
    if (n === n.toUpperCase() || !currentVisited.includes(n)) {
      let arr = backtracing(n, currentVisited, adjacencyList, allpaths);
      if (arr !== undefined) {
        allpaths.push(arr);
      }
    }
  }
};

const backtracing2 = (node, visitedNodes, adjacencyList, allpaths) => {
  const currentVisited = [...visitedNodes, node];

  if (node === "end") {
    return [currentVisited];
  }

  const next = adjacencyList.get(node);

  for (let n of next) {
      
    let go = false;
    if (n === n.toLowerCase() && n !== "start" && n !== "end") {
      go = !currentVisited
        .filter((obj) => obj === obj.toLowerCase())
        .some( (obj) => currentVisited.indexOf(obj) !== currentVisited.lastIndexOf(obj));
    }

    if (n === n.toUpperCase() || !currentVisited.includes(n) || go) {
      let arr = backtracing2(n, currentVisited, adjacencyList, allpaths);
      if (arr !== undefined) {
        allpaths.push(arr);
      }
    }
  }
};

const part1 = (adjacencyList) => {
  console.log("Part 1");
  let allpaths = [];
  backtracing("start", [], adjacencyList, allpaths);
  console.log(allpaths.length);
};

const part2 = () => {
  console.log("Part 2");
  let allpaths = [];
  backtracing2("start", [], adjacencyList, allpaths);
  console.log(allpaths.length);
};

///////////////////////////////////////////////////////////////
const puzzleInput = readDataAsLine.readDataAsLine(input);

let adjacencyList = new Map();

puzzleInput.forEach((pi) => {
  let path = pi.split("-");
  const source = path[0];
  const target = path[1];

  if (adjacencyList.has(source)) {
    let targetList = adjacencyList.get(source);
    targetList.push(target);
  } else {
    adjacencyList.set(source, [target]);
  }

  if (adjacencyList.has(target)) {
    let targetList = adjacencyList.get(target);
    targetList.push(source);
  } else {
    adjacencyList.set(target, [source]);
  }
});

part1(adjacencyList);
part2(adjacencyList);
