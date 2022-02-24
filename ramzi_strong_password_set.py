print('WELCOME TO MY PYRHON TASK')
a="C:/Users/Administrator/Downloads/ramzi/ramzi/project1/students.txt"
try:
    open(a,"r")
    print(a.read())
except IOError:
    print("file does not exist")
finally:
    a.close()   
id=""
password=""
special_char=['=','+','!']
print("Enter your credentials:")
id=input("Enter the student'sID:")
if id=="001" or id=="002" or id=="003":
 for a in range(3):
  password= input("Enter the student's password:")
  if len(password) < 8:
   print("Make sure your password is at lest 8 character")
  elif not any (char.isdigit() for char in password):
   print("Make sure your password has a number in it")
  elif not any (char.isupper() for char in password):
   print("Make sure that your password has a capital letter in it")
  elif any(char in special_char for char in password):
    print("Symbol(s) used should not be the part of password")
  else:
    print("Your password seems to be fine")
    file = open('final_students.txt', 'a+')
    if id=="001":
         file.write("id:001,firstname:Eric,lastname:Smith,Password:"+password+'\n')
    if id=="002":
         file.write("id:002,firstname:Alice,lastname:Brown,Password:"+password+'\n')
    if id=="003":
         file.write("id:003,firstname:Robert,lastname:Rock,Password:"+password+'\n')
    file.close()
    exit()
else:
    print("invalid id")
