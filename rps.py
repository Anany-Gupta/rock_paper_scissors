import sys
p1=''                      #player one name
p2=''                      #player two name
p1ch=0                     #player 1 choice
p2ch=0                     #player 2 choice 
sp1=0
sp2=0
flag=0

p1=str(input("Enter name for Player 1  :  "))
p2=str(input("Enter name for player 2  :  "))

print("\n Name for player 1 : ",p1,"\n Name for player 2 : ",p2)
ch='y'
#Functions
def play(): 
    p1ch=int(input("Player 1 Enter your choice\n  1.Rock\n  2.Paper\n  3.Scissors\n  "))
    p2ch=int(input("Player 2 Enter your choice\n  1.Rock\n  2.Paper\n  3.Scissors\n  "))
    if ((p1ch==1) or (p1ch==2) or (p1ch==3)):
      if ((p2ch==1) or (p2ch==2) or (p2ch==3)): 
       m=cal(p1ch,p2ch,-1)
       return m
    else:
       print("please input correct values!!!!!")
def cal(a,b,flag=-1):
    if (a==b):
        print("Its a TIE")
    elif (a==1):
        if (b==2):
            print(p1," chooose Rock and ",p2," choose Paper hence",p2,"  WINS!!!")
            flag=1
        else:    
            print(p1," chooose Rock and ",p2," choose Scissors hence",p1,"  WINS!!!")
            flag=0
    elif (a==2):
        if (b==3):
            print(p1," chooose Paper and ",p2," choose Scissors hence",p2,"  WINS!!!")
            flag=1
        else:    
            print(p1," chooose Paper and ",p2," choose Rock hence",p1,"  WINS!!!")
            flag=0
    elif (a==3):
        if (b==2):
            print(p1," chooose Scissors and ",p2," choose Paper hence",p1,"  WINS!!!")
            flag=0
        else:    
            print(p1," chooose Scissors and ",p2," choose Rock hence",p2,"  WINS!!!")        
            flag=1
    return flag
#a    print("Scoreboard : ",p1," = ",sp1,"   ",p2," = ",sp2 )
while (ch=='y')or(ch=='Y'):
   sp1=0
   sp2=0
   i=1
   while (sp1<5) & (sp2<5):
       print("\n\n\n\nRound  ", i," :\n " )
       flag=play()
       if (flag==0):sp1+=1
       elif(flag==+1):sp2+=1     
       print("Score is ",p1,"   ",sp1,p2,"  = ",sp2)
       i+=1
   
   ch=str(input("Do you wish to play again y/n "))
print("Thank You for playing")   
            


    
    






