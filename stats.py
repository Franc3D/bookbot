# Get a filepath and return the entire textof the book
def get_book_text(filepath):
    with open (filepath) as file:
    # Obtain the content of a file
        file_contents = file.read()
        # Turn the file contant into string
        return file_contents
        #return the text as string

def get_num_words(text):
    words = text.split()
    # Split the text into a list of words
    wordcount = len(words)
    # get the length of the list of words
    return wordcount
    # Print the number of words found in the document


def count_characters(text):
    # create a dictionnary to assign char to the nb counted
    count_list = {}
    # for every character in the text(transform upper case to lower case)
    for char in text.lower():
        # if char not already created, give it a numerical value (0) to then be able to += without error
        if char not in count_list:
            count_list[char] = 0
            # for each char add +1 tp the count value 
        count_list[char] += 1
    # return unformated list of characters and their count
    return count_list

def get_sorted_list(filepath):
    text = get_book_text(filepath)
    
    # Get the text of the book
    num_word = get_num_words(text)

    char_count = count_characters(text)
    #make a list of the numbers
    #turn the dictionnary into a list of dictionnaries
    char_dict_list = []
    for items in char_count.items():
        char_dict_list.append({"char": items[0], "num": items[1]})
    
    # THIS IS A DOOSY (it's stupid and I hate it)
    # key=lambda allows you to write a function that will be used to sort the list
    # in this case we sort the list by the value of the "num" key in the dictionary
    sorted_dict_list = sorted(char_dict_list, reverse=True, key=lambda item: item["num"])


#EXPLANATIONS FOR .SORT() (CONTINUATION)
    # Lambda prevents us from having to do an entire function to sort the list
    # since sort goes through a list line by line, the (item) in this case is the value of list[N] (similar to for item in items:)
    # the item["num"]  is the equivalent of list[N]["num"]
    #def sort_on(item):
    #    return item["num"]


    message = f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\n"
    message += f"Found {num_word} total words\n----------- Character Count -----------\n"
    


    # Loop through the sorted list and add each character and its count to the message
    # Only include alphabetic characters
    for item in sorted_dict_list:
        if item["char"].isalpha() == True:
            message += f"{item['char']}: {item['num']}\n"

    #Send the completed message    
    return message