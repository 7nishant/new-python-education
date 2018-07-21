# wap which give prime numbre range of 500 TO 10000

for num in range(500,10000 + 1):
    if num > 1:
        for j in range(2,num):
            if num % j == 0:
                break
        else:
            print(num)


#primelist = []
#for num in range(500,10000 + 1):
#    if num > 1:
#        for j in range(2,num):
#            if num % j == 0:
#                break
#        else:
#            primelist.append(num)
#print "Prime Number:", primelist
