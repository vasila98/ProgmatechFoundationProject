let x = 10

function yuxari() {
    let box = document.querySelector(".box");
    box.style.transform = `translate(0px,${-x}px)`;
    x += 10;
}

function asagi() {
    let box = document.querySelector(".box");
    box.style.transform = `translate(0px,${x}px)`;
    x += 10;
}

function saga() {
    let box = document.querySelector(".box");
    box.style.transform = `translate(${x}px,0px)`;
    x += 10;
}


function sola() {
    let box = document.querySelector(".box");
    box.style.transform = `translate(${-x}px,0px)`;
    x += 10;
}