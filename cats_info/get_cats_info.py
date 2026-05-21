"""
Expand a function that will read this file and return a list
of dictionaries containing information about each cat.

Args:
    path (str): a string with a path to file.

Returns:
    list[dict]: returns a list of dictionaries with cat info.
"""

def get_cats_info(path: str) -> list[dict]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []

            for line in file:
                try:
                    line = line.strip()
                    if not line:
                        continue
                    id, name, age = line.split(',')
                    cat_info = {
                        'cat_id': id,
                        'name': name,
                        'age': int(age)
                    }
                    cats_info.append(cat_info)

                except ValueError:
                    print(f"Warning: invalid line '{line}' skipped.")
                    continue

            return cats_info

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return []


cats_info_data = get_cats_info("cats_data.csv")

print("List of cats info:", cats_info_data)