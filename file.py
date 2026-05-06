'''Project Instructions
Implement a function called validate_name(), that takes in one parameter, which will be a datatype of string to check the user has inputted a valid name.

The function should check that the user has inputted a name that is a data type of string.
The function should check that the name is greater than two characters long.
The function should return a boolean value, True if the name is valid, and False if not.
Implement a function called validate_email(), that takes in one parameter, which will be a datatype of string to check the user has inputted a valid email.

The function should check that the user has inputted an email that contains an '@' symbol.
The function should check that the email contains any top-level domain included in the top_level_domains list variable. This has been preloaded to the workbook for you.
The function should return a boolean value,True if the name is valid, and False if not.'''
# Re-run this cell
# Preloaded data for validating email domain.
top_level_domains = [
    ".org",
    ".net",
    ".edu",
    ".ac",
    ".gov",
    ".com",
    ".io"
]
# 1: Create a function that validates the input name is a string and greater than 2 characters.

def validate_name(name):
    # Check that datatype of the variable, is what is expected. A string.
    if type(name) != str:
        return False   
    # Check if character is less than two characters, if so return false.
    elif len(name) <= 2: 
            return False
    # Name passed all checks
    else: 
        return True 
      
# 2: Create a function that validates the email is in the correct format.

def validate_email(email):
    # If the email does not include the @ symbol return False.
    if '@' not in email:
        return False     
    # Loop through domain string in the top_level_domains list.
    for domain in top_level_domains:
        # Check if the domain is included in the email.
        if domain in email:
        # If the domain is in the email, return a boolean with a value of True.
            return True
     # If code reaches this point, domain did not match, so return False to indicate invalid email 
    return False  