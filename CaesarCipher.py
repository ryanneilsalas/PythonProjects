# def greet():
#     print("Hello")  
#     print("How do you do?")
#     print("Isn't the weather nice today")
# greet()
# def greet_with_name (name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Ryan")

#Functions with more than one input
# def greet_with(name,location) :
#     print(f"Hello  {name}")
#     location(f"What is it line in {location}")


# greet_with(name="Ryan",location="Maasin")
# Prime Checker 👇
# def prime_checker(number):
#   if number <=100 :
#     if number > 1:
    
#       for i in range(2, (number//2)+1):
        
#           if (number % i) == 0:
#               print("It's not a prime number.")
#               break
#       else:
#           print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
    
#   else:
#     print("The limit is 100")

# n = int(input()) # Check this number
# prime_checker(number=n)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text,shift,direction):
    output =""
    for word in text:
     if word in alphabet:
     
        cipher_text = alphabet.index(word)
        if direction == "encode":
          encoded_letter=alphabet[cipher_text+shift]
        else:
            encoded_letter=alphabet[(cipher_text+26)-shift]
        output += encoded_letter
     else:
         output += word
    print(f"The {direction}d text is {output}")

should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()  
    shift = int(input("Type the shift number:\n"))  
    shift = shift % 26
    if direction == "encode" or direction == "decode":
      caesar(text,shift,direction)
    else:
     print("Please type a valid option in direction")
     
    restart = input ("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

 
# Udemy solution
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode":
#       shift_amount *= -1
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     end_text += alphabet[new_position]
#   print(f"Here's the {direction}d result: {end_text}")


# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
 


    
