
def encode(s):
    if s == None or len(s) < 1:
        return ""

    counter = len(s)
    strr = []
    dict = {}
    for i in range(0,counter):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] in dict:
            continue
        dict[s[i]] = True
        strr.append(s[i])

    strr = "".join(strr)
    counter = len(strr)
    final = [""] * counter
    for i in range(0, counter):
        index = i+1
        if index == counter:
            index = 0

        total = ord(strr[i]) + ord(strr[index]) - (2*96)
        if total > 26: total = total - 26
        total = total + 96
        final[i] = chr(total)

    return "".join(final)

print(encode("dbcboui"))