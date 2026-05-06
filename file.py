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
