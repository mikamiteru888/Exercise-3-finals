def main():
    try:
        username = input("Enter Username: ")
        age = int(input("Enter Age: "))

        with open("users.txt", "a") as file:
            file.write(f"{username} - {age}\n")
        
        print("\nData saved successfully!")

        print("--- Saved Users ---")
        with open("users.txt", "r") as file:
            print(file.read())

    except ValueError:
        print("Error: Please enter a valid numerical age.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print("\nSystem complete.")

if __name__ == "__main__":
    main()
