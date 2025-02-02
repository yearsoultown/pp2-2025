#1st task
def ounce_to_gram(gram):
   return 28.3495231 * gram

grams = int(input())

print(ounce_to_gram(grams))

#2nd task
def far_to_cel(far):
   print(far, "Farenheits in Celcius = ", (5 / 9) * (far - 32))

farenheit = int(input())
far_to_cel(farenheit)

#3rd task We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
def rabbits_and_chickens(heads, legs):
   #x + y = 35
   #2x + 4y = 94

   y = (legs - 2 * heads)//2
   x = heads - y

   return x,y

total_heads = 35
total_legs = 94
chickens, rabbits = rabbits_and_chickens(total_heads, total_legs)

print(f"chickens are {chickens}")
print(f"rabbits are {rabbits}")

#4th task
num_list = [10,11,12,13,14,15,16,17,18,19]

def prime_numbers(numbers):
    primes = []
    for num in numbers:
        if filtering_primes(num):
            primes.append(num)
    return primes
            

def filtering_primes(n):
    if n < 2:
       return False
    for x in  range(2, n):
       if n % x == 0:
           return False
    return True
   

print(prime_numbers(num_list))

#5th task
def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        ch = s[i]  
        remaining = s[:i] + s[i+1:]  
        permute(remaining, answer + ch)  

user_input = input()
permute(user_input)

#6th task
def one_by_one(sentence):
    st_to_list = []
    string = ""
    for i in sentence:
        if i == " ":
            if string:
                st_to_list.append(string)
                string = ""
        else:
            string += i
            
    if string:
        st_to_list.append(string)
    return st_to_list

def reversed_list(sentence):
    words = one_by_one(sentence)
    words = words[::-1]
    
    reversed_string = ""
    for x in words:
        reversed_string += x
        reversed_string += " "
        
    return reversed_string
    
        
st = input()
print(reversed_list(st))

#7th task
def if_33(list):
    cnt = 0
    for x in list:
        if x == 3:
            cnt += 1
            if cnt == 2:
                break
        else:
            cnt = 0
    
    if cnt == 2:
        return True
    else:
        return False
    
has_33 = []
for x in range(6):
    num = int(input())
    has_33.append(num)
    
print(if_33(has_33))

#8th task

def spy_game(inserted_list):
    cnt = 0
    for i in inserted_list:
        if i == 0:
            cnt += 1
        elif i == 7 and cnt == 2:
            return True
        elif i == 7 and cnt != 2:
            return False
    
spy_list = []

for x in range(6):
    element = int(input())
    spy_list.append(element)
    
print(spy_list)

print(spy_game(spy_list))

#9th task
import math

def sph_volume(r, pi):
    V = (4/3)*p*r**3
    return (V)

radius = int(input())
p = math.pi

print(sph_volume(radius, p))

#10th task
duplicates_list = []

for i in range(10):
    x = int(input())
    duplicates_list.append(x)
    
def filtering_uniques(dup_list):
    uniques_list = []
    for i in dup_list:
        if i not in uniques_list:
            uniques_list.append(i)
            
    return uniques_list

print(filtering_uniques(duplicates_list))

#11th task
palindrome = input()

def checking(plndr):
    return palindrome == palindrome[::-1]

print(checking(palindrome))

#12th task
histogram_list = []

for i in range(3):
    x = int(input())
    histogram_list.append(x)
    
def changing_to_ast(h_list):
    new_list = []
    for i in h_list:
        new_list.append("*" * i)
            
        
    for x in new_list:
        print(x)

changing_to_ast(histogram_list)

#13th task
import random

print("Hello, What is your name?")
name = input()
print("Well,", name + ",", "I am thinking of a number between 1 and 20\nTake a guess")

x = random.randint(1, 20)

def guessing(rand, name):
    guess = int(input())
    word = "Take a guess."
    for i in range(1, 21):
        if guess == rand:
            print("Good job,", name + "!", "You guessed my number in", i, "guesses!")
            break
        elif guess < rand:    
            print("Your guess is too low", "\n", word)
            guess = int(input())
        else:
            print("Your guess is too high", "\n", word)
            guess = int(input())

guessing(x, name)

#14th task
print("python file created successfully!")