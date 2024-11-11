import os

# Function to get file names from user input
def get_file_names():
    file_names = []
    
    while True:
        file_name = input("Enter a file name (or type 'done' to finish): ")
        if file_name.lower() == 'done':
            break
        file_names.append(file_name)
    
    return file_names

# Function to save file names to a text file
def save_file_names(file_names, file_path='file_names.txt'):
    with open(file_path, 'a') as file:
        for name in file_names:
            file.write(f"{name}\n")
    print(f"New file names saved to {file_path}")

# Function to read and display previously saved file names
def display_previous_file_names(file_path='file_names.txt'):
    if os.path.exists(file_path):
        print("\nPreviously saved file names:")
        with open(file_path, 'r') as file:
            file_names = file.readlines()
            if file_names:
                for name in file_names:
                    print(name.strip())
            else:
                print("No file names have been saved yet.")
    else:
        print("No file names have been saved yet.")

# Main function to run the program
def main():
    display_previous_file_names()  # Display previously saved file names
    file_names = get_file_names()  # Get new file names from user
    save_file_names(file_names)    # Save new file names

if __name__ == "__main__":
    main()
