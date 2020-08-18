# Q1.  Printing all no, in 1 list.

List=[1,2,[2,4,5],4,[2,1]]
final_list = []
for i in List:
	print("i > ",i)
	print(type(i))
	if "int" in str(type(i)):
		final_list.append(i)
	else:
		for j in i:
			final_list.append(j)
	print("final_list = ",final_list)

print(final_list)


# Q2.  factorial number

def fact(a):
	if a==1:
		return 1
	else:
		return fact(a-1)*a

print(fact(int(input("Enter your number: "))))


# Q3. Remove duplicate from the list

def duplicate(a):
	new_list=[]
	for i in a:
		if i not in new_list:
			new_list.append(i)
	print("new_list = ",new_list)
duplicate([34,34,3,24,3,4,3,4,34,3])


# Q4. For checking number is perfect or not:

p=int(input("Enter any No: "))
sum1=0
for i in range(1,p):
	if p%i==0:
		sum1=sum1+i
if sum1==p:
	print("It is a perfect number")
			
else:
	print("It is not a perfect number")


# Q5. For doing number in Decending order:

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
	print(a)
	if b>c:
		print(b)
		print(c)
	else:
		print(c)
		print(b)
elif b>c and b>a:
	print(b)
	if a>c:
		print(a)
		print(c)
	else:
		print(c)
		print(a)
else:
	print(c)
	if a>b:
		print(a)
		print(b)
	else:
		print(b)
		print(a)



# Q6. Counting vowels and constant from the given string:

vowels="aeiou"
user=input("Enter your text: ").lower()
total_count=0
for i in vowels:
	count=user.count(i)
	total_count+=count

print("Vowels=",total_count)
constant=(len(user))-total_count
print("Constant=",constant)


# Q7. for checking type:

a=input("enter anything:-")
numbers = "0123456789"
if ("." not in a) and a not in numbers:
	print("str")
else:
	if "." in a:
		print("float")
	else:
		for i in a:
			if i in numbers:
				print("int")
			else:
				print("its not int")


# Q8. For checking Armstrong Number:

num=int(input("Enter any number: "))
power = len(str(num))
sum=0
b=num
while num>0:
	a=num%10
	sum=sum+a**power
	num=num//10
if b==sum:
	print(b,"It is a arm strong no.")
else:
	print(b,"It is not a arm strong no.")


# Q9.  Program for printing Heart:

for a in range(6):
	for b in range(7):
		if a==0 and b%3!=0 or a==1 and b%3==0 or a-b==2 or a+b==8:
			print("$",end="     ")
		else:
			print(end="     ")
	print()
	print()


# Q10. For printing marks less_than 50 or more than 50:

student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
list_length = len(student_marks)
index = 0
less_than50 = 0
more_than50 = 0
while index < list_length:
	marks = student_marks[index]
	if marks < 50:
		less_than50 = less_than50 + 1
	else:
		more_than50 = more_than50 + 1
	index = index + 1
print ("Marks more than 50: " + str(more_than50))
print ("Marks less than 50: " + str(less_than50))


# Q11.   NAME Printing
        
for i in range(9):
	for j in range(52):
		if (i==8 and j==51) or(i==7 and j==50) or (i==6 and j==49) or (i==5 and j>47 and j<=49) or (j==50 and i>0 and i<=4) or (j==46 and i<=8) or 	(i==0 and j>45 and j<=49) or (i==8 and j>39 and j<=44) or (i==4 and j>39 and j<=44) or (j==40 and i<=8) or (i==0 and j>39 and j<=44) or (i==8 and j>32 and j<=36) or (i==7 and j>36 and j<=37) or (j==38 and i>1 and i<=6) or (j==38 and i>0 and i<=1) or (j==33 and i<=8) or 	(i==0 and j>32 and j<=37) or (i<9 and j==31) or (i>0 and j-i==23) or (j==23 and i<=8) or (i==8 and j>16 and j<=21) or (i==4 and j>16 and j<=21) or (j==17 and i<=8) or (i==0 and j>16 and j<=21) or (i==7 and j==10) or (i==8 and j>10 and j<=12) or (j==13 and i<=8) or (i==0 and j>10 and j<=15) or (j==0 and i<=8) or (i==0 and j>0 and j<=2) or (i==1 and j==3) or (i==2 and j==3) or (i==3 and j==3) or (i==5 and j==3) or (i==6 and j==3) or (i==7 and j==3) or (i==8 and j>0 and j<=2) or (i==4 and j>0 and j<=2) or (i==0 and j>4 and j<=9) or (j==7 and i<=8) or (i==8 and j>4 and j<=9): 
			print("*",end=" ")
		else: 
			print(end="  ")
	print()


# Q12. finding all pair whose sum is equal to the given number:

number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
d=[]
for i in n:
	for j in n:
		a=i+j
		p=i,j
		if a==number:
			d.append(p)
