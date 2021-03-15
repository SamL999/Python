
"""
text=

將以下內容儲存到檔案
1. Apple
2. Box
3. Cloud


print(text,file=open('data.txt','a'))

print(text,file=open(R'C:\Users\user\Desktop\Python\test\data.txt','a'))


file = open(R'C:\Users\user\Desktop\Python\test\wrdata.txt','w')
file.write("I want write data to file \n")
file.write("This is a test.\n")
file.write("987654321 \n")
file.close()



file = open(R'C:\Users\user\Desktop\Python\test\wrdata.txt','r')
content = file.read()
print(content)
file.close()


with open(R'C:\Users\user\Desktop\Python\test\wrdata.txt',"w") as file:
    file.write("I want a power \n")
    file.write("It is Good Job ! \n")
    file.write("33226688 \n")
     
with open(R'C:\Users\user\Desktop\Python\test\wrdata.txt',"r") as file:
     content = file.read()
     print(content)     
     
"""

