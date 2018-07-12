#def prime(number):
 #   for num in range(2, number):
  #      status = True
   #     for i in range(2, number):
    #        if num % i == 0:

    #           status = False
     #   if status:
      #      print(num)


#prime(10001)

#print("program completed")


def prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2, n):
            if n % i == 0:
                status = False
    return status
    for n in range(1, 10001):
        if prime(n):
            if n == 10097:
                print(n)
            else:
                print(n, ", ",)

print("program finish")