def prompt_int(prompt: str) -> int:
    # Keeps asking the user to enter a valid int. Throws err on str
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a number.")


def choose_from_list(rows, title: str, label_fn):
    # ----------------------------------------
    # Generic chooser for a list of DB rows.
    # rows: list of tuples (e.g. (id, name, type))
    # label_fn: function(row)->str to show each row
    # Returns: chosen row (tuple)
    # ----------------------------------------
    if not rows:
        raise RuntimeError(f"No options available for {title}.")

    print(f"\n{title}:")
    for idx, row in enumerate(rows, start=1):
        print(f"{idx}) {label_fn(row)}")

    while True:
        choice = prompt_int("Choose number: ")
        if 1 <= choice <= len(rows):
            return rows[choice - 1]
        print("Invalid choice. Try again.")