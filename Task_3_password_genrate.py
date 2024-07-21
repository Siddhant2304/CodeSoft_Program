import random
import string

def generate_password(length, lowercase=True, uppercase=True, digits=True, punctuation=True):

  characters = ""
  if lowercase:
    characters += string.ascii_lowercase
  if uppercase:
    characters += string.ascii_uppercase
  if digits:
    characters += string.digits
  if punctuation:
    characters += string.punctuation


  if not characters:
    raise ValueError("At least one character type must be included (lowercase, uppercase, digits, punctuation)")
  

  password = ''.join(random.choices(characters, k=length))
  return password

while True:
  try:
    length = int(input("Enter desired password length (minimum 8 characters): "))
    if length < 8:
      print("Password length must be at least 8 characters. Please try again.")
    else:
      break
  except ValueError:
    print("Invalid input. Please enter a number.")

complexity_options = {
  "lowercase": "Include lowercase letters (y/n)? ",
  "uppercase": "Include uppercase letters (y/n)? ",
  "digits": "Include digits (y/n)? ",
  "punctuation": "Include punctuation characters (y/n)? ",
}

character_types = {}
for option, prompt in complexity_options.items():
  while True:
    response = input(prompt).lower()
    if response in ("y", "n"):
      character_types[option] = response == "y"
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'.")


password = generate_password(length, **character_types)
print(f"Your generated password is: {password}")
