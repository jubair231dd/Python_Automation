# Python_Automation
Lists the materials and files I needed to learn the automation in Python.

For opening file and reading the file:
```
file = open("file_name") // pass the absolute `PATH` if the file is in another `dir`
print(file.readlines()) //reads a single line each time and updates the next time
print(file.read()) //reads to the end 
file.close() // close the file after opening
```
For automatically closing the opened file in `terminal` use this :
```
with open("health_check.py") as file:
        print(file.readline())
 ```
For reading each line in the text file after making it `upper case`:
```
with open("demo.txt") as file:
  for line in file:
      print(line.strip().upper())
 ```  
 For stripping the new line chracter after each line do this:   
`print(line.strip().upper()`
For storing the file contents in a list:
```
>>> file = open("demo.txt")
>>> lines = file.readlines()
>>> file.close()
>>> lines.sort()
>>> print(lines)
['\n', 'Georgia pulled me in, I asked to\n', 'Georgia, wrap me up in all your\n', 'I found you\n', 'I found you\n', 'I found you\n', 'I said, "I would never fall unless it\'s you I \n', 'I said, "I would never fall unless it\'s you I \n', 
```
For write in a file : 
```
>>> with open("demo.txt", "w") as file:
...     file.write("It is my favourite song")

"r" > read only mode
"w" > write only , overwrites the current content 
"a" > append the contents
"r+" > read - write mode
```
Working with the `os` module: 


For removing a file using the `os` module:
```
>>> import os
>>> os.remove("remove.txt")
```
For renaming a file:
```
>>> import os 
>>> os.rename("old_file", "new_file.txt")
```
Check whether a file exists or not using the `os` module:
```
>>> os.path.exists("rename1.txt")
True
>>> os.path.exists("rename.txt")
False
```
For getting the size and time of modification of a file using `os`:
```
>>> os.path.getsize("health_check.py")
376
>>> os.path.getmtime("health_check.py")
1686166960.7232504 // this is time stamp not the actual time

>>> import datetime 
>>> timestamp = os.path.getmtime("health_check.py")
>>> datetime.datetime.fromtimestamp(timestamp)
datetime.datetime(2023, 6, 7, 15, 42, 40, 723250) // this is used for getting the date and time it was created
```
For finding the `absolute path` of a file:
```
>>> os.path.abspath("demo.txt")
'/Users/student/Desktop/Courses/coursera_python_automate/demo.txt'
```
For getting the current working directory in python :
```

>>> import os
>>> print(os.getcwd())
/Users/student/Desktop/Courses/coursera_python_automate
```
```
>>> os.mkdir("new_dir")

>>> os.chdir("new_dir")
```
```
>>> os.rmdir("new_dir")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'new_dir'
```
```
>>> os.mkdir("new1")

>>> os.rmdir("new1")
>>> os.listdir()
[]
```
```

>>> os.mkdir("n1")
>>> os.mkdir("n2")
```
```
>>> os.listdir()
['n1', 'n2']
```

For listing all the files and directories inside a `dir`:
```
>>> dir = "coursera_python_automate"
>>> import os
>>> for name in os.listdir(dir):
...     fullname = os.path.join(dir, name)
...     if os.path.isdir(fullname):
...             print("{} is a directory".format(fullname))
...     else:
...             print("{} is a file".format(fullname))
... 
coursera_python_automate/hello_world.py is a file
coursera_python_automate/demo.txt is a file
coursera_python_automate/book.txt is a file
coursera_python_automate/areas.py is a file
coursera_python_automate/__init__.py is a file
coursera_python_automate/__pycache__ is a directory
coursera_python_automate/README.md is a file
coursera_python_automate/rename1.txt is a file
coursera_python_automate/new_dir is a directory
coursera_python_automate/health_check.py is a file
coursera_python_automate/sum.py is a file
coursera_python_automate/.git is a directory
```

