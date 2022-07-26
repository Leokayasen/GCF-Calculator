#---------------------------------------------------------------------------

def gcf_of(factors1,factors2):
#Finds the greatest common factor (gcf) in two input lists
    index = 0
    #Check all the numbers in the factors1 list until the same number is found in the factors2 list
    #Needs the lists to be in numerical order
    while factors1[index] not in factors2:
        index = index + 1
    #Return the highest number found in both lists
    return factors1[index]

#---------------------------------------------------------------------------

def factors_of(number):
#Returns a list of all the factors for a number
    factors = []
    #Check all numbers from the number input down to 0
    for countdown in range(number,0,-1):
        #If the number divided by the count down has no remainder...
        if number % countdown == 0:
            #...it is a factor and is added to the list
            factors.append(countdown)
    return factors

#---------------------------------------------------------------------------

#Main program starts here
#Input the numbers to find greatest common factor
valid = False
while valid == False:
    valid = True
    input1 = input("Enter a number: ")
    input2 = input("Enter a number: ")
    if not input1.isnumeric() or not input2.isnumeric():
        print("Invalid data entry.")
        valid = False
    else:
        input1 = int(input1)
        input2 = int(input2)
        if input1 < 1 or input2 < 1:
            print("Numbers must be greater than 0.")
            valid = False

#Find the factors of the two numbers input
factors1 = factors_of(input1)
factors2 = factors_of(input2)
#Output the greatest common factor of the two numbers
print("The GFC of",input1,"and",input2,"is",gcf_of(factors1,factors2))
