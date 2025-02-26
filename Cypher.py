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

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse shift for decryption

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-letters unchanged
    
    return result

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

def url_encode(text):
    return urllib.parse.quote(text, safe='')  # Encode all characters, including /, :, etc.

def url_decode(text):
    return urllib.parse.unquote(text)

def get_valid_mode():
    """Ensure the user enters 'E' or 'D'."""
    while True:
        mode = input("Do you want to Encrypt or Decrypt? (E/D): ").strip().lower()
        if mode in ['e', 'd']:
            return mode
        print("Invalid choice! Please enter 'E' for Encrypt or 'D' for Decrypt.")

def main():
    print("Choose the encoding method:")
    print("1. Caesar Cipher")
    print("2. Base64 Encoding")
    print("3. URL Encoding")
    
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == '1':  # Caesar Cipher
        shift = int(input("Enter the shift value: "))
        mode = get_valid_mode()
        
        text = input("Enter text: ")
        result = caesar_cipher(text, shift, mode='encrypt' if mode == 'e' else 'decrypt')
        print(f"Result: {result}")

    elif choice == '2':  # Base64
        mode = get_valid_mode()
        
        text = input("Enter text: ")
        result = base64_encode(text) if mode == 'e' else base64_decode(text)
        print(f"Result: {result}")

    elif choice == '3':  # URL Encoding
        mode = get_valid_mode()
        
        text = input("Enter text: ")
        result = url_encode(text) if mode == 'e' else url_decode(text)
        print(f"Result: {result}")

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
