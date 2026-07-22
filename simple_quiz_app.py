###(5. **Simple Quiz App**)

score = 0

print("-Simple_Quiz_App-")

#Q-1
print("\n What is capital of India:")
print("1.Hyderabad")
print("2.Adilabad")
print("3.Banglore")
print("4.Delhi")

Answer = int(input("enter a option from(1-4):"))

if Answer == 4:
    print("Correct")
    score = score+1
else:
    print("Wrong")


#Q2    
print("\n What is the national animal of india:")
print("1.Tiger")
print("2.Lion")
print("3.Fox")
print("4.Camel")

Answer = int(input("enter a option from(1-4):"))

if Answer == 1:
    print("Correct")
    score = score+1
else:
    print("Wrong")

#Q3    
print("\n Who is the prime minister of india:")    
print("1. Rahul Gandhi")
print("2. Narendra Modi")
print("3. Amit Shah")
print("4. Droupadi Murmu")

Answer = int(input("enter a option from(1-4):"))

if Answer==2:
    print("Correct")
    score = score+1
else:
    print("Wrong")
    
#Q4
print("\n Who is the god of cricket in india:")
print("1.Ms.Dhoni")    
print("2.Virat Kohli")
print("3.Rohith Sharma")
print("4. Sachin Tendulkar")

Answer = int(input("enter a option from (1-4):"))
if Answer==4:
    print("Correct")
    score=score+1
else:
    print("wrong")
    
#Q5

print("\n4. When do we celebrate Independence Day in India?")
print("1. 26 January")
print("2. 15 August")
print("3. 2 October")
print("4. 14 November")

answer = int(input("Enter your answer (1-4): "))

if answer == 2:
    print("Correct")
    score = score+1
else:
    print("Wrong")
    
print("\n-Quiz Result-")
print("Your Score =", score, "/5")
   
   
if score >=4:
    print("Excellent You Performed Very Well")
elif score>=3:
    print("Good")
elif score>=2:
    print("Average")
else:
    print("Fail")


    
    
