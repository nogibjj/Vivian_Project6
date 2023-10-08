import sys
import argparse
from lib.query import test_query

def handle_arguments():
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument("query", help="Query to be tested")

    return parser.parse_args()

def main():
    args = handle_arguments()
    test_query(args.query)
    return 1  # Indicate success

if __name__ == "__main__":
    sys.exit(main())
