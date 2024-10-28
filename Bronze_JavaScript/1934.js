// 최소공배수

const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const gcd = (a, b) => {
  while (b > 0) {
    let temp = b;
    b = a % b;
    a = temp;
  }

  return a;
};

const lcm = (a, b) => {
  return (a * b) / gcd(a, b);
};

const num = parseInt(input[0]);

for (let i = 1; i <= num; i++) {
  let [num1, num2] = input[i].split(" ").map(Number);

  console.log(lcm(num1, num2));
}
