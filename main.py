
#IMPORT THE stats.py FILE CODE TO WORK IN MAIN.PY
from stats import get_sorted_list
import sys


    
def main():
   
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        # catch if the file can be opened 
        try:
            with open(book, 'r') as file:
                pass  # Just to check if the file can be opened
        except FileNotFoundError:
            print(f"Error: The file '{book}' does not exist.")
            sys.exit(1)
        
    
        # Get the string for the sorted list
        print(get_sorted_list(book))

main()