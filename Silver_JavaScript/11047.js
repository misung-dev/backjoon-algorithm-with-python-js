// 동전 0

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (firstInput) => {
  const [n, k] = firstInput.split(" ").map(Number);
  let coinList = [];
  let count = 0;
  let remainingAmount = k;

  const getCoins = (index) => {
    if (index < n) {
      rl.question("", (coinInput) => {
        coinList.push(parseInt(coinInput));
        getCoins(index + 1);
      });
    } else {
      coinList.sort((a, b) => b - a);

      for (let coin of coinList) {
        count += Math.floor(remainingAmount / coin);
        remainingAmount %= coin;
      }

      console.log(count);
      rl.close();
    }
  };

  getCoins(0);
});
