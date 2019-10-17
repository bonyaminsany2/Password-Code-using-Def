#Johne Vang
#Group member Hlao Xiong
## P5.30
#  Check whether a password has the required properties.
#

def main() :
   # Read input from the user.
   password1 = input("Enter your password: ")
   password2 = input("Re-enter your password: ")

   # Keep looping until the passwords match and have the desired properties.
   while password1 != password2 or not isValidPassword(password1) :
      print("Passwords didn't match or didn't have the required properties.")

      # Read the next pair of passwords.
      password1 = input("Enter your password: ")
      password2 = input("Re-enter your password: ")

   # Display the final message.
   print("That pair of passwords will work.")

## Determine if a password has the desired properties: >=8 characters long, at
#  least one uppercase letter, at least one lowercase letter and at least one
#  digit.
#  @param password the password to check
#  @return True if all four properties are present, False otherwise
#
def isValidPassword(password) :
	hasDight = False
	hasLower = False
	hasUpper = False

	while len (password) >= 8:
		i = 0
		while i < len(password):
			if password[i].islower() and hasLower != True:
				hasLower = True
			if password[i].isdigit() and hasDight!= True:
				hasDight = True
			if password[i].isupper() and hasUpper!= True:
				hasUpper = True
			i = i + 1

		if hasUpper == True and hasDight == True and hasLower == True:
			return True
		else:
			return False

	return False
	

# Call the main function.
main()
