import collections, re

def get_keywords(path, max_kwrd):
    # with open('De Bangemann ao Plano Tecnológico .txt', 'r', encoding='UTF-8') as f:
    # Read the file given with 'path', using UTF-8 encoding
    with open(path, 'r', encoding='UTF-8') as f:
        text = f.read().lower()
    # Find all the strings of text in the file that contain at least 1 letter or digit
    regex = re.findall(r'\w+', text)
    # Create a Counter object for the regular expression matches, counting the total\
    # number of occurrences of the match in the text
    counter_obj = collections.Counter(regex)
    # Lastly return a list with the most 100 frequent matches that are at 3 characters long
    return ([word for word in counter_obj.most_common(max_kwrd) if len(word[0]) > 2])

if __name__ == "__main__":
    # file_path = input('Enter the file path: ').replace('\\', '\\', 10)
    file_path = input('Enter the file path: ')
    print(get_keywords(file_path, 100))
    # C:\Users\ze179\Desktop\De Bangemann ao Plano Tecnológico.txt