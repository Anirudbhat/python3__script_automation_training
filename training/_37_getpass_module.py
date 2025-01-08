import getpass

# print(dir(getpass))

# getpass() function is used to get the password from the user. While getting the password this function ensures that the password is not displayed in the screen

pwd = getpass.getpass()

print(f"The input password is {pwd}")


#getuser() function is used to get user name. This function checks the environment variables LOGNAME, USER, LNAME & USERNAME, in order and returns the value of first non empty string

username = getpass.getuser()

print(f"Username = {username}")
