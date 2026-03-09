
file_object = open('words.txt')  # the built-in function open, which takes the name of the file as a parameter and returns a file object we can use to read the file;

# The open() is a factory function that creates and returns a file object.

# The file_object becomes a file object. A file object is an object that represents an opened file and gives you methods to interact with it.

#  More formal definition: An abstraction over a file descriptor that provides high-level methods to perform buffered I/O operations.
# -> Abstraction → It hides low-level OS details.

# -> File descriptor → A number the OS uses to identify an opened file.

# -> Buffered I/O → It doesn’t always read/write directly to disk; it uses memory buffers for efficiency.

line = file_object.readline()

word = line.strip() # strip removes whitespace characters — including spaces, tabs, and newlines — from the beginning and end of the string.



def words():
    for line in open('words.txt'):
        word  = line.strip() # Why declare a local variable word again? Because the first word variable is based on the line variable which returns just the first line, because of the readline method
        print(word)   # Here is something to learn: If you put a print function, it returns all the words contained in the archive, but if you return it, it stops the for loop, because it ends the function. So the return vale is useful when you want after that decision have been taken the function finishes.
    


print(words())
def has_e(word):
    for letter in word:
        if letter == 'E' or letter == 'e':
            return True
    return False

