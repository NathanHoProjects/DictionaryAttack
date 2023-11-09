#Module Import
import time
John = [] 
Dictionary = []
with open("John The Ripper List.txt", "r") as data_file: #Opens datafile
  for line in data_file: #For each line in data file
    data = line.split()
    John.append(data) #Append to list "Jack"

with open('dictionary.txt', 'r') as datafile: #Opens data file
  for line in datafile: #For each line in data file
    data = line.split()
    Dictionary.append(data) #Append to list "dictionary"

#Flattens nested list into a normal list
john = [item for sublist in John for item in sublist]
dictionary = [item for sublist in Dictionary for item in sublist]

#Grabs user input and stores to variable
user1 = input('Please input a username for the first account: ')
pass1 = input('Please input a password for the first account: ')
user2 = input('Please input a username for the second account: ')
pass2 = input('Please input a password for the second account: ')

def passwordcracker1(User1, Pass1, User2, Pass2): #checks if both username and password are the same
  if User1 == Pass1: #If 1st username = 1st password
    print('Test 1')
    print('First account cracked')
    print('Username: ', User1)
    print('Password:', Pass1)
  elif User2 == Pass2:
    print('Test 1')
    print('Second account cracked')
    print('Username: ', User2)
    print('Password:', Pass2)
  else:
    print('Test 1')
    print('Failed to crack both passwords.')
def passwordcracker2(User1, Pass1, User2, Pass2):
  count = 0 #Count used for later 
  start = time.time() #Starts time
  for elem in john: #Runs through john list
    if elem == Pass1: #Checks to see if an element is the same as the passsword
      end = time.time() - start #Finds total time 
      print('Test 2')
      print('First account cracked')
      print('Username: ', User1)
      print('Password', Pass1)
      print('Time taken: ', str(end))
      count = 1 #Disables the rest of the function
  if count == 0: #If first test failed
    start2 = time.time() #Starts the second timer
    for eleme in john: #Runs through john list
      if eleme == Pass2: #If same as 2nd password 
        end2 = time.time() - start2 #Finds total time
        print('Test 2')
        print('Second account cracked')
        print('Username: ', User2)
        print('Password', Pass2)
        print('Time taken:', str(end2))
        print('Total time: ', str(time.time() - start))
        count = 1 #Disables rest of function
        
  if count == 0: #If password failed to crack
    print('Test 2')
    print('Failed to crack both passwords.')
    print('End time: ', str(time.time() - start))


def passwordcracker3(User1, Pass1, User2, Pass2):
  count = 0 #Count used for later 
  start = time.time() #Starts time
  for elem in dictionary: #Runs through john list
    if elem == Pass1: #Checks to see if an element is the same as the passsword
      end = time.time() - start #Finds total time 
      print('Test 3')
      print('First account cracked')
      print('Username: ', User1)
      print('Password', Pass1)
      print('Time taken: ', str(end))
      count = 1 #Disables the rest of the function
  if count == 0: #If first test failed
    start2 = time.time() #Starts the second timer
    for eleme in dictionary: #Runs through john list
      if eleme == Pass2: #If same as 2nd password 
        end2 = time.time() - start2 #Finds total time
        print('Test 3')
        print('Second account cracked')
        print('Username: ', User2)
        print('Password', Pass2)
        print('Time taken:', str(end2))
        print('Total time: ', str(time.time() - start))
        count = 1 #Disables rest of function
        
  if count == 0: #If password failed to crack
    print('Test 3')
    print('Failed to crack both passwords.')
    print('End time: ', str(time.time() - start))
    

#Uses functions created earlier to crack passwords
print()
passwordcracker1(user1, pass1, user2, pass2)
print()
passwordcracker2(user1, pass1, user2, pass2)
print()
passwordcracker3(user1, pass1, user2, pass2)
