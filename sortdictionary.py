# if ascending is True (default), the dictionary will be sorted from least to greatest value
# if ascending is False, the dictionary will be sorted from greatest to least value
def sortDictionaryByValues(dictionaryName, ascending=True):
    if (type(ascending) != bool and type(dictionaryName) != dict):
        raise ValueError("sortDictionaryByValues requires a dictionary and boolean as arguments, respectively")
        return None
    else:
        sortedDictionary = {}
        sortedList = sorted(dictionaryName.items(),key=lambda x: x[1], reverse=(not ascending))
        for item in sortedList:
            sortedDictionary[item[0]] = item[1]
        return sortedDictionary
        #return(sortedList)

        