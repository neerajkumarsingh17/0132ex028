
#shortest code in min line
# method 1
def fibonacci(length, first=0, second=1):
    if length <= 0:
       print("Please enter a positive integer")
    elif length == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
        for _ in range(length):
            print (first)
            nth_num = first + second
            first = second
            second = nth_num

fibonacci(10)

#O/P 0 1 1 2 3 5 8 13 21 34
        
# method 1
# if you not want to write fun you want to give number as a input the do this type 
length = int(input("How many terms? "))
first=0
second=1
if length <= 0:
       print("Please enter a positive integer")
elif length == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
    for _ in range(length):
        print (first)
        nth_num = first + second
        first = second
        second = nth_num


