# Create a program that reads a file and writes a modified version to a new file.
with open("./WEEK_4/input.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a sample input file.\n")
    f.write("It contains multiple lines of text.\n")
    f.write("Each line will be processed by the script.\n")

with open("./WEEK_4/input.txt", "r") as f:
    content = f.readlines()

    # modify content
    contentm = content.pop(0)

# Output
with open("./WEEK_4/output.txt", "w") as f:
    f.write(contentm)

# Exception handling
file_name = input("Enter the file name: ")
def error_handling(file_name):
    try:
        with open(file_name, "r") as f:
            content = f.read()
            print("File content read successfully")
            return content
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist")
        return None