def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()    
        #print(file_contents)
        word_count = 0
        words = file_contents.split()
        for word in words:
            word_count += 1
        #print(word_count)
        low_text = file_contents.lower()
        #print(get_character_count(low_text))
        print_report(word_count, get_character_count(low_text))

def get_character_count(lowered_text):
    letter_count = {}
    for letter in lowered_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def dict_to_list(dict):
    temp_list=[]
    new_list=[]
    for key, value in dict.items():
        if key.isalpha():
            temp_list = [key, value]
            new_list.append(temp_list)
        else:
            pass
    sorted_list = sorted(new_list, reverse = True, key=lambda x: x[1])
    return sorted_list


def arrange_dict(letter_count):
    for i in letter_count:
        print(f"The '{i[0]}' character was found '{i[1]}' times")
    else:
        pass

def print_report(word_count, letter_count):
    print(" ")
    print("--- Begin Report of frankenstein.txt ---")
    print(" ")
    print(f"{word_count} words found in this document")
    print(" ")
    arrange_dict(dict_to_list(letter_count))
    print(" ")
    print("--- End Report ---")

main()