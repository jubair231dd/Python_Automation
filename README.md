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
