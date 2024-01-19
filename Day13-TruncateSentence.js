var truncateSentence = function (s, k) {
    var s = s.split(" ")
    let formatted_string = []
    if (s.length === k) {
        sameS = s.toString().replaceAll(",", " ")
        return sameS
    }
    else {
        for (let i = 0; i < k; i++) {
            formatted_string.push(s[i])
        }
        formatted_string = formatted_string.toString().replaceAll(",", " ")
        return formatted_string

        
    }

};


obj = truncateSentence("chopper is not a tanuki", 5)
console.log(obj);