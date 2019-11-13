print("WELCOME TO BOI")
print("PLEASE ENTER CARD")
print("ENTER PIN:")
pin=int(input())
class atm:
    def __init__(self):
        self.pin=pin
        self.bal=10000

    def verify(self):
        global dict
        dict={1234:"harsh",5678:"rahul",9876:"raju"}
        if self.pin in dict:
            print("VERIFIED ACCOUNT:",dict[self.pin])
            return(1)
        else:
            print("PLEASE ENTER A VALID PIN")

    def balance(self):
        print("BALANCE=",self.bal)

    def withdawal(self,amount):
        self.bal=self.bal -amount

    def deposit(self,amount):
        self.bal=self.bal + amount

    def updpin(self,npin):
       dict[npin] = dict.pop(self.pin)
       print("NEW PIN updated for :",dict[npin])


var=atm()
a=var.verify()
if(a):
    l=1
    while(l>0):
        print("PLEASE CHOOSE THE OPTIONS:-")
        print("press 1 for balance")
        print("press 2 for withdrawal")
        print("press 3 for deposit")
        print("press 4 for exit")
        print("press 5 to update pin")
        n=int(input())
        if(n==1):
            var.balance()
        elif(n==2):
            amt=int(input("ENTER AMOUNT TO WITHDRAW:"))
            var.withdawal(amt)
            var.balance()
        elif (n == 3):
            amt1 = int(input("ENTER AMOUNT TO deposit:"))
            var.deposit(amt1)
            var.balance()
        elif (n == 4 ):
            print("HAPPY TO SERVE YOU")
        elif(n==5):
            npin = int(input("ENTER NEW PIN"))
            var.updpin(npin)

        l=int(input("press 1 to continue or 0 to leave:"))
        if (l == 0):
            print("HAPPY TO SERVE YOU")

