#Just a dumb python script to to create a shitload of lines of text. 

def createFile():
    inputs = input("Enter the text you would like to repeat:")
    lines = int(input("Number of lines:"))
    fileName = input("Output filename:")

    if not fileName.endswith('.txt'):
        fileName += '.txt'

    with open(fileName, 'w') as file:
        for _ in range(lines):
            file.write(inputs + '\n')

        fileNameOutput = f"\033[1;32m{fileName}\033[0m"  #make green bold text

        print(f"Successfully created {fileNameOutput}")

# Main
createFile()