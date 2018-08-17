#What is different of while and for loop? which one is fast & why ? Write program for example.

#While Loop
#while loop construct consists of block of codes and a condition.To repeat some lines of code or block of code while a
# given condition is TRUE. In while loop the controls goes to loop body after testing some condition.

#For loop
#In python is little bit different like other programming languages (JavaScript, C and Java). These types of
#language have the concept of index variable that counts the number of iteration in for loop. we represent the values
#we want to process as a range. we have a ready-made collection: a set, tuple, list, map or even a string is already an
#iterable collection, so we simply use a for loop.

#which one is faster?
#A while is faster for shorter loop. while loop is very simple. It simply repeats a set of statements as long as the
#loop expression is True. So in this case, we do a numerical comparison during each iteration
#for is faster for longer loops. for loops are slightly different. Instead of explicitly comparing values, they repeat
# until they run out of data to operate on, which causes a StopIteration exception.

#Examples
def main():
    x = 0
    while(x < 5):
        print(x)
        x = x +1
if __name__ == '__main__': main()


def main():
    x = 0
    for x in range(5, 10):
       print(x)

if __name__ == "__main__": main()
