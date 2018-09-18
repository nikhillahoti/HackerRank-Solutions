function get_rock_quantity(quantity){
    let jamie_box = quantity.slice();
    let ned_box = quantity.slice().sort((a,b) => {return a - b});

    let dictCount = {};
    let dictIndex = {};
    
    for(let i = 0 ; i < quantity.length ; i++){
        let total = jamie_box[i] + ned_box[i];
        
        if(total in dictCount) dictCount[total] += 1;
        else dictCount[total] = 1;

        dictIndex[total] = i;
    }
    
    console.log(dictCount);
    console.log(dictIndex);

    let finalKey = Object.keys(dictCount)[0];
    let count = dictCount[finalKey];

    for(let key in dictCount){
        console.log(finalKey + ":" + count);
        console.log(key + ":" + dictCount[key]);
        if(dictCount[key] > count){
            finalKey = key;
            count = dictCount[key];
        }
        else {
            console.log("hhhh + " + key + " + " + finalKey);
            console.log(key > finalKey);
            if(dictCount[key] == count && key > finalKey){
                console.log("here" + key)
                finalKey = key;
            }
        }
        console.log("================");
    }
    console.log(finalKey);
    return dictIndex[finalKey];
}


console.log(get_rock_quantity([1,3,5]));