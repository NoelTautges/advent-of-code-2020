#!/usr/bin/env python3

def main():
    group_questions = set()
    count_sum = 0

    with open("06.txt") as questions_file:
        for line in questions_file:
            group_questions.update(line.strip())

            if line == "\n":
                count_sum += len(group_questions)
                group_questions.clear()
        
    print(f"Question count sum: {count_sum}")

if __name__ == "__main__":
    main()