import os
# p = os.getcwd()
# print(p)
# os.chdir('D://')
# if not os.path.exists("TempDir"):
#     os.mkdir('TempDir')
# print(os.getcwd())    
a = input("enter your name:")
if not os.path.exists(a):
    os.mkdir(a)
