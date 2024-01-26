
# Online Python - IDE, Editor, Compiler, Interpreter

def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract numbers from each line
    numbers = [int(line.split()[0]) for line in lines]

    # Find the maximum number to determine the pyramid height
    max_number = max(numbers)

    # Initialize a list to store words for each level of the pyramid
    pyramid = [[] for _ in range(max_number)]

    # Populate the pyramid with words
    for line in lines:
        num, word = line.split()
        pyramid[int(num) - 1].append(word)

    # Build the decoded message by selecting words from the pyramid
    decoded_message = ' '.join(' '.join(words) for words in pyramid)

    return decoded_message

# Example usage:
message_file = 'coding_qual_input.txt'
result = decode(message_file)
print(result)