#list
students = ['leroy', 'julius', 'collins', 'omar', 'gabriel']
print (students)

#creating empty list
students = []
print (students)

#indexing the list
students = ['leroy', 'julius', 'collins', 'omar', 'gabriel','samuel']
print (students [1]) #display index 1 from the list
print (students [0]) #display index 0 from the list
print (students [2:5]) #display index 2.5 from the list
print (students [2:]) #display index 2: from the list
print (students [:5]) #display index :5 from the list

#indexing replacing
students [3]= 'richard' #replacing 'omar' with 'richard'
print (students) #display the replacement index

#loop through the list
for student in students:
    print (student) #display the loop result
    
#check if item exists
if 'richard' in students:
    print ('richard is here')
    print ('richard is not here')

#methods
#len(), append(), insert(), pop():
    print (len(students)) #displaying the length of the list
    students.append('teddy') #inserting teddy at the end of the list
    print (students)
    students.insert(3, 'julius') #inserting julius in index 3
    print (students)
    students.pop(3)
    print (students)
    students.remove ('julius') #removes 'julius' from the list
    print (students)
    students.reverse () #reversing list & beginning from last to first
    print (students)
    students.sort() #sorting list in an alphabetical order
    print (students)
    students.clear() #clearing list
    print (students)