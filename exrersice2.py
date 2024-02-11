#Step 1: creating a list
todoList=["ironing"]
# , "doing homework", "cooking", "walk the dog", "do the laundry"

#Step 2: add content inside the list
todoList.append("Wash the dishes")
print("The list is",todoList)

#Step 3: add a  task to the to-do list
addTask= input("What task do you want to add? ")
print(addTask) #showing the task
todoList.append(addTask) #adding the task
print(todoList)

#Step 4: print the number  of  tasks  in  the to-do  list  
sizeList=len(todoList)
# print(sizeList)

#Step 5: remove the  first  task  from  the to-do  list
firstTaskRemove = todoList.pop(0)
# print(todoList)
 
#Step 6: remove a  specific task  from  the to-do  list   
removeTask = todoList.pop(1)
# print(todoList)

# Step 7 what to do the user
print(sizeList)
if(sizeList < 4):
    print("She  has time  to  do more.")
elif (sizeList >= 6):
    print("She  has no room  to  do more  tasks.")
# tell the  user  that if  he/ she  has  less than  4  tasks  on  the to-do  list  she  has time  to  do more    
# tell the  user  that if  he/ she  has more or  equal than  6 items  she  has no room  to  do more  tasks   
