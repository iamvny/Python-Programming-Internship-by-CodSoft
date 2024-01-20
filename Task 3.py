import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        length = int(input("Enter the desired password length (default is 12): ") or 12)

        if length <= 0:
            print("Invalid length. Please enter a positive number.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")

        another = input("Generate another password? (yes/no): ").lower()
        if another != 'yes':
            print("Exiting Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
