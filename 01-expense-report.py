#!/usr/bin/env python3

def main():
    expenses = {}
    totals = []

    with open("01.txt") as expense_report:
        for line in expense_report:
            expense = int(line)
            complement = 2020 - expense
            
            if (parts := expenses.get(complement, [])):
                middle = f" * {parts[1]}" if len(parts) == 2 else ""
                total = parts[0] * expense * (parts[1] if len(parts) == 2 else 1)
                print(f"{parts[0]}{middle} * {expense} = {total}")
                
                totals.append(len(parts))
                if sorted(totals) == [2, 3]:
                    break

            added_expenses = {expense: [expense]}
            for total, components in expenses.items():
                if len(components) < 2 and total < complement:
                    added_expenses[total + expense] = components + [expense]
            expenses.update(added_expenses)

if __name__ == "__main__":
    main()