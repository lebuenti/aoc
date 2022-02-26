"use strict";

const { versions } = require("process");
const reader = require("../util");
const exampleInput = "./lea/day16/exampleInput.txt";
const input = "./lea/day16/input.txt";

const hex2bin = (hex) => {
  hex = hex.toLowerCase();
  var out = "";
  for (let i = 0; i < hex.length; i++) {
    let c = hex[i];
    switch (c) {
      case "0":
        out += "0000"; break;
      case "1":
        out += "0001"; break;
      case "2":
        out += "0010"; break;
      case "3":
        out += "0011"; break;
      case "4":
        out += "0100"; break;
      case "5":
        out += "0101"; break;
      case "6":
        out += "0110"; break;
      case "7":
        out += "0111"; break;
      case "8":
        out += "1000"; break;
      case "9":
        out += "1001"; break;
      case "a":
        out += "1010"; break;
      case "b":
        out += "1011"; break;
      case "c":
        out += "1100"; break;
      case "d":
        out += "1101"; break;
      case "e":
        out += "1110"; break;
      case "f":
        out += "1111"; break;
      default:
        return "";
    }
  }

  return out;
};
const bin2dec = (bin) => parseInt(bin, 2);

const isLiteral = (number) => number === 4;

const literal = (string) => {
  let literalNumber = "";
  let next = false;
  for (let i = 0; i <= string.length - 5; i += 5) {
    if (parseInt(string[i]) === 1) {
      next = true;
    }
    literalNumber +=
      string[i + 1] + string[i + 2] + string[i + 3] + string[i + 4];

    if (next === false) {
      console.log("literal", literalNumber, bin2dec(literalNumber));
      const r = string.substring(i + 4 + 1);
      return {
        result: bin2dec(literalNumber),
        remaining: r,
        bits: 6 + i + 4 + 1,
      };
    }
    next = false;
  }
};

const calculate = (id, values) => {
  if (id === 0) {
    let sum = 0;
    for (let val of values) {
      sum += val;
    }
    return sum;
  } else if (id === 1) {
    let product = 1;
    for (let val of values) {
      product *= val;
    }
    return product;
  } else if (id === 2) {
    return Math.min(...values);
  } else if (id === 3) {
    return Math.max(...values);
  } else if (id === 5) {
    return values[0] > values[1] ? 1 : 0;
  } else if (id === 6) {
    return values[0] < values[1] ? 1 : 0;
  } else if (id === 7) {
    return values[0] === values[1] ? 1 : 0;
  }
};

const subPackets = (
  string,
  numberSubPackets = undefined,
  numberBits = undefined
) => {
  const resultsSubPcks = [];

  while ( (numberSubPackets && numberSubPackets > 0) || (numberBits && numberBits > 0)) {
    if (string.match(/^0+$/)) {
      string.log("----------------------");
      return;
    }

    const res = parsePacket(string);
    resultsSubPcks.push(res);

    string = res.remaining;

    if (numberSubPackets) {
      numberSubPackets--;
    } else {
      numberBits -= res.bits;
    }
  }

  return resultsSubPcks;
};

const literalPackage = (string) => {
  return literal(string.substring(6));
};

const operatorPackage = (current, id) => {
  const lengthId = current.charAt(6);

  let resSubPacks = undefined;
  let bits = 7;

  if (parseInt(lengthId) === 1) {
    const subPacksTmp = bin2dec(parseInt(current.substring(7, 7 + 11)));
    const next = current.substring(7 + 11);
    bits += 11;
    resSubPacks = subPackets(next, subPacksTmp);
  } else {
    const subBitsTmp = bin2dec(parseInt(current.substring(7, 7 + 15)));
    const next = current.substring(7 + 15);
    bits += 15;
    resSubPacks = subPackets(next, undefined, subBitsTmp);
  }

  const val = calculate(
    id,
    resSubPacks.map((o) => o.val)
  );

  let versionSum = 0;
  for (let subPack of resSubPacks) {
    versionSum += subPack.version;
  }

  resSubPacks.forEach((o) => {
    bits += o.bits;
  });

  return {
    val: val,
    bits: bits,
    remaining: resSubPacks[resSubPacks.length - 1].remaining,
    version: versionSum,
  };
};

const parsePacket = (string) => {
  console.log(string);

  const id = bin2dec(
    parseInt(string.charAt(3) + string.charAt(4) + string.charAt(5))
  );

  const version = bin2dec(
    parseInt(string.charAt(0) + string.charAt(1) + string.charAt(2))
  );

  if (isLiteral(id)) {
    const res = literalPackage(string);
    return {
      val: res.result,
      remaining: res.remaining,
      bits: res.bits,
      version: version,
    };
  } else {
    const res = operatorPackage(string, id);
    let t = version + res.version;
    return {
      val: res.val,
      remaining: res.remaining,
      bits: res.bits,
      version: t,
    };
  }
};

const part1 = () => {
  const i = reader.readDataAsString(input);
  const bin = hex2bin(i);

  const a = parsePacket(bin);
  console.log(a.version);
};

const part2 = () => {
  const i = reader.readDataAsString(input);
  const bin = hex2bin(i);

  const a = parsePacket(bin);
  console.log(a);
};

part1();
part2();
