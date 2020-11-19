# in this code List element Count As a Key

names = ["Amogh", "Neeraj", "Mandakini", "Neeraj", "Mandakini", "Neeraj"]

my_dict = {i:names.count(i) for i in names}
print(my_dict)


#OR In Single Line
print({i:names.count(i) for i in names})
