

def merge_the_tools(string, k):
    # your code goes here

    if string is None:
        return

    counter = int(len(string) / k)
    for i in range(0,counter):
        sub = ""
        cnt = k * i
        for j in range(cnt, cnt + k):
            if(string[j] in sub):
                continue
            else:
                sub = sub + string[j]
        print(sub)


merge_the_tools("AABCAAADA", 3)