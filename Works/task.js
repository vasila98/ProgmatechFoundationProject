let admin = prompt("1 reqemini daxil edin");

if (admin == 1) {
    function numberA(n) {
        let totoal = 0;
        for (let i = 1; i <= n; i++) {
            totoal += i;
        }
        return totoal;
    }
    number = numberA(100);
    console.log(number);
}