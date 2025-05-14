# we can use print just to send to a file
words = 'here is some important information'

# all I/O bound operations make requests to the Operating System to do the actual work
# this is a file access object - a means through which we access files
file_obj = open('my_file.txt', 'at') # 'a' will append ('t' for text)
print(words, file=file_obj)