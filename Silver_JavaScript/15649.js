// N과 M (1)

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  const [n, m] = line.split(" ").map(Number);
  const array = [];

  function backtracking() {
    if (array.length === m) {
      console.log(array.join(" "));
      return;
    }

    for (let i = 1; i <= n; i++) {
      if (!array.includes(i)) {
        array.push(i);
        backtracking();
        array.pop();
      }
    }
  }

  backtracking();
  rl.close();
});
