'''print("ramchadra");
print("ram","chandra","bhatta",sep="-"); # this sep function is use seperated all the content 
# program to find addition multiplication subtraction division and modulus 
a=int(input('enter a number:'))
b=int(input('enter b number:'))
c=a+b;
d=a*b
e=a-b;
f=a/b
g=a%b
print("The sum of a and b is:",c)  
print("The multiplication of two num:",d)  
print("The subtraction of two number is:",e)
print("The division of two number is:",f) 
print("The modulos of two number is:",g)

# program to find Even and odd number 
num=int(input("Enter a number"))# input number from user
if num%2==1:{                       # Even number condition 
print("the number is Odd")
}
else:
    {
print("the number is even")
    }

#program of voting System 
age =int(input("Enter the age  :"))
if age>=18:
    {
    print("Eligible for voting")
    }
else:
    {
print("Not eligible for voting")
    }

    # program to finds the greater number from two number 
num1=int(input("emter first number:"))
num2=int(input("enter second number:"))
if num1>num2:
    {
        print("num one is greater ")
    }
else: 
    {
        print("Num two is greater ")
    }
 
#program of largest among three number 
a=int(input("Enter first num"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
if a>b and a>c:
    max=a;
elif b>a and b>c:
    max=b;
else:
    max=c;
print("The maximum value is:",max )

#find natural number using for loop 
num=int(input("Enter a number"))
for i in range(1,num+1):
    
    print(i,"I love you");


# Area of rectangle 
L=int(input("Enter the value of leangth="))
B=int(input("Enter the value of breadth="))
Area=L*B;
print("The area of rectangle is:",Area);

# FIND THE AREA OF SQUARE 
A=int(input("enter the side "));
Area=A*A;
print("The area of square is ",Area);

# calculate The area of circle
r=float(input("Enter the radious:"))
Area=3.14*r*r
print("The area of circle is :",Area)

# calculate the Area of triangle

# s= (a+b+c)/2
#area = (*s*(s-a)*(s-b)*(s-c))**0.5
a=float(input("ENter the side of A="))
b=float(input("Enter the side of b="))
c=float(input("enter the side of c="))
s=(a+b+c)/2;
Area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of Triangle  =",Area);


#Swapping the value of a and b
a=int(input("Enter the value of A :"))
b=int(input("Enter the value of b :"))
a=a+b
b=a-b
a=a-b;
print("A =",a,"B=",b)

# calculate the factorial of N number
Num=int(input("Enter a number"))
fact=1;
for i in range(1,Num+1):
    fact=fact*i;
print("factoial :",fact)
'''
 
"""# check the Number is palindrone or not   example 121 same reverse
n=int(input("enter a Number"))
temp=n
sum=0

while n>0:
    r=n%10 
    sum=sum*10+r
    n=n//10
    if temp==sum:{
        print("palindrame Number")
    }
    else:
        {
        print("Not palindrame")
        }
        """

 #reverse number of the  given data
 #input 321
 #output 123
n=int(input("enter a number"))
while n>0:
    r=n%10
    print(r,end="")
    n=n//10