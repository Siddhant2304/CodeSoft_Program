n1=int(input("Enter A Number 1 \n"))
n2=int(input("Enter A Number 2 \n"))

operation=int(input('''Enter A Operations You Want To Perform
Press 1 For Addition
Press 2 For Subtraction
Press 3 For Multiplication
Press 4 For Division \n'''))

if operation==1:
    add=n1+n2
    print("The Addition of given Two Number is : ",add)
elif operation==2:
    sub=n1-n2
    print("The Subtraction of given Two Number is : ",sub)
elif operation==3:
    multi=n1*n2
    print("The Multiplication of given Two Number is : ",multi)
elif operation==4:
    div=n1/n2
    print("The Division Of Given two Number is :",div)
else:
    print("Invaild Choice Of Operation Retry !!!!!")

