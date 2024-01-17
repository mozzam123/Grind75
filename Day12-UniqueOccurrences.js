
var uniqueOccurrences = function (arr) {
    occurrences = {}
    original_occurrence = []
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] in occurrences) {
            occurrences[arr[i]] += 1
        }
        else {
            occurrences[arr[i]] = 1
        }
    }
    for (var key in occurrences) {
        original_occurrence.push(occurrences[key])
    }
    let sorted_occurrence = [...new Set(original_occurrence)]
    if (JSON.stringify(original_occurrence) === JSON.stringify(sorted_occurrence)) {
        return true
    }
    return false
};

const result = uniqueOccurrences([1, 2, 2, 1, 1, 3])
console.log(result);