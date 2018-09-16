#program to convert USD to INR

def curr(amount):
    amount = float(amount)
    if amount > 0:
        try:
            usd = amount * 72;
            return usd
        except(TypeError):
            err = 'the value suppose to be positive'
            return err
    else:
        return 'no negative value allowed'
#print(curr(input("Enter an USD amount to convert: ")))