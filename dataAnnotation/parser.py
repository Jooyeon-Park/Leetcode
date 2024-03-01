import os
print("Current Working Directory:", os.getcwd())

def parser():
    file_path = os.path.join(os.getcwd(), 'coding_qual_input.txt')
    with open(file_path, 'r') as file:
        lines = file.readlines()

    words = {}
    for line in lines:
        words[int(line.split(" ")[0])] = line.split(" ")[1]
    
    print(words)

    while()

parser()