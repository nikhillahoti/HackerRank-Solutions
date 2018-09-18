function encode(s){

    let dict = {};
    let vowels = {'a': true, 'e': true, 'i': true, 'o': true, 'u': true};
    let encodedString = "";

    for(let i = 0 ; i < s.length ; i++){
        if(s[i] in dict || s[i] in vowels){
            continue;
        }
        let index = i + 1;
        if(index == s.length) index = 0;

        /*console.log("-----------");
        console.log(s[i] + ":" + ((s[i] + "").charCodeAt(0)));
        console.log(s[index]+ ":" + ((s[index] + "").charCodeAt(0)));*/

        let value = ((s[i] + "").charCodeAt(0) - 96) + ((s[index] + "").charCodeAt(0) - 96);
        if(value > 26){
            value = value - 26;
        }
        //console.log("value:" + value);
        dict[s[i]] = true;
        //console.log(typeof String.fromCharCode(value + 96));
        encodedString += String.fromCharCode(value + 96);
    }
    return encodedString;
}

console.log(encode("aeious"));