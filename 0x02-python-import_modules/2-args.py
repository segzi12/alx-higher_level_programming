import sys

def print_arguments(argv):
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name
    print("Number of argument(s):", num_args, end="")
    if num_args == 0:
        print(".")
    else:
        print(":")
        for i in range(1, num_args + 1):
            print(i, ":", argv[i])

if __name__ == "__main__":
    print_arguments(sys.argv)
