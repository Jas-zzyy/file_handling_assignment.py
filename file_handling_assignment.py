
try:
    with open("my_file.txt", "w") as file:
        file.write("Hello, this is line 1.\n")
        file.write("12345\n")
        file.write("Another line with some text and numbers: 67890\n")
except FileNotFoundError:
    print("Error: File not found or cannot be created.")
except PermissionError:
    print("Error: Permission denied.")
    
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Content of my_file.txt:")
        print(content)
except FileNotFoundError:
    print("Error: File not found or cannot be opened.")
except PermissionError:
    print("Error: Permission denied.")

try:
    with open("my_file.txt", "a") as file:
        file.write("This line is appended.\n")
        file.write("98765\n")
        file.write("Appending more text and numbers: 54321\n")
except FileNotFoundError:
    print("Error: File not found or cannot be opened.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("Task completed.")
