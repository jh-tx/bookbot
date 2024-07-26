print('--- Begin report of books/frankenstein.txt ---')

def sort_on(dict):
    return dict["num"]

def report():
    char_count = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().lower()
        for letter in file_contents:
            if letter.isalpha():  # Only count alphabetic characters
                if letter in char_count:
                    char_count[letter] += 1
                else:
                    char_count[letter] = 1

    # Convert the dictionary to a list of dictionaries
    char_list = []
    for char, num in char_count.items():
        char_list.append({"letter": char, "num": num})

    # Sort the list of dictionaries by the number of occurrences, in descending order
    char_list.sort(reverse=True, key=sort_on)

    print(char_list)  # For debugging purposes

    # Print the final report in the format specified
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{sum(char_count.values())} words found in the document")
    for item in char_list:
        print(f"The '{item['letter']}' character was found {item['num']} times")
    print("--- End report ---")

report()