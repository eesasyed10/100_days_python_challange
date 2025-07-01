alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

code_end=False

while not code_end==True:
    start=input("Type 'start' to start the code and type'end' to break the code:\n")
    if start != "start" and start != "end":
        print("You have entered the wrong input.")
    elif start=="start":


        correct_word=False


        while not correct_word:

            direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")).lower().strip()


            if direction != "encode" and direction !="decode" :
                print(f"You have entered the wrong input.")


            else:
                correct_word=True
        
        text = input("Type your message:\n").lower()


        shift = int(input("Type the shift number:\n"))

        #first I will create an input function


        if direction=="encode":


            def encrypt(original_text,shift_amount):


                cypher_text=""


                for letter in original_text:
                    if letter not in alphabet:
                        cypher_text+=letter


                    else:
                        shifted_amount=(alphabet.index(letter) + shift_amount)%26
                        number_to_text=alphabet[shifted_amount]
                        cypher_text+=number_to_text
                print(cypher_text)


            encrypt(text,shift)




        elif direction == "decode":
            def decrypt(original_text, shift_amount):
                cypher_text = ""
                for letter in original_text:
                    if letter not in alphabet:
                        cypher_text += letter
                    else:
                        shifted_amount = (alphabet.index(letter) - shift_amount) % 26
                        cypher_text += alphabet[shifted_amount]
                print(f"Decoded message: {cypher_text}")

            decrypt(text, shift)
    else:
        code_end=True
        print("Thanks for using my program.")
        break
