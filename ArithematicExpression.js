function arithmeticExpressions(arr) {
    let elem = arr.shift();
    return checkDivisiblity(arr, "" + elem, elem);
}

function checkDivisiblity(arr, exp, result){
    // check if the result is divisible by 101. result will contain the operation performed yet
    if(result % 101 == 0){
        // When it is divisible, just appending all the other operations by *
        if(arr.length > 0) return exp + "*" + arr.join("*");
        return exp;
    }

    if(arr.length > 0){
        let elem = arr.shift();
        let finalExp = checkDivisiblity(arr.slice(0), exp + "+" + elem, result + elem);
        if(finalExp != "") return finalExp;

        finalExp = checkDivisiblity(arr.slice(0), exp + "-" + elem, result - elem);
        if(finalExp != "") return finalExp;

        finalExp = checkDivisiblity(arr.slice(0), exp + "*" + elem, result * elem);
        if(finalExp != "") return finalExp;

        return "";
    }
    else {
        return "";
    }
}

console.log(arithmeticExpressions([79, 22, 45, 33, 25]));
//arithmeticExpressions([55, 3, 45, 33, 25]);
















