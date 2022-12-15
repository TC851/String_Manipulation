from os.path import join


# A function to move string in an arbitrary way

def move(string):
    words = string.split(" ")
    tmp = " "

    for words in words:
        tmp += join(words[1:])
        tmp += words[0]
        tmp += "cb"

    return tmp[0:len(tmp) - 2]


# main -------------------------------------------------------------------
print(move("Python Chatbot 2.0"))
