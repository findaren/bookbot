from stats import print_report
import sys 

  
def main():
    if len(sys.argv) <= 1:
        print ("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    filename = sys.argv[1]
    print_report(filename)


main()
