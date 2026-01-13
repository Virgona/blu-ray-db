def prompt_int(prompt: str) -> int:
    # Keeps asking the user to enter a valid int. Throws err on str
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a number.")


def choose_from_list(rows, title: str, label_fn):

    # displays a numbered list of items from the database. Depending which the user has chosen to see
    
    if not rows:
        raise RuntimeError(f"No options available for {title}.")

    print(f"\n{title}:")                        
    for idx, row in enumerate(rows, start=1):
        print(f"{idx}) {label_fn(row)}") # converts a row from the database into displayed text. e.g. 1. movieTitle

    while True:
        choice = prompt_int("Choose number: ")
        if 1 <= choice <= len(rows):
            return rows[choice - 1]
        print("Invalid choice. Try again.")