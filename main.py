import sys
import argparse
from lib.query import test_query

def handle_arguments():
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument("action", choices=["test_query"])

    args = parser.parse_args()

    if args.action == "test_query":
        parser.add_argument("query")
        args = parser.parse_args()  # Parse again to include the 'query' argument

    return args

def main():
    args = handle_arguments()

    if args.action == "test_query":
        if hasattr(args, 'query'):
            test_query(args.query)
            return 0  # Indicate success
        else:
            print("Error: 'query' argument is required for 'test_query' action.")
            return -1

    # This block is technically not needed since argparse will handle invalid choices
    # But it's kept here for clarity
    else:
        print(f"Unknown action: {args.action}")
        return -1

if __name__ == "__main__":
    sys.exit(main())
