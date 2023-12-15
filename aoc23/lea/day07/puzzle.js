const fs = require("fs");
const assert = require("assert");

const getAmountOfChars = (str) => {
  const charCounter = new Map();
  for (const char of str) {
    if (charCounter.has(char)) {
      let result = charCounter.get(char);
      charCounter.set(char, ++result);
    } else {
      charCounter.set(char, 1);
    }
  }
  return charCounter;
};
assert.equal(getAmountOfChars("AABBAA").size, 2);
assert.equal(getAmountOfChars("AABBAA").get("A"), 4);
assert.equal(getAmountOfChars("AABBAA").get("B"), 2);

const isFiveOfAKind = (uniqueChars, joker = false) => {
  return (
    uniqueChars.size === 1 ||
    (joker && uniqueChars.size === 2 && uniqueChars.has("J"))
  );
};
assert.equal(isFiveOfAKind(getAmountOfChars("AAAAJ"), true), true);
assert.equal(isFiveOfAKind(getAmountOfChars("AJJJJ"), true), true);
assert.equal(isFiveOfAKind(getAmountOfChars("AAAAQ"), true), false);
assert.equal(isFiveOfAKind(getAmountOfChars("AAAAA"), true), true);

const isFourOfAKind = (uniqueChars, joker = false) => {
  return (
    (uniqueChars.size === 2 &&
      !![...uniqueChars.values()].find((entry) => entry === 4)) ||
    (joker &&
      uniqueChars.size === 3 &&
      uniqueChars.has("J") &&
      !(
        [...uniqueChars.entries()].filter(
          ([key, value]) => value === 2 && key !== "J"
        ).length === 2
      ))
  );
};
assert.equal(isFourOfAKind(getAmountOfChars("AA8AA"), true), true);
assert.equal(isFourOfAKind(getAmountOfChars("AA8JA"), true), true);
assert.equal(isFourOfAKind(getAmountOfChars("AA8QA"), true), false);
assert.equal(isFourOfAKind(getAmountOfChars("AJ8JJ"), true), true);
assert.equal(isFourOfAKind(getAmountOfChars("7QQJ7"), true), false);
assert.equal(isFourOfAKind(getAmountOfChars("7QJJJ"), true), true);
assert.equal(isFourOfAKind(getAmountOfChars("7QJJ7"), true), true);

const isFullHouse = (uniqueChars, joker = false) => {
  return (
    (uniqueChars.size === 2 &&
      !![...uniqueChars.values()].find((entry) => entry === 3)) ||
    (joker && uniqueChars.size === 3 && uniqueChars.has("J"))
  );
};
assert.equal(isFullHouse(getAmountOfChars("23332"), true), true);
assert.equal(isFullHouse(getAmountOfChars("233J2"), true), true);
assert.equal(isFullHouse(getAmountOfChars("23JJ2"), true), true);
assert.equal(isFullHouse(getAmountOfChars("7QQJ7"), true), true);

const isThreeOfAKind = (uniqueChars, joker = false) => {
  return (
    (uniqueChars.size === 3 &&
      !![...uniqueChars.values()].find((entry) => entry === 3)) ||
    (joker && uniqueChars.size === 4 && uniqueChars.has("J"))
  );
};
assert.equal(isThreeOfAKind(getAmountOfChars("TTT98"), true), true);
assert.equal(isThreeOfAKind(getAmountOfChars("TTJ98"), true), true);
assert.equal(isThreeOfAKind(getAmountOfChars("TJJ98"), true), true);

const isTwoPair = (uniqueChars, joker = false) => {
  return (
    uniqueChars.size === 3 &&
    !![...uniqueChars.values()].find((entry) => entry === 2)
  );
};
assert.equal(isTwoPair(getAmountOfChars("22334"), true), true);
assert.equal(isTwoPair(getAmountOfChars("A23J4"), true), false);

