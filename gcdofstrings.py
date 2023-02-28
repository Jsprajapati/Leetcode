
def gcdOfStrings(str1: str, str2: str) -> str:
    gcdS = ""
    foundL = 0
    for i in range(0,len(str1)-1):
        if str1[:i] in str2:
            foundL += 1
        else:
            print("Not",i)
    if foundL > 0:
        # str1[:foundL-1]

# ABCABC
# 012345
# 
# 
# 

print(gcdOfStrings("ABCABC","ABC"))
print(gcdOfStrings("ABABAB","ABAB"))
print(gcdOfStrings("LEET","CODE"))
# gcdOfStrings("ABABAB","ABAB")
# gcdOfStrings("LEET","CODE")
# gcdOfStrings("ABCABC","ABC")
