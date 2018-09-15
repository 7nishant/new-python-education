# program to print reverse string
def lst(test):
    n = len(test)
    x = " "
    if test != 0:
        try:
            for i in range(n-1, -1, -1):
                x += test[i]
            return x
        except(TypeError):
            err = 'enter only alphabet'
            return err
    else:
        return 'no number allowed'
