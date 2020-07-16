
# 1. Create word_list
# 2. Choose a random word
# 3. Transform the word in a string like "*****"

# 4. Play 
#       - letter input from the player
#       - validate input from the player => IsAlpha
#       - check if input letter is in the chosen word
#           If YES, 
#               replace the "*" in the string with the chosen letter
#           If NO,
#               player looses one life and revert to asking player for a new input



# 5. All the items in 4. will repet as long as the word is still not found or the lifes are still available != 0

# Tests

# -----

# start finding index of e

# s = "mouse"
# animal_letter = s.find("s")
# print(animal_letter)
# exit()

# end finding index of e

# ------------------------------------------

# start replacing a string

# a_string = "aba"

# print("aba = " + a_string)

# a_string = a_string.replace("a", "b")

# print("a_string modificat = " + a_string)

# exit()

# end replacing a string

# -------------------------------------------

# start replace 3 rd element of the string

# old_string = "aba"
# string_list = list(old_string)
# string_list[2]="c"
# new_string = "".join(string_list)

# print("new string = " + new_string)


# exit()

# end replace 3 rd element of the string

# start set

# i = 5
# my_set = set()

# while i > 0:

#     set_element = input("Pls. enter set element: ")
#     my_set.add(set_element)
#     print(my_set)
#     i = i - 1

# exit()


# end set



# ----------------------------------------------

# end testst 

# ---------------------------------------------

# start functions 

import random


def random_choose(some_list):
    
    the_chosen_object = random.choice(some_list)
    return the_chosen_object

def length_of_something(some_list_2):
    length_of_the_object = len(some_list_2)
    return length_of_the_object

def mask_something(some_list_3):
    masked_object = length_of_something(some_list_3) * "*"
    return masked_object





# end functions




# ---------------------------------------------

# 1. Create word_list

my_set = set()

word_list = ["SUA", "Poland", "Germany", "Israel", "Ukraine", "France"]
#lenght_word_list = len(word_list)

lenght_word_list = length_of_something(word_list)


# 2. Choose a random word

#import random
#the_chosen_country = random.choice(word_list)

the_chosen_country = random_choose(word_list)
print(the_chosen_country)




#print("the chosen country [2] = " + str(the_chosen_country[2]))


lenght_chosen_country = length_of_something(the_chosen_country)
#print("length of the chosen country: " + str(lenght_chosen_country))



# 3. Transform the word in a string like "*****"

#mask_of_the_chosen_country = ""

#1mask_of_the_chosen_country = lenght_chosen_country * "*"

# for index in range(lenght_chosen_country):
#     mask_of_the_chosen_country = mask_of_the_chosen_country + "*"
#     #index = index + 1

mask_of_the_chosen_country = mask_something(the_chosen_country)

print("mask of the chosen country = " + mask_of_the_chosen_country)


# 4. Play 

i = 0

#print("chosen country [i] = " + the_chosen_country[i])

life = 3



while life > 0 and mask_of_the_chosen_country.count("*") > 0:

    take_one_life = True

    input_letter = input("Plese enter a letter: ")


    if input_letter in the_chosen_country: #the input letter is inside the chosen country

        input_letter_index = the_chosen_country.find(input_letter) #finding index of the input letter inside the chosen country
        #print("input_letter_index = " + str(input_letter_index))

        # start changing the mask ***** with input letters

        old_mask_of_the_chosen_country = mask_of_the_chosen_country
        string_list = list(old_mask_of_the_chosen_country)
        string_list[input_letter_index]=input_letter
        new_mask_of_the_chosen_country = "".join(string_list)

        print("the chosen country: " + new_mask_of_the_chosen_country)

        mask_of_the_chosen_country = new_mask_of_the_chosen_country



        # end changing the mask ***** with input letters

    else:
        # the input letter is not inside the chosen country

        # start check if the chosen letter was allready inserted


        for set_element in my_set:
            if set_element == input_letter:
                take_one_life = False
                print("You did allready try this wrong character ! I'll let you live this time !")

        my_set.add(input_letter)
        print(my_set)


        # end check if the chosen letter was allready inserted

        if take_one_life:
            life = life - 1
            print("You lost one life ! Still " + str(life) + " life(s) remaining !")
        
        

if mask_of_the_chosen_country.count("*") == 0:
            print(" *** You win !!! ***")
else:
    print(" *** You lost the game ! *** ")


