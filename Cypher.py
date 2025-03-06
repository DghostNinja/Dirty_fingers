import base64
import urllib.parse

# ASCII art for the script
ascii_art = """
  ____            _               
 / ___|   _ _ __ | |__   ___ _ __ 
| |  | | | | '_ \| '_ \ / _ \ '__|
| |__| |_| | |_) | | | |  __/ |   
 \____\__, | .__/|_| |_|\___|_|   
      |___/|_|                 
         
~ iPsalmy
      
"""

print(ascii_art)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    
    return result

def vigenere_cipher(text, key, mode='encrypt'):
    result = []
    key = key.lower()
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('a')
            if mode == 'decrypt':
                shift = -shift
            
            shift_base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            result.append(char)
    
    return ''.join(result)

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

def url_encode(text):
    return urllib.parse.quote(text, safe='')

def url_decode(text):
    return urllib.parse.unquote(text)

def morse_encode(text):
    return ' '.join(MORSE_CODE_DICT[char.upper()] if char.upper() in MORSE_CODE_DICT else char for char in text)

def morse_decode(text):
    return ''.join(REVERSE_MORSE_CODE_DICT[char] if char in REVERSE_MORSE_CODE_DICT else char for char in text.split())

def get_valid_mode():
    while True:
        mode = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().lower()
        if mode in ['e', 'd']:
            return mode
        print("Invalid choice! Please enter 'E' for Encrypt or 'D' for Decrypt.")

def main():
    print("Choose the encoding method:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")
    print("3. Base64 Encoding")
    print("4. URL Encoding")
    print("5. Morse Code")

    choice = input("Enter your choice (1/2/3/4/5): ").strip()

    if choice == '1':
        shift = int(input("Enter the shift value: "))
        mode = get_valid_mode()
        text = input("Enter text: ")
        result = caesar_cipher(text, shift, mode='encrypt' if mode == 'e' else 'decrypt')
        print(f"Result: {result}")

    elif choice == '2':
        key = input("Enter the keyword: ").strip()
        mode = get_valid_mode()
        text = input("Enter text: ")
        result = vigenere_cipher(text, key, mode='encrypt' if mode == 'e' else 'decrypt')
        print(f"Result: {result}")

    elif choice == '3':
        mode = get_valid_mode()
        text = input("Enter text: ")
        result = base64_encode(text) if mode == 'e' else base64_decode(text)
        print(f"Result: {result}")

    elif choice == '4':
        mode = get_valid_mode()
        text = input("Enter text: ")
        result = url_encode(text) if mode == 'e' else url_decode(text)
        print(f"Result: {result}")

    elif choice == '5':
        mode = get_valid_mode()
        text = input("Enter text: ")
        result = morse_encode(text) if mode == 'e' else morse_decode(text)
        print(f"Result: {result}")

    else:
        print("Invalid choice! Please enter 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
