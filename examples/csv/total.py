"""Sum the integer `amount` column from CSV on standard input."""
import csv
import sys

if __name__ == "__main__":
    print(sum(int(row["amount"]) for row in csv.DictReader(sys.stdin)))