print("Equal pair = ",d)


# Q13. for checking it is magic_square or not:

magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
List=[]
for i in magic_square:
	sum=0
	for j in i:
		sum+=j
	List.append(sum)
for col in range(3):
	sum=0
	for row in magic_square:
		sum+=(row[col])
	List.append(sum)
w=0
r=1
for k in List[1:]:
	if k!=List[w]:
		r+=1
		break
	else:
		w+=1
		r=1
if r==1:
	print('it is magic square')
else:
	print('it is not magic square')


# Q14.  list mei kitne log:

1 - Crorepati hai
2 - Lakhpati hai
3 - Dilwale

kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
a=0
b=0
c=0
for i in kitna_paisa_hai:
	if i>=10000000:
		a+=1
	elif i>=100000:
		b+=1
	elif i<=100000:
		c+=1
print("Croreppati=",a,"\n""Lakhpati=",b,"\n""Dilwale=",c)


# Q15. Counting of same letter:

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
b=[]
for i in char_list:
    if i in b:
        continue
    b.append(i)
    count=0
    for j in char_list:
        if i==j:
            count+=1
    print(i,"=",count,"times")


# Q16. Writting name from exercise.py file to other file: 

# This all name in exercise.py file:

# rishabh - meerut
# imtiyaz - delhi
# nilima - cochin
# rati - shimla
# ayishah - delhi
# raghu - shimla
# naseer - kanpur
# karthikeyan - delhi
# salma - jaipur
# pankaj - delhi
# brijesh - delhi
# govind - delhi
# puneet - shimla
# siddhi - delhi
# suman - jaipur
# rajeev - shimla
# mohinder - delhi
# rajendra - jaipur
# priyanka - shimla
# neela - delhi
# sashi - jaipur
# sarika - delhi
# deepti - shimla
# harshad - delhi
# trishna - raipur
# pradeep - jaipur
# sekhar - delhi
# nand - delhi
# anoop - delhi
# balwinder - tokyo

file=open("exercise.py")
c=file.read()
d=c.split("\n")
for i in d:	
	if 'delhi' in i:
		file = open("delhi.py","a")
		d = i+"\n"
		file.write(d)
	if 'shimla' in i:
		file = open("shimla.py","a")
		d = i+"\n"
		file.write(d)

	if 'delhi' not in i and 'shimla' not in i:
		file = open("other.py","a")
		d = i+"\n"
		file.write(d)

a=open("exercise.py")
c=a.read()
b=c.split("\n")
for i in b:
	if "delhi" in i:
		f=open('delhi.py','w')
		f.write(i)


# Q17. Prime number

while True:
	a=int(input("Enter number: "))
	c=2
	sum=0
	while c<=a:
		if a%c==0:
			sum+=c
		c+=1
	if sum==a:
		print("It is prime number")
	else:
		print("It is not prime number")


# Q18. Program to combine two dictionary adding values for common keys. 

def sum(a,b):
	for i in a:
		print(a[i]+b[i])
a={'a': 100, 'b': 200, 'c':300}
b={'a': 300, 'b': 200, 'd':400,"f":300}

	
a={'a': 100, 'b': 200, 'c':300}
b={'a': 300, 'b': 200, 'c':400,"d":450}
c={}
for i in a:
	c[i]=a[i]
for j in b:
	if j not in c:
		c[j]=b[j]
	else:
		c[j]+=b[j]
print(c)

# Q19. Simple calculator:

def calculator(number_x,number_y,operation):
	if operation=="+":
		return number_x+number_y
	elif operation=="-":
		return number_x-number_y
	elif operation=="*":
		return number_x*number_y
	else:
		return number_x/number_y

print("+,-,*,/")
print()		
b=calculator(10,5,operation =input("Enter your operation: "))
print(b)


# Q20. fibonacci squence even number:

n=int(input("Enter number: "))
a=0
b=1
for i in range(1,n):
	if a%2==0:
		print(a)
	s=a
	a=b
	b=s+a
if n==0:
	print("kuch Nahi")


# Q21. for reversing number:

r = int(input("enter the value to be reversed : "))
lsii = []
for i in str(r):
	lsii.append(i)
lsii.reverse()
for i in lsii:
	print(i,end="")
print()


# Q22. Printing counting from string number to int number till 9:

dict1={ 'zero':0,'one': 1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
n=input("Enter the Value:  ")
a=n.split()
sum=0
for i in a:
	if i in dict1:
		sum+=dict1[i]
print(sum)


# Q23. for printing details:

class Student:
	def __init__(self,first_name,last_name,father_name):
		self.first_name=first_name
		self.last_name=last_name
		self.father_name=father_name
	def fullname(self):
		print("My fullname is",self.first_name,self.last_name)
		print("My father name is",self.father_name)

object1=Student("Bijender","Shakya","Mr.Gopal")
object1.fullname()
