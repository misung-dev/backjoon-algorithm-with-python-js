function solution(a, b) {
	if (a > b) {
		return ">";
	} else if (a < b) {
		return "<";
	} else {
		return "==";
	}
}

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const a = parseInt(input[0]);
const b = parseInt(input[1]);

console.log(solution(a, b));

// 테스트 케이스
console.log(solution(1, 2)); // '<'
