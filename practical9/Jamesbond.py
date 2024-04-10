s={'a':"Roger Moore", 'b':"Timothy Dalton", 'c':"Pierce Brosnan", 'd':"Daniel Craig"}
def birthyear(x):
     x+=18
     if x<1986:
         y='a'
     else:
        if x<1994:
            y='b'
        else:
            if x<2005:
               y='c' 
            else:
               y='d'
     return y                       
x=int(input("The birthyear:"))
y=birthyear(x)
print("actor is " +s[y])

            


