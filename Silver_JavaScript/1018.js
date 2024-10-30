// 체스판 다시 칠하기

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  const [n, m] = input[0].split(" ").map(Number);
  const board = input.slice(1).map((line) => line.split(""));
  const result = [];

  for (let i = 0; i <= n - 8; i++) {
    for (let j = 0; j <= m - 8; j++) {
      let draw1 = 0;
      let draw2 = 0;

      for (let a = i; a < i + 8; a++) {
        for (let b = j; b < j + 8; b++) {
          if ((a + b) % 2 === 0) {
            if (board[a][b] !== "B") draw1++;
            if (board[a][b] !== "W") draw2++;
          } else {
            if (board[a][b] !== "W") draw1++;
            if (board[a][b] !== "B") draw2++;
          }
        }
      }
      result.push(draw1, draw2);
    }
  }

  console.log(Math.min(...result));
  process.exit();
});
