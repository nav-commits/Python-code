import random

# function name validation
def nameexcution (fname, lname, names):
    
    # if check if its true
    if fname == 'gurveer' and lname == 'gill':
      print( fname + ' is his first name ' +  'and his lastname is ' + lname)
    else:
        print('name not found')
        
    for name in names:
      print( 'other names as well like ' + name)
      
 # here we have dicitonary for user 
user = {"name": "Moe" , "age":27 ,"email": "john123@hotmail.com"}
print('Moes email is : '+ user['email'])

nameexcution('Gurveer','Gill',['John','Joe', 'Moe'])



# code to check if person can afford
priceguess = random.randint(0,200)
content = ' the price is {} $ for the table and you can afford this!'
name = input("enter name:")

# if checks
if priceguess >= 120:
 print(content.format(priceguess) + name)
else:
  print('you cant afford this')
  
  