const isOnePair = (uniqueChars, joker = false) => {
  return (
    uniqueChars.size === 4 ||
    (joker && uniqueChars.size === 5 && uniqueChars.has("J"))
  );
};
assert.equal(isOnePair(getAmountOfChars("A23A4"), true), true);
assert.equal(isOnePair(getAmountOfChars("A23J4"), true), true);

const calculate = (allHands, sortOrder) => {
  allHands.forEach((hand) =>
    hand.sort((a, b) => {
      for (let i = 0; i < Math.min(a.hand.length, b.hand.length); i++) {
        const indexA = sortOrder.indexOf(a.hand[i]);
        const indexB = sortOrder.indexOf(b.hand[i]);

        if (indexA !== indexB) {
          return indexB - indexA;
        }
      }
      return b.hand.length - a.hand.length;
    })
  );

  let counter = 1;
  let result = 0;
  allHands.forEach((hands) => {
    hands.forEach((card) => {
      result += card.bid * counter;
      counter++;
    });
  });
  return result;
};

const file = fs.readFileSync("./input.txt", "utf-8");

const part1 = () => {
  const fiveOfAKind = [];
  const fourOfAKind = [];
  const fullHouse = [];
  const threeOfAKind = [];
  const twoPair = [];
  const onePair = [];
  const highCard = [];
  const allHands = [
    highCard,
    onePair,
    twoPair,
    threeOfAKind,
    fullHouse,
    fourOfAKind,
    fiveOfAKind,
  ];

  file.split(/\r?\n/).forEach((line) => {
    const bid = parseInt(line.split(" ")[1].trim(), 10);
    const hand = line.split(" ")[0];

    const uniqueChars = getAmountOfChars(hand);

    if (isFiveOfAKind(uniqueChars)) {
      fiveOfAKind.push({ hand: hand, bid: bid });
    } else if (isFourOfAKind(uniqueChars)) {
      fourOfAKind.push({ hand: hand, bid: bid });
    } else if (isFullHouse(uniqueChars)) {
      fullHouse.push({ hand: hand, bid: bid });
    } else if (isThreeOfAKind(uniqueChars)) {
      threeOfAKind.push({ hand: hand, bid: bid });
    } else if (isTwoPair(uniqueChars)) {
      twoPair.push({ hand: hand, bid: bid });
    } else if (isOnePair(uniqueChars)) {
      onePair.push({ hand: hand, bid: bid });
    } else {
      highCard.push({ hand: hand, bid: bid });
    }
  });

  const sortOrder = "AKQJT98765432";
  return calculate(allHands, sortOrder);
};

const part2 = () => {
  const fiveOfAKind = [];
  const fourOfAKind = [];
  const fullHouse = [];
  const threeOfAKind = [];
  const twoPair = [];
  const onePair = [];
  const highCard = [];
  const allHands = [
    highCard,
    onePair,
    twoPair,
    threeOfAKind,
    fullHouse,
    fourOfAKind,
    fiveOfAKind,
  ];

  file.split(/\r?\n/).forEach((line) => {
    const bid = parseInt(line.split(" ")[1].trim(), 10);
    const hand = line.split(" ")[0];

    const uniqueChars = getAmountOfChars(hand);

    if (isFiveOfAKind(uniqueChars, true)) {
      fiveOfAKind.push({ hand: hand, bid: bid });
    } else if (isFourOfAKind(uniqueChars, true)) {
      fourOfAKind.push({ hand: hand, bid: bid });
    } else if (isFullHouse(uniqueChars, true)) {
      fullHouse.push({ hand: hand, bid: bid });
    } else if (isThreeOfAKind(uniqueChars, true)) {
      threeOfAKind.push({ hand: hand, bid: bid });
    } else if (isTwoPair(uniqueChars, true)) {
      twoPair.push({ hand: hand, bid: bid });
    } else if (isOnePair(uniqueChars, true)) {
      onePair.push({ hand: hand, bid: bid });
    } else {
      highCard.push({ hand: hand, bid: bid });
    }
  });

  const sortOrder = "AKQT98765432J";
  return calculate(allHands, sortOrder);
};

console.log(part1());
console.log(part2());
