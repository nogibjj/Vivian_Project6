import argparse
from lib.query import test_query

def main():
    args = handle_arguments(sys.argv[1:])
    if args.action == "test_query":
        test_query(args.query)
        return 1

    else:
        print(f"Unknown action: {args.action}")
        return -1

if __name__ == "__main__":
    main()
