
#Check Number is armstrong or not and return True and False

def armstrong(num):
    numberSum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       numberSum += digit ** 3
       temp //= 10
    
    if (num == numberSum):
        return True
    else:
        return False
        
        
print(armstrong(153))
