def encode(password):
    encoded_list = []
    for digit in password:
        number = int(digit)
        if number <= 6:
            number += 3
        else: 
            number -= 7
        encoded_list.append(str(number))
    encoded_string = ''.join(encoded_list)
    return encoded_string


# DONE BY JACK
def decode(password):
    deccoded = ""
    for char in password:
        if int <= 2:
            decoded += str(int(char) + 7)
            continue
        decoded += str(int(char) -3)
    return decoded

def menu():
    print("""Menu
-------------
1. Encode
2. Decode
3. Quit
""")

def main():
    while True:
        menu()
        menu_input = input('Please enter an option: ')
        if menu_input == '1':
            pass_input = input('Please enter the password to encode: ')
            encoded_pass = (encode(pass_input))
            print('Your password has been encoded and stored!')
        elif menu_input == '2':
            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.\n') 
        elif menu_input == '3':
            exit() 

if __name__ == "__main__":
    main()