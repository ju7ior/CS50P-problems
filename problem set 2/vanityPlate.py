# Implement a program that prompts the user for a Vanity plate and 
# outputs if the input would be a valid plate or invalid.

def is_valid(s):
  # Must start with 2 letters , Max 6 chars min 2
  # NUmbers must be at the end and first number cannot be zero
  # NO punctuation
  if len(s) < 2 or len(s) > 6:
    return False
  if s.isalnum() == False:
    return False
  if s[:2].isalpha() == False:
    return False
  if sandwich_or_0(s) == False:
    return False
  return True

def sandwich_or_0(s):
  # Check if there are letters between numbers or if the first number is zero
  if s.isalpha():
    return True
  for i in range(len(s)-1):
    if s[i].isdigit() and s[i+1].isdigit():
      if s[i+1].isalpha():
        return False
    if s[i].isalpha() and s[i+1].isdigit():
      if s[i+1] == '0':
        return False
  return True

def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")

main()