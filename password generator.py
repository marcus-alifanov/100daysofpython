#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# LETTER SECTION

def letters_final():
    # How many letters?
    total_letters = len(letters)  # This counts the number of letters in the list
    
    # Random NUM Letters
    letters_num_array = []
    for letter_num in range(1, nr_letters + 1):
        random_letter_num = random.randint(1, total_letters)
        letters_num_array.append(random_letter_num)
    #print(letters_num_array)

    # WORKING - letters_final()
    
    letter_array = []
    # Random Letters
    for position in letters_num_array:
        selected_letter = letters[position - 1]  # Adjust for zero-based index
        letter_array.append(selected_letter)
    #print(letter_array)
    return letter_array
    
letters_final()  # Working



# SYMBOL SECTION

def symbols_final():
    # How many Symbols?
    total_symbols = len(symbols)  # This counts the number of symbols in the list
    
    # Random NUM Symbols
    symbols_num_array = []
    for symbol_num in range(1, nr_symbols + 1):
        random_symbol_num = random.randint(1, total_symbols)
        symbols_num_array.append(random_symbol_num)
    #print(symbols_num_array)

    # WORKING - Symbols_final()
    
    symbol_array = []
    # Random symbols
    for position in symbols_num_array:
        selected_symbol = symbols[position - 1]  # Adjust for zero-based index
        symbol_array.append(selected_symbol)
    #print(symbol_array)
    return(symbol_array)
    
symbols_final()  # WORKING


#NUMBER SECTION (same system as above)

def numbers_final():
    #How many Numbers?
    total_numbers = 0
    for number in numbers:
        total_numbers += 1
    #Random NUM Numbers
    numbers_num_array = []
    for number_num in range(1, nr_numbers + 1):
        random_number_num = random.randint(1, total_numbers) 
        numbers_num_array.append(random_number_num)
    #print(numbers_num_array)
    return numbers_num_array

# WORKING - numbers_final()

    number_array = []
    #Random numbers
    for position in numbers_num_array:
        selected_number = numbers[position - 1]  # Adjust for zero-based index
        number_array.append(selected_number)
    #WORKING - print(number_array)
    
numbers_final() #WORKING

#JOINING STRINGS [Easy Level]

def joined_string():
    #NEW ARRAY
    final_joined = []
    #NEW ARRAY joining
    final_joined.append(letters_final())
    final_joined.append(symbols_final())
    final_joined.append(numbers_final())

    # Flatten the list and convert all elements to string
    flattened_list = [str(item) for sublist in final_joined for item in sublist]

    # Join all elements into a single string
    result_ordered = ''.join(flattened_list)

    return result_ordered

joined_string()


# # Randomise String [HARD LEVEL]

# Random array order (ex. 5,2,8...)
#   Based on length of joined_string(), creates array 1-length joined_strings()
num_array = []
num_times_loop = 0
for i in range(1, len(joined_string())+1): #REMEMBER 0
    num_array.append(num_times_loop)
    num_times_loop +=1
#print(num_array) #WORKS!

# Randomise num_array order / shuffeled array for order

random.shuffle(num_array)
#print(num_array) #WORKS!

#[11, 8, 0, 9, 15, 6, 4, 5, 1, 3, 14, 13, 2, 7, 10, 12]
#To do is...       varibale = num_array[i] #== 11     
#    result_ordered[variable]
#for loop range

final_string = ""
string = joined_string()
for i in range(1, len(string)+1):
    if i-1 < len(num_array):
        var = num_array[i-1]
        if 0 <= var < len(string):  # Ensure var is a valid index
            variable2 = string[var]
            final_string = final_string + variable2
            # WORKS - print(variable2)

print("**********************************************")

print(f"Your selected password is: {final_string}")

print("**********************************************")
