import sys
import argparse
from lib.query import test_query

def handle_arguments(args):
    """add action based on inital calls"""
    parser = argparse.ArgumentParser(description="ETL-Query script")
    parser.add_argument(
        "action",
        choices=[
            "test_query"
        ],
    )
    args = parser.parse_args(args[:1])
    print(args.action)

    if args.action == "test_query":
        parser.add_argument("query")

    # parse again with ever
    return parser.parse_args(sys.argv[1:])

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
