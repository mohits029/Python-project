import random
words= ["python","physics","designer","product","service","explore","drink","hidden","makeup"]
i=0
s= []
score= 0



def arrengement(w):
    global score
    x= mesh(w)
    print(x)
    y= input("Arrange the above word: ")
    if w==y:
        print("correct")
        score= score+1
    else:
        score= score-1
        print("Wrong")
    


# generate random character of a word
def mesh(w):
    randChar= []
    s= []
    i= 0
    while i< len(w):
        n= random.randint(0, (len(w)-1))
        if n in s:
            continue
        else:
            s.append(n)
            randChar.append(w[n])
            i+=1
    else:
        return randChar



# generate random five words
while i<5:
    n= random.randint(0, (len(words)-1))
    if n in s:
        continue
    else:
        s.append(n)
        arrengement(words[n])
        i+=1


print("Net Score= ",score)
    

    
    