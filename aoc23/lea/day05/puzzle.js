const fs = require("fs");

const part1 = () => {
  const seeds = [];
  const maps = new Map([
    ["seed-to-soil", []],
    ["soil-to-fertilizer", []],
    ["fertilizer-to-water", []],
    ["water-to-light", []],
    ["light-to-temperature", []],
    ["temperature-to-humidity", []],
    ["humidity-to-location", []],
  ]);

  let currentMap = undefined;

  const file = fs.readFileSync("./input.txt", "utf-8");
  for (line of file.split(/\r?\n/)) {
    if (line.includes("seeds")) {
      const s = line.split("seeds:")[1].trim().split(" ");
      seeds.push(...s.map((seed) => parseInt(seed, 10)));
      continue;
    }

    if (line.includes("map")) {
      for (const [key] of maps.entries()) {
        if (line.includes(key)) {
          currentMap = key;
          break;
        }
      }
      continue;
    }

    if (line.match(/[0-9 ]+/)) {
      let numbers = line.trim().split(" ");
      numbers = numbers.map((number) => parseInt(number, 10));
      const result = maps.get(currentMap);
      result.push({
        begin: numbers[1],
        end: numbers[1] + numbers[2] - 1,
        value: numbers[0],
      });
    }
  }

  const locations = seeds.reduce((acc, seed) => {
    let currentSeed = seed;
    for (const [key, value] of maps) {
      const fun = value.find(
        (val) => val.begin <= currentSeed && val.end >= currentSeed
      );
      currentSeed = fun ? fun.value + (currentSeed - fun.begin) : currentSeed;
      if (key === "humidity-to-location") {
        acc.push(currentSeed);
      }
    }
    return acc;
  }, []);

  return locations.reduce((acc, lowest) => {
    return acc > lowest ? (acc = lowest) : acc;
  }, locations[0]);
};

console.log(part1());
