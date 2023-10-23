```javascript
var obj = {
    val1: '',
    val2: '',
    op: ' ', // operator +-x/
    step: 1, // user pressing the number 1st time or not
    equal: ' '
}
var val = " "
function number(n){
    console.log("n >>> ", n)
    if(obj.step == 1) {
        obj.val1 += n; //connect all values in string
        val = obj.val1
    }
    else{
        obj.val2 += n
        val = obj.val2
    }
    document.getElementById("shownumber").innerHTML = val
    console.log("obj", obj)
    
}

function remove(){
    var val = document.getElementById("shownumber").innerHTML
    var new_val = "0"
    if(val.length <= 1){
        if(obj.step == 1) {
            obj.val1 = new_val;
        }
        else {
            obj.val2 = new_val;
        }
    }
    else {
        new_val = val.substring(0, val.length -1)
        if(obj.step == 1) {
            obj.val1 = new_val;
        }
        else {
            obj.val2 = new_val;
        }
    }
    document.getElementById("shownumber").innerHTML = new_val
    console.log("obj", obj)
}

function operator(op, el){
    console.log("op", op, "el", el.id)
    obj.step = 2;
    obj.op = op; // store operator sign of the button we click
    console.log("obj", obj)
}

function equal() {
    if(obj.op == "+") {
        obj.equal = parseFloat(obj.val1) + parseFloat(obj.val2)
    }
    else if(obj.op == "-") {
        obj.equal = parseFloat(obj.val1) - parseFloat(obj.val2)
    }
    else if(obj.op == "x") {
        obj.equal = parseFloat(obj.val1) * parseFloat(obj.val2)
    }
    else if(obj.op == "/") {
        obj.equal = parseFloat(obj.val1) / parseFloat(obj.val2)
    }
    
    document.getElementById("shownumber").innerHTML = obj.equal

    // clear for new calculation
    obj.step = 1
    obj.op = ''
    obj.val1 = obj.equal
    obj.val2 = ''
    console.log("obj", obj)
}

function clear_val() {
    obj = {
        val1: '',
        val2: '',
        op: ' ', 
        step: 1, 
        equal: ' '
    } // reset all the values
    var reset = "0"
    document.getElementById("shownumber").innerHTML = reset
    console.log("obj", obj)
}

function percent() { // convert number into percentage in terms of 100
    val = document.getElementById("shownumber").innerHTML 
    new_val = "0"
    if(obj.step == 1) {
        obj.val1 = (val)/100
        new_val = obj.val1
    }
    else if (obj.step ==2) {
        obj.val2 = (val)/100
        new_val = obj.val2
    }
    document.getElementById("shownumber").innerHTML = new_val
    console.log("obj", obj)
    
}

function dot() {
    val = document.getElementById("shownumber").innerHTML
    new_val = "0"
    if(val == "0") {
        if(obj.step == 1){
            obj.val1 += "0."
            new_val = obj.val1
        }
        else {
            obj.val2 += "0."
            new_val = obj.val1
        }
    }
    else if (val.indexOf(".") == -1){
        if(obj.step == 1){
            obj.val1 += "."
            new_val = obj.val1
        }
        else {
            obj.val2 += "."
            new_val = obj.val1
        }
    }

    document.getElementById("shownumber").innerHTML = new_val
    console.log("obj", obj)
}

```
