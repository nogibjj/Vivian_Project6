import sys
import argparse
from lib.query import test_query

def main():
    parser = argparse.ArgumentParser(description="ETL-Query script")
    args = parser.parse_args(sys.argv[1:])
    test_query(args)
    return 1  # Indicate success

if __name__ == "__main__":
    main()
