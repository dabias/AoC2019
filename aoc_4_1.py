counter = 0
i= 112233
for t in range(1):
#for i in range(168630,718098):
    s = str(i)
    flag = False
    adjacent = 0
    for j in range(len(s)-1): 
        if s[j]>s[j+1]:
            flag = False
            break
        else
            if s[j] == s[j+1]:
                adjacent = True
            else:
                if adjacent == 2:
                    flag = True
                    print('lel')
                adjacent = 0
        if adjacent == 2:
            flag = True
            print('lel')

    if (flag == True):
        counter += 1

print(counter)
