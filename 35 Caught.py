import post_pulling
import post_reviewing
import posts_json_to_csv

def main():
    while True:
        print("1. Pull new posts")
        print("2. Review already pulled posts")
        print("3. Convert posts JSON to CSV")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            post_pulling.pull()
        elif choice == "2":
            post_reviewing.review()
        elif choice == "3":
            posts_json_to_csv.convert()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
    