let birinci = prompt(" birinci ededi daxil edin");
let ikinci = prompt("ikinci eded daxil edin");

Number(birinci)
Number(ikinci)

if (birinci > 30 & birinci < 70 & ikinci > 30 & ikinci < 70) {
    console.log("her iki eded verilen araliga daxildir")
} else if (birinci > 30 & birinci < 70 & ikinci < 30 & ikinci < 70) {
    console.log("sadece birinci eded verilen araliga daxildir")
} else if (birinci > 30 & birinci > 70 & ikinci > 30 & ikinci < 70) {
    console.log("sadece ikinci eded verilen araliga daxildir")
} else if (birinci > 30 & birinci > 70 & ikinci < 30 & ikinci < 70) {
    console.log("hec bir eded verilen araliga daxil deyil")
}