def result(n):
    for num in range(320, 444374):
        if num % 13 == 0 and num % 7 == 0:
            print(str(num) + " ", end = " ")
        else:
            pass
if __name__ == "__main__":
    n = 320
print(result(n))
