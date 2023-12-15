const fs = require("fs");
const assert = require("assert");

const readSeedsAndMaps = (maps, filepath) => {
  const seeds = [];

  let currentMap = undefined;

  const file = fs.readFileSync(filepath, "utf-8");
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
  return { seeds: seeds, maps: maps };
};

const part1 = () => {
  const initMaps = new Map([
    ["seed-to-soil", []],
    ["soil-to-fertilizer", []],
    ["fertilizer-to-water", []],
    ["water-to-light", []],
    ["light-to-temperature", []],
    ["temperature-to-humidity", []],
    ["humidity-to-location", []],
  ]);
  const result = readSeedsAndMaps(initMaps, "./input.txt");

  const locations = result.seeds.reduce((acc, seed) => {
    let currentSeed = seed;
    for (const [key, value] of result.maps) {
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

const isSeed = (seeds, current) => {
  for (let i = 0; i < seeds.length; i += 2) {
    if (current >= seeds[i] && seeds[i] + seeds[i + 1] > current) {
      return true;
    }
  }
  return false;
};

assert.equal(isSeed([79, 14, 55, 13], 79), true);
assert.equal(isSeed([79, 14, 55, 13], 79 + 14), false);
assert.equal(isSeed([79, 14, 55, 13], 79 + 13), true);
assert.equal(isSeed([79, 14, 55, 13], 15), false);
assert.equal(isSeed([79, 14, 55, 13], 55), true);
assert.equal(isSeed([79, 14, 55, 13], 55 + 12), true);
assert.equal(isSeed([79, 14, 55, 13], 55 + 13), false);
assert.equal(isSeed([79, 14, 55, 13], 0), false);

const part2 = () => {
  const initMaps = new Map([
    ["humidity-to-location", []],
    ["temperature-to-humidity", []],
    ["light-to-temperature", []],
    ["water-to-light", []],
    ["fertilizer-to-water", []],
    ["soil-to-fertilizer", []],
    ["seed-to-soil", []],
  ]);
  const result = readSeedsAndMaps(initMaps, "./input.txt");

  for (let i = 0; i < Infinity; i++) {
    let current = i;

    for (const [key, value] of result.maps) {
      const fun = value.find((val) => {
        return (
          current < val.value + (val.end - val.begin) && //max
          current >= val.value //min
        );
      });

      current = fun ? current - fun.value + fun.begin : current;

      if (key === "seed-to-soil" && isSeed(result.seeds, current)) {
        return i;
      }
    }
  }
};

console.log(part1());
console.log(part2());
