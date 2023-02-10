import math
def singleRowKeyboard(keyboard,word):
    steps = lastPos = 0
    for w in word:
        currentPos = indexOf(keyboard,w)
        # print(cnt)
        # if last > x:
        steps += abs(lastPos - currentPos)
        # else:
            # cnt += x - last
        lastPos = currentPos 
    print(steps)


def indexOf(keyboard,w):
    for index in range(0,len(keyboard)):
        if keyboard[index] == w:
            return index
    return -1

keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"

singleRowKeyboard(keyboard,word)

keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"

singleRowKeyboard(keyboard,word)



# TC => n * m
# SC => n + m + 1