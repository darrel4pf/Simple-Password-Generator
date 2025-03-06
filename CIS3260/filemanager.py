# Save-to-file feature
def save_to_file(data, filename="passwords.txt"):

    # - data : The data to save.
#- filename : The file name to save the data in.

    
    with open(filename, 'w') as file:
        file.write(data)
    print(f"Data saved to {filename}")


class PasswordManager:
    
    #Manages password history for the current session.
    #Prevents reusing old passwords and limits the history size to 5 entries.
    def __init__(self):
        self.password_history = []

    def update_password(self, new_password):

        
        #new_password : The password being added

        if new_password in self.password_history:
            print("Password cannot be reused.")
            return False
        self.password_history.append(new_password)
        # Limit history to the last 5 passwords
        if len(self.password_history) > 5:
            self.password_history.pop(0)
        print("Password updated successfully.")
        return True

    def get_password_history(self):
    
       #Retrieves the password history

        return self.password_history