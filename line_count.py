# Imports
import os


# Solution find a. files in the directory, b. count the number of lines in each file, c. print the details with average
def line_count(path, extension):
    num_files = 0
    total_lines = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                num_files += 1
                filename = os.path.join(root, file)
                num_lines = sum(1 for _ in open(filename))
                total_lines.append(num_lines)
                print(filename, '\t', num_lines)

    print("\nNumber of files found: ", num_files)
    print("Total number of lines: ", sum(total_lines))
    print("Average lines per file: ", (sum(total_lines) / num_files))

    print("\n\nThank you for the opportunity")


if __name__ == "__main__":
    # Get the directory name and file extension
    directory = input("Enter the directory name: ")  # directory = "C://Users//VIJAYA//Desktop//test"
    file_extension = input("Enter the file extension: ")

    print("\nDirectory name: ", directory)
    if file_extension:
        print("File extension: ", file_extension)
    else:
        file_extension = '.txt'
        print("File extension: ", file_extension)
    print("\nFiles: ")
    line_count(directory, file_extension)
