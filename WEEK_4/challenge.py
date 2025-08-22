# 
with open("./WEEK_4/input.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a sample input file.\n")
    f.write("It contains multiple lines of text.\n")
    f.write("Each line will be processed by the script.\n")
    f.write("Good luck with the challenge!\n")

# Read the content of the file
with open("./WEEK_4/input.txt", "r") as f:
    content = f.read()
    
# Count the number of words
word_count = sum(len(line.split()) for line in content)
print("Number of words", word_count)

# Convert the content to uppercase
line_upper = [line.upper() for line in content]
print("Uppercase lines:", line_upper)

# Output the file
with open("./WEEK_4/output.txt", "") as f:
    # f.writelines(word_count)
    f.writelines(line_upper)
    