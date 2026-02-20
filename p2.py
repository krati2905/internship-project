# n = 5
# for i in range(1,n+1):
#     print("* " * i )
# for i in range(1,n+1):
#     print(" " *(n-i)+"* "* i)

# user = "krati"
# age = 20
# amount = 100
# print(f"welcome {user},you are {age} years old and your salary is ${amount}")
# # print(f"welcome {user},you are {age} years old and your salary is ${amount:10.4}")
# print(f"welcome {user},you are {age} years old and your salary is $ %2.7x"%amount)
# # print("welcome{} your age{} and salary{}" .format{user})

a=[3,4,5]
max_val = max(a)
for i in range(max_val):
    for j in a:
        if j >= max_val - i:
            print('* ', end ='')
        else:
            print('  ', end ='')
    print()    

