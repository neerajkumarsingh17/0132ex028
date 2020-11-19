# if you provide range then find between prime number in double line code only then write this type of code

for num in range(100,200):
    if all(num%i !=0 for i in range(2, num)):
        print(num)
        
        
# in second method if you have number and check this number is prime or not then do this type of code

num = 103
if num>1:
    for i in range(2, num):
        if (num%i) == 0:
            print("{} is not Prime".format(num))
            break
        else:
            print("{} is prime number".format(num))
            break
else:
    print("{} is not Prime".format(num))
