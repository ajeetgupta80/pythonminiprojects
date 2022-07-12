# in this we gonna make mad libs game in python 
# by concatenation of strings 


# few ways to concatenate strings in python 
# youtuber = "ajeet gupta"
# print("subscribe to " + youtuber)
# print("subscribe to {} ".format(youtuber))
# print(f"subscribe to {youtuber}")


# defining variables
adj = input("adjective :")
verb = input("verb1: ")
verb2 = input("verb2: ")
famusperson = input("famus_person: ")

madlib = f"computer programming is so {adj}! it makes me so excited all the time because \
i love to {verb} stay hydrated and {verb2} like you are {famusperson}"

print(madlib)