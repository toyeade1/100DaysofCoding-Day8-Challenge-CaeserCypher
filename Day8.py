# This program creates a ceaser cypher which essentially encodes a message with a sort of prefixxed algorithm.

from Day8logo import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text,shift):
    if direction == 'encode':
        cipher_text = []
        for letter in text:
            if letter in alphabet:
                cypher_letter = alphabet.index(letter) + shift
                cipher_text.append(alphabet[cypher_letter])
            else:
                cipher_text.append(letter)
        print(f"The encoded text is {''.join(cipher_text)}")
    elif direction == 'decode':
        cipher_text = []
        for letter in text:
            if letter in text:
                cypher_letter = alphabet.index(letter) - shift
                cipher_text.append(alphabet[cypher_letter])
            else:
                cipher_text.append(letter)
        print(f"The decoded text is {''.join(cipher_text)}")
    else:
        print('You typed the wrong word, you need to type either \'encode\' or \'decode\', please try again.')

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # this is put incase the user enters a number that is greater than the list, so the index is never out of range
    shift = shift % 26
    caeser(text,shift)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if go_again == 'no':
        should_continue = False
        print('Goodbye')
