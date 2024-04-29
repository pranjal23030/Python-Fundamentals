# with open("C:\\Users\\Dell\\PycharmProjects\\pythonProject\\pythonFundamentals\\file_Handling\\file_handling_practice"
#           "\\test.txt", "r") as fr:
#     result = fr.read()
#     print(result)

def countTokens():
    with open("test.txt", 'r') as file:
        content = file.read()
        spaces = content.count(' ')

        words = content.split()
        word_count = len(words)

        return spaces, word_count


spaces, word_count = countTokens()
print(f"Spaces: {spaces}, Word Count: {word_count}")
