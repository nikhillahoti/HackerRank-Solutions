function candies(n, arr) {
    let indiv = [1];
    for(let i = 1 ; i < arr.length ; i++){
        indiv.push(1);
        if(arr[i] > arr[i-1]){
            // Current students rating is higher than the previous
            // Giving more candies to this person
            indiv[i] = indiv[i-1] + 1;
        }
        else {
            for(let j = i ; j > 0 ; j--){
                if(arr[j] < arr[j-1] && indiv[j-1] <= indiv[j]){
                    // the rating of the previous person was greater so incrementing his candy share
                    indiv[j-1] = indiv[j] + 1;
                }
                else {
                    break;
                }
            }
        }
    }

    console.log(indiv);
    let total = 0;
    for (let i = 0; i < indiv.length ; i++){
        total += indiv[i];
    }
    return total;
}

console.log(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]));
