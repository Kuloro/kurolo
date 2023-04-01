const myForm = document.getElementById('form-data');



myForm.addEventListener("submit", e => {  
    e.preventDefault();
    const a1 = document.getElementById('box1').value;
    const a2 = document.getElementById('box2').value;
    const a3 = document.getElementById('box3').value;
    const a4 = document.getElementById('box4').value;
    const a5 = document.getElementById('box5').value;

    
    var d1 = a2-a1
    var d2 = (a3-a2)-(a2-a1)
    var d3 = [(a5-a4)-(a4-a3)]-[(a4-a3)-(a3-a2)]
    var a = d3/6
    var b = (d2/2)-d3
    var c = d1-7*a-3*b
    var d = a1-(a+b+c)

    if ([(a3-a2)-(a2-a1)]-[(a4-a3)-(a3-a2)] == [(a4-a3)-(a3-a2)]-[(a5-a4)-(a4-a3)]) {    
        document.getElementById("cumtoab").innerHTML = a+"n³+"+b+"n²+"+c+"n+"+d
}   else {
        document.getElementById("cumtoab").innerHTML = "นี่ไม่ใช่ลำดับพหุนามดีกรีสาม"
  }
})

