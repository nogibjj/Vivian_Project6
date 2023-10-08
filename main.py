import sys
import argparse
from lib.query import test_query

def main():
    if args.action == "test_query":
        test_query(args.query)

    else:
        print(f"Unknown action: {args.action}")

if __name__ == "__main__":
    main()
