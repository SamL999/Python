'''

answer =input("Please input HAPPY \n")

while answer.upper() != "HAPPY" :
    answer =input("Wrong ! Please input HAPPY \n")
else :
    print("  Correct !!!  ")

    
for i in range(5):
    print(i)


name = "David"
for i in range(len(name)):
    print(i, name[i])



answer =input("Please input Good : (Type quit to exit) \n")

while answer.upper() != "GOOD" :
    if answer.upper() == "QUIT":
        print ("You are leaving now !")
        break
    answer =input("Wrong ! Please input Good \n")
else :
    print("  Correct !!!  ")
    
'''

i=0

while i<10:
    i=i+1
    if i%3 !=0:
        continue
    print(i)
        