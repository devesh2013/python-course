def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("list of 1st and 2nd characters same\n", lst)
    return ctr
count = match_words(['abc', 'cfc' , 'xyz', 'aba', '1221'])
print("number of 1st and 2nd having first and last character same:", count)