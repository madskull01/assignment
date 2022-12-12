accountName=[]
accountNumber=[]
accountData=[]
while(True):
 
    a=input("Please enter the command, type comand 'done' to close the program:-")
    command=a.split()
    
    if (command[0]=="CREATE"):
        accountName.append(command[2])
        accountNumber.append(command[1])
        accountData.append(0)
    

    if (command[0]=="DEPOSIT"):
        if(command[1] in accountNumber):
            print("account existed ")
            index=accountNumber.index(command[1])
            data=int(accountData[index])
            data=data+int(command[2])
            accountData.remove(accountData[index])
            accountData.insert(index,data)
        else:
            print("account does not exist")
            
    if (command[0]=="BALANCE"):
        if(command[1] in accountNumber):
            print("account existed ")
            index=accountNumber.index(command[1])
            data=int(accountData[index])
            list1=[]
            list1.append(accountName[index])
            list1.append(data)
            for i in list1:
                print(i, end =" ")
            
           
        else:
            print("account does not exist")

    if (command[0]=="WITHDRAW"):
        if(command[1] in accountNumber):
            print("account existed ")
            index=accountNumber.index(command[1])
            data=int(accountData[index])
            if(data>int(command[2])):
                data=data-int(command[2])
                accountData.remove(accountData[index])
                accountData.insert(index,data)
            else:
                print("your account has not enough balance")
        else:
            print("account does not exist")
    if(command[0]=="done"):
        break

    else:
        print("please check the command use uppercase letters only")
