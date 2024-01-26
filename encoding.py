

def caesar_cipher(text, shift):
    ciphered_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                ciphered_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                ciphered_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            ciphered_text += char
    return ciphered_text


text = input("Enter the text to be encrypted: ")
shift = int(input("Enter the shift value: "))
ciphered_text = caesar_cipher(text, shift)
print("ciphered text is : "+ciphered_text)
