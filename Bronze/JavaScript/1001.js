// const fs = require('fs')로 모듈을 불러온다.
// 모듈이란 여러 기능들에 관한 코드가 모여있는 하나의 파일임.
// 다른 모듈을 사용할 때는 require 를, 모듈을 해당 스코프 밖으로 보낼 때에는 module.exports 를 사용함.
const fs = require("fs");

// fs모듈에서 readFileSync 함수로 /dev/stdin을 참조해서 불러오는 것이다.
// 불러온 입력값을 toString()으로 type을 string으로 변환해주고, split(' ')으로 띄어쓰기로 구분해서
// input이라는 배열에 저장하는 것이다.
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const a = parseInt(input[0]);
const b = parseInt(input[1]);

console.log(a - b);

// 참고)
// readFile
// 비동기식 처리 (데이터를 가져올 때 프로그램 진행을 멈추지 않고 그 다음으로 진행함)
// readFileSync
// 동기식 처리 (데이터를 가져올 때 프로그램 진행을 멈추고, 꼭 순서대로 실행함)
