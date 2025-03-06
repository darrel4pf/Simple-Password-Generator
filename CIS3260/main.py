# Main.py


from passwordgenerator import generatepassword, addexpiration, analyze_password_strength, generate_multiple_passwords
from filemanager import save_to_file, PasswordManager  


password_manager = PasswordManager()

def getuserpreference():
    
    #Collects user input for password preferences like length and character types.
    
    
    print("Welcome to the Password Generator!")
    try:
        # Get user input for password customization
        length = int(input("Enter password length (minimum 1): "))
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
        multiple_passwords = input("Generate multiple passwords? (yes/no): ").strip().lower() == 'yes'

        count = 1
        if multiple_passwords:
            count = int(input("How many passwords do you want to generate? "))

        # Get days for expiration
        days_valid = int(input("Enter number of days before password expires (e.g., 30): "))

        return {
            "length": length,
            "use_letters": use_letters,
            "use_numbers": use_numbers,
            "use_symbols": use_symbols,
            "days_valid": days_valid,
            "count": count
        }
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    
    #Main function to gather user preferences and generate passwords.
    
    preferences = getuserpreference()
    if preferences:
        if preferences["count"] > 1:
            # Generate multiple passwords
            passwords = generate_multiple_passwords(
                count=preferences["count"],
                length=preferences["length"],
                use_letters=preferences["use_letters"],
                use_numbers=preferences["use_numbers"],
                use_symbols=preferences["use_symbols"]
            )
            # Display multiple passwords
            print("\nGenerated Passwords:")
            for idx, pwd_data in enumerate(passwords, start=1):
                print(f"{idx}. Password: {pwd_data['password']} | Strength: {pwd_data['strength']}")
                # Update password history
                password_manager.update_password(pwd_data['password'])
        else:
            # Generate a single password
            password = generatepassword(
                length=preferences["length"],
                use_letters=preferences["use_letters"],
                use_numbers=preferences["use_numbers"],
                use_symbols=preferences["use_symbols"]
            )
            expiration = addexpiration(preferences["days_valid"])
            strength = analyze_password_strength(password)

            # Display the single password
            print("\nGenerated Password:")
            print(f"Password: {password}")
            print(f"Strength: {strength}")
            print(f"Expiration Date: {expiration.strftime('%Y-%m-%d %H:%M:%S')}\n")

            # Update password history
            password_manager.update_password(password)

        # Save-to-file option
        save_option = input("Do you want to save the generated password(s) to a file? (yes/no): ").strip().lower()
        if save_option == 'yes':
            history = "\n".join(password_manager.get_password_history())
            save_to_file(history)

        # Display password history
        print("\nPassword History:")
        for idx, past_password in enumerate(password_manager.get_password_history(), start=1):
            print(f"{idx}. {past_password}")

if __name__ == "__main__":
    main()
