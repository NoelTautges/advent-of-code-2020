#!/usr/bin/env python3

def main():
    expenses = {}

    with open("01.txt") as expense_report:
        for line in expense_report:
            expense = int(line)
            complement = 2020 - expense
            
            if (pair := expenses.get(complement, [])) and len(pair) == 2:
                print(f"{pair[0]} * {pair[1]} * {expense} = {pair[0] * pair[1] * expense}")
                break

            added_expenses = {expense: [expense]}
            for total, components in expenses.items():
                if len(components) < 2 and total < complement:
                    added_expenses[total + expense] = components + [expense]
            expenses.update(added_expenses)

if __name__ == "__main__":
    main()