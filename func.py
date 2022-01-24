from termcolor import colored
import sys

def httperror_assess(e):        
    if e in [x for x in range(400, 499)]:
        print(colored(f"Client Error {e}. Please try again later."), "red")
    
    elif e in [x for x in range(500, 599)]:
        print(colored(f"Server Error {e}. Please try again later."), "red")
    
    else:
        print(colored(f"An error occured with status number of {e}"), "red")
    
    sys.exit()        
