function isValid(s){
    let dic = {};
    for(let i = 0 ; i < s.length ; i++){
        if(s[i] in dic) dic[s[i]] += 1;
        else dic[s[i]] = 1;
    }
    
    let nameDic = {};
    for(let key in dic){
        if(dic[key] in nameDic){
            nameDic[dic[key]] = nameDic[dic[key]] + 1;
        }
        else{
            if(Object.keys(nameDic).length > 2){
                return "NO";
            }
            nameDic[dic[key]] = 1;
        } 
    }
    
    if(Object.keys(nameDic).length > 1){
        let firstKey = Object.keys(nameDic)[0];
        let secondKey = Object.keys(nameDic)[1];

        if((nameDic[firstKey] == 1 && ( secondKey == firstKey - 1)) || 
            (nameDic[secondKey] == 1 && ( firstKey == secondKey - 1)) || 
            (nameDic[firstKey] == 1 && firstKey == 1) ||
            (nameDic[secondKey] == 1 && secondKey == 1)  ) return "YES";
        else return "NO";
    }
    return "YES";
}

console.log(isValid("aabbccddeefghi"));