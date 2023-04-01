const myForm = document.getElementById('form-data');



myForm.addEventListener("submit", e => {  
    e.preventDefault();
    const a1 = document.getElementById('box1').value;
    const a2 = document.getElementById('box2').value;
    const a3 = document.getElementById('box3').value;
    const a4 = document.getElementById('box4').value;
    
    var d1 = a2-a1
    var d2 = (a3-a2)-(a2-a1)
    var a = d2/2
    var b = d1-(3*d2)/2
    var c = (2*a1-a2)+d2

    if ((a3-a2)-(a2-a1) == (a4-a3)-(a3-a2)) {    
        document.getElementById("cumtoab").innerHTML = a+"n²+"+b+"n+"+c
}   else {
        document.getElementById("cumtoab").innerHTML = "นี่ไม่ใช่ลำดับพหุนามดีกรีสอง"
  }
})

document.getElementById("index").style.transition = "all 2s";