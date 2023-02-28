
s = [-89,1,9,8,3,10,99,-10,394,9894,734,6,64,4235,9823,48,0]

min = 9999
max = -9999
for i in range(0,len(s)):
    if s[i] < min:
        min = s[i]
    # else:
    if s[i] > max:
        max = s[i]


print(max)
print(min)
