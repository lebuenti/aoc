const readDataAsLine = require("../util");

const exampleInput = "./lea/day04/exampleInput.txt";
const input = "./lea/day04/input.txt";

const isBingo = (board) => {
  for (let line of board) {
    if (line.filter((elem) => elem.marked === false).length === 0) {
      return true;
    }
  }

  for (let j = 0; j < board[0].length; j++) {
    for (let i = 0; i < board.length; i++) {
      if (board[i][j].marked === false) {
        break;
      } else if (board[i][j].marked === true && i === board.length - 1) {
        return true;
      }
    }
  }
};

const calculateBingoScore = (board, number) => {
  let score = 0;
  for (let line of board) {
    const res = line.filter((elem) => elem.marked === false);
    res.forEach((elem) => {
      score += elem.number;
    });
  }
  return score * number;
};

const createNumberAndBoardsFromInput = (puzzleInput) => {
  let numbers = puzzleInput[0].split(",");

  let boards = [];
  let last = 2;
  for (let i = 2; i < puzzleInput.length; i++) {
    if (puzzleInput[i] === "" || i === puzzleInput.length - 1) {
      let tmpBoard = [];

      for (let j = last; j <= i; j++) {
        let tmp = puzzleInput[j].split(/\s+/);
        if (tmp.length === 1) continue;

        let res = tmp.filter((elem) => elem !== "");
        tmpBoard.push(
          res.map((elem) => {
            return { number: parseInt(elem), marked: false };
          })
        );
      }
      boards.push(tmpBoard);
      last = i + 1;
    }
  }

  return { bingoNumbers: numbers, boards: boards };
};

const part1 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine("./lea/day04/input.txt");
  const { boards, bingoNumbers } = createNumberAndBoardsFromInput(puzzleInput);

  let winner = [];

  for (var i = 0; i < bingoNumbers.length; i++) {
    let number = bingoNumbers[i];

    boards.forEach((board) => {
      if (isBingo(board)) {
        winner.push(board);
      }
    });

    if (winner.length > 0) {
      break;
    }

    boards.forEach((board) => {
      board.forEach((line) => {
        let i = line.findIndex((elem) => elem.number === parseInt(number));
        if (i > -1) {
          line[i].marked = true;
        }
      });
    });
  }

  console.log(calculateBingoScore(winner[0], bingoNumbers[i - 1]));
};

const part2 = () => {
  const puzzleInput = readDataAsLine.readDataAsLine(input);
  const { boards, bingoNumbers } = createNumberAndBoardsFromInput(puzzleInput);

  let lastWinner;

  for (var i = 0; i < bingoNumbers.length; i++) {
    let number = bingoNumbers[i];

    let winner = [];

    boards.forEach((board) => {
      if (isBingo(board)) {
        winner.push(board);
      }
    });

    if (winner.length > 0) {
      if (boards.length === 1) {
        lastWinner = boards[0];
        break;
      }

      winner.forEach((w) => {
        let j = boards.findIndex((b) => b === w);
        boards.splice(j, 1);
      });
    }

    boards.forEach((board) => {
      board.forEach((line) => {
        let k = line.findIndex((elem) => elem.number === parseInt(number));
        if (k > -1) {
          line[k].marked = true;
        }
      });
    });
  }

  console.log(calculateBingoScore(lastWinner, bingoNumbers[i - 1]));
};

part1();
part2();
