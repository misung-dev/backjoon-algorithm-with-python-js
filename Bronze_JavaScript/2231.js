// 분해합

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const num = parseInt(input);
let result = 0;

for (let i = 0; i <= num; i++) {
  let sum = i;
  const numList = String(i).split("").map(Number);

  sum += numList.reduce((acc, curr) => acc + curr, 0);

  if (sum === num) {
    result = i;
    console.log(result);
    break;
  }
}

// 조건을 만족하는 생성자가 없는 경우
if (result === 0) {
  console.log(0);
}
