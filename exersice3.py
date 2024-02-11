#Step 1: Create  a  static dictionary with  a  number  of users  and with the following values ​​:  first name, Last name, Email address, Password     
users={
    1: {"firstName": "John", "lastName":"Smith", "emailAddress":"john.smith@example.com", "password":"BlueSky123!" },
    2: {"firstName": "Emily", "lastName":"Johnson", "emailAddress":"emily.johnson@emailprovider.comemily.johnson@emailprovider.com", "password":"Sunflower@789" },
    3: {"firstName": "Michael", "lastName":"Brown", "emailAddress":"michael.brown@example.net", "password":"P@ssw0rd123" },
    4: {"firstName": "Sarah", "lastName":"Davis", "emailAddress":"sarah.davis@emailservice.com", "password":"PurpleDaisy456" },
    5: {"firstName": "David", "lastName":"Lee", "emailAddress":"david.lee@example.org", "password":"GreenGrass987!" },
}

# print("The users are: " , users)
#Step 2: having a variable where to save the information from the loop
nameFirst = ""
nameLast = ""

while nameFirst == "":
    #Step 3: Ask the  user  for : Email address and Passwordcle
    emailInput = input("What is your email?")
    passInput = input("What is your password?")
    #Step 4: Going through the loop 
    for id,info in users.items():
    #Step 4.1: Getting all the information from the dictionary separetly
        fname = info["firstName"]
        lname = info["lastName"]
        email = info["emailAddress"]
        passw = info["password"]
    #Step 5: Checking if the user is in the system or not
        if(emailInput == email and passInput == passw):
            # if they match print the following text
            nameFirst = fname
            nameLast = lname
            break
    print("Your email and password are wrong.Please try agin" )
if(nameFirst != "" and nameLast !=""):
    print("Hello ," , fname, lname, " you have  successfully logged  in" )

#If I dont do the additonal taksk 
# for id,info in users.items():
#     # getting all the information from the dictionary separetly
#     fname = info["firstName"]
#     lname = info["lastName"]
#     email = info["emailAddress"]
#     passw = info["password"]

# #Step 4: Checking if the user is in the system or not
#     if(emailInput == email and passInput == passw):
#         # if they match print the following text
#         nameFirst = fname
#         nameLast = lname
#         break
# if(nameFirst != "" and nameLast !=""):
#     print("Hello ," , fname, lname, " you have  successfully logged  in" )
# else:
#     print("Your email and password are wrong.Please try agin" )
