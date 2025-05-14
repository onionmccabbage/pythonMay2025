# we can use print just to send to a file
words = 'here is some important information'
file_obj = open('my_file.txt', 'at') # 'a' will append ('t' for text)
print(words, file=file_obj)