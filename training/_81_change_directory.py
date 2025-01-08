#Changing directory

#Changing directory inside python script can be done using simple function chdir()
#But it is necessary to make sure that EXCEPTIONS that will raise during directory change are handled correctly.

import os

def main():
    req_path = input("Enter the path to change working directory: ")
    print("The current working directory is ", os.getcwd())
    try:
        os.chdir(req_path)
        print("Working directory is changed to ", req_path)
    except FileNotFoundError:
        print("Given path is not valid. Hence, working directory can't be changed")
    except NotADirectoryError:
        print("Given path is not a directory. Hence, working directory can't be changed")
    except PermissionError:
        print("Don't have access to the given path. Hence, working directory can't be changes")
    except Exception:
        print(e)
    return None

if __name__ == "__main__":
    main()
