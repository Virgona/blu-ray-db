from movies import add_movie, list_movies, list_boutique_movies  # importing all our functions to keep it clean


def main_menu():
    while True:
        print("\n=== Blu-ray Collection ===")
        print("1) Add a movie")
        print("2) List all movies")
        print("3) List boutique movies")
        print("4) Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_movie()
        elif choice == "2":
            list_movies()
        elif choice == "3":
            list_boutique_movies()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main_menu()