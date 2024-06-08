import pro1
import pro2
import pro3
import pro4
import pro5
import pro6
print("***Welcome to my Bank Application ***")
print("Your Bank services")
print("1.Create Account")
print("2.Display All Account")
print("3.Deposit")
print("4.Withdraw")
print("5.Search by one accountant details")
print("6.Balance Enquery")
print("7.Quit")
while True:
    n=int(input("Enter your choice"))
    if (n==1):
        accno=int(input("Enter the accno: "))
        accname=input("Enter the accname: ")
        acctype=input("Enter the acctype: ")
        balance=int(input("Enter the balance: "))
    if (n==2):
        pro2.Display()
    if (n==3):
        accno=int(input("accno: "))
        balance=int(input("deposit amt:"))
        pro3.deposit(accno,balance)
    if (n==4):
        accno=int(input("accno: "))
        balance=int(input("withdraw amt: "))
        pro4.withdraw(accno,balance)
    if(n==5):
        accno=int(input("accno: "))
        pro5.accountant(accno)
    if (n==6):
        accno=int(input("accno: "))
        pro6.Balanceenquery(accno)
    if (n==7):
        break
pro1.insertData(accno,accname,acctype,balance)
