alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("type encode for encription and type decode for decrption :")
text = input("enter the text ").lower()
shift = int(input("how many shifts you want:"))

def encript(text,shift):
    cipher_text = ""
    for letter in text:
     position =alphabet.index(letter)
     new_position = shift + position
     new_letter = alphabet[new_position]
     cipher_text+=new_letter
    print(f"the encoded text is {cipher_text}")   

def decript(cipher,shift_num):
    caeser_text = ""
    for letter in cipher:
      position = alphabet.index(letter)
      new_position =position-shift_num
      new_letter = alphabet[new_position]
      cipher+=new_letter
    print(f"the decoded text is {caeser_text}")
  
if(direction == "encode"):
   encript(text,shift)
else:
   decript(text,shift)   
   
  

