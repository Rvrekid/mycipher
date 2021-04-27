import sys 

def main(argv):
    print(sys.argv)
    line = sys.stdin.readline() 
    while line:
        print(line)
        line = sys.stdin.readline()

if __name__ == "__main__": 
    main(sys.argv)
