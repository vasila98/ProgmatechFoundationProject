let color = ["#00FFAC ", "#FFFB03", " #8D4BDB ", "  #F309B3", "#B60031 ", " #083B67 ", " #1ABC9C", " #F1948A ", " #CCD1D1 ", " #BDC3C7 "]
let x = 0
document.querySelector("button").addEventListener("click",
    function() {
        x = 1 < color.length ? ++x : 0

        document.querySelector("body").style.background = color[x]

        document.getElementById("span").innerHTML = color[x]
        this.style.backgroundColor = color[x];

    })