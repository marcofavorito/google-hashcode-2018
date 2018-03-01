import sys

from src.Input import Input


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        input_obj = Input(*f.readline().split(" "))
    print(input_obj)



if __name__ == '__main__':
    main()