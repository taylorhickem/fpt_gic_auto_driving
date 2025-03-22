import sys


def main():
    args = sys.argv[1:]
    if not args:
        print("Welcome to Crash CLI! Use 'crash start' or 'crash exit'.")
    elif args[0] == 'start':
        print("Welcome to Crash! Auto car simulation program")
    elif args[0] == "exit":
        print('Exiting... Goodbye!')
    else:
        print(f'ERROR. Unknown command: {args[0]}')