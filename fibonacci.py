
#shortest code in min line

def fibonacci(length, first=0, second=1):
    
    for _ in range(length):
        print (first)
        nth_num = first + second
        first = second
        second = nth_num
