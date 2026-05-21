"""
Develop a function that analyzes this file and returns
the total and average salary of all developers.

Args:
    path (str): a string with a path to file.

Returns:
    tuple: returns tuple with calculated total and average.
"""

def total_salary(path: str) -> tuple:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            developers_count = 0

            for line in file:
                try:
                    line = line.strip()
                    if not line:
                        continue
                    _, salary_string = line.split(',')
                    salary = float(salary_string)

                    total += salary
                    developers_count += 1

                except ValueError:
                    print(f"Warning: invalid line '{line}' skipped.")
                    continue

            if developers_count == 0:
                return 0, 0

            average = total / developers_count

            return total, average

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return 0, 0


total, average = total_salary("total_salary_data_t.csv")

print(f"Total salary: {total}, Average salary: {average}")

