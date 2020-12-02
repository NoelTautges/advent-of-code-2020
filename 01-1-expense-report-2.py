#!/usr/bin/env python3

def main():
    expenses = set()

    with open("01.txt") as expense_report:
        for line in expense_report:
            expense = int(line)
            complement = 2020 - expense
            
            if complement in expenses:
                print(expense * complement)
                break

            expenses.add(expense)

if __name__ == "__main__":
    main()