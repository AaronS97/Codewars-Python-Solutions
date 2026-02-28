### You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

## If the string's length is odd, return the middle character.
## If the string's length is even, return the middle 2 characters.


def get_middle(s):
    mid = len(s)//2
    print(s[mid]) if len(s) % 2 == 1 else print(s[mid-1:mid+1])

def main():
    s = input("String: ")
    get_middle(s)

if __name__ == '__main__':
    main()