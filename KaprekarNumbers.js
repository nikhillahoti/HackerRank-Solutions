// Kaprekar Numbers
// A number is Kaprekar Number if its square can be split into two numbers, such that the sum of the two parts
// is equal to the number
// For e.g.  45^2 = 2025; and splitting 2025 as 20 + 25 = 45 <- The number itself

// takes the range in which the kaprekar numbers are to be found
function kaprekarNumbers(p, q){
    let flag = false;
    let result = [];
    for(let i = p ; i <= q ; i++){
        let strSq = String(i*i);
        for(let j = 0; j < strSq.length; j++){
            let leftpart = isNaN(parseInt(strSq.substring(0,j))) ? 0 : parseInt(strSq.substring(0,j));
            let rightpart = parseInt(strSq.substring(j, strSq.length));
            
            if(rightpart > 0 && ((leftpart + rightpart) == i)){
                result.push(i);
                flag = true;
                break;
            } 
        }
    }
    if(!flag) {
        return "INVALID RANGE";
    }
    return result;
}

console.log(kaprekarNumbers(1,99999));