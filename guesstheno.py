# its a random guess game made using random library which gave us the random int 
import random 

def guess(x):
    randomno = random.randint(1,x)
    guess = 0

    while guess!=randomno:
        guess = int(input(f"guess the number betweeen 1 and {x}:"))
        if guess<randomno:
            print("sorry guess again . its too low ")
        
        elif guess>randomno:
            print("sorry guess again . its to high ")
           
        
    
    print(f" yay you have guessed the number . its [{randomno}]")
    
x = int(input("type a number greater than 3 to guess between : "))
            
guess(x)
