function numberA(n) {
    let totoal = 0;
    for (let i = 1; i <= n; i++) {
        totoal += i;
    }
    return totoal;
}
number = numberA(1000);
console.log(number);