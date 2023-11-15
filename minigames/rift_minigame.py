import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def display_key_map(shift):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    decrypted_chars = [chr((ord(char) - shift) % 256) for char in all_chars]

    key_map = dict(zip(all_chars, decrypted_chars))

    print("Key Map:")
    for encrypted, decrypted in key_map.items():
        print(f"{encrypted} -> {decrypted}")

    return key_map

# Step 1: Generate a random password
server_password = generate_password(15)  # Adjust the length as needed

# Step 2: Encrypt the password
shift_value = 5  # You can adjust this for difficulty
encrypted_password = encrypt(server_password, shift_value)

# Step 3: Display the key map
key_map = display_key_map(shift_value)

# Step 4: Present the challenge
print("\nYou need to decrypt the following password to access the server:")
print(encrypted_password)

# Step 5: User input and decryption attempt
user_attempt = input("\nEnter your decryption attempt: ")
decrypted_attempt = ''.join(key_map.get(char, char) for char in user_attempt)

# Step 6: Check for success
if decrypted_attempt == server_password:
    print("Access granted! You successfully decrypted the password.")
else:
    print("Access denied. Incorrect decryption attempt.")