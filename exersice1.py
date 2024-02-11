#Step 1: Calculating how much one Oreo has calories ,  sodium ,  carbohydrate , fat and printing the result
countOreo = 3
calories = 160/countOreo
print(calories)

sodium = 190/countOreo
print(sodium)

carbohydrate = 25/countOreo
print(carbohydrate)

fat = 7/countOreo
print(fat)

#Step 2: Asking the user How many  cookies  you ate?
ateCookies = int(input("How many  cookies  you ate? ")) #I am making a number so afer that I can calculate it. 
# I put an integer in front so I can turn the answer in number. I can use it for later calculations.
print(ateCookies)

#Step 3: How much is that? -  calculating the cookies with the calories for one cookie
ateCalories = calories * ateCookies
print(ateCalories)

ateSodium = sodium * ateCookies
print(ateSodium)

ateCarbohydrate = carbohydrate * ateCookies
print(ateCarbohydrate)

ateFat = fat * ateCookies
print(ateFat)

#Step 4:warn the  user  that if  he/ she surpasses  2000kcal he/ she should  stop  eating  these  darn delicious  cookies 
calorisLimit = 2000 
if(calorisLimit < ateCalories):
    print("You should  stop  eating  these  darn delicious  cookies ")