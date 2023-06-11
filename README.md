# Python_Automation
# Lists the materials and files I needed to learn the automation in Python.

# For opening file and reading the file:
```
file = open("file_name") // pass the absolute `PATH` if the file is in another `dir`
print(file.readlines()) //reads a single line each time and updates the next time
print(file.read()) //reads to the end 
file.close() // close the file after opening
```
# For automatically closing the opened file in `terminal` use this :
```
with open("health_check.py") as file:
        print(file.readline())
 ```
# For reading each line in the text file after making it `upper case`:
```
with open("demo.txt") as file:
  for line in file:
      print(line.strip().upper())
 ```  
# For stripping the new line chracter after each line do this:   
`print(line.strip().upper()`
# For storing the file contents in a list:
```
>>> file = open("demo.txt")
>>> lines = file.readlines()
>>> file.close()
>>> lines.sort()
>>> print(lines)
['\n', 'Georgia pulled me in, I asked to\n', 'Georgia, wrap me up in all your\n', 'I found you\n', 'I found you\n', 'I found you\n', 'I said, "I would never fall unless it\'s you I \n', 'I said, "I would never fall unless it\'s you I \n', 
```
# For write in a file : 
```
>>> with open("demo.txt", "w") as file:
...     file.write("It is my favourite song")

"r" > read only mode
"w" > write only , overwrites the current content 
"a" > append the contents
"r+" > read - write mode
```
# Working with the `os` module: 


# For removing a file using the `os` module:
```
>>> import os
>>> os.remove("remove.txt")
```
# For renaming a file:
```
>>> import os 
>>> os.rename("old_file", "new_file.txt")
```
# Check whether a file exists or not using the `os` module:
```
>>> os.path.exists("rename1.txt")
True
>>> os.path.exists("rename.txt")
False
```
# For getting the size and time of modification of a file using `os`:
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
# For finding the `absolute path` of a file:
```
>>> os.path.abspath("demo.txt")
'/Users/student/Desktop/Courses/coursera_python_automate/demo.txt'
```
# For getting the current working directory in python :
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

# For listing all the files and directories inside a `dir`:
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
# Working with `.csv` file:


# Read the csv file:
```
import csv
>>> f = open("hosts.csv")
>>> aws_f = csv.reader(f)
>>> for row in aws_f:
...     name, number = row 
...     print("name: {}, number: {}".format(name, number))
... 
name: Jamil, number: 0171233
name: nayeem, number: 0393993
```
# Generate the `csv` file: 
```
>>> import csv
>>> hosts = [["Jamil", "0171233"], ["nayeem", "0393993"]]
>>> with open('hosts.csv', 'w') as hosts_csv:
...     writer = csv.writer(hosts_csv)
...     writer.writerows(hosts) // writes all the rows, when writer.writerow used the only one rows are written


❯ ls
README.md       aws.xlsx        hello_world.py  hosts.csv
__init__.py     book.txt        homeprices.csv  new_dir
__pycache__     demo.txt        homeprices.txt  rename1.txt
areas.py        health_check.py homeprices1.csv sum.py
❯ cat hosts.csv
Jamil,0171233
nayeem,0393993
```
# Reading and writing `csv` file with `dictionaries` : 
### Reading:

```
❯ cat homeprices.csv
area,bedrooms,age,price
2600,3,20,550000
3000,4,15,565000
3200,,18,610000
3600,3,30,595000
4000,5,8,760000
4100,6,8,810000% 
```
```
>>> import csv
>>> with open("homeprices.csv") as homeprices:                  
...     reader = csv.DictReader(homeprices)                     
...     for row in reader:                                                 
...             print(("{} bedrooms price is {}").format(row["bedrooms"],row["price"]))
... 
3 bedrooms price is 550000
4 bedrooms price is 565000
 bedrooms price is 610000
3 bedrooms price is 595000
5 bedrooms price is 760000
6 bedrooms price is 810000 
```
### Writing:
```
>>> users = [{"name" : "jamil", "salary" : 2000}, {"name" : "kobbat", "salary" : 40000}]
>>> keys = ["name", "salary"]
>>> with open("employee.csv", "w") as employee:
...     writer = csv.DictWriter(employee, fieldnames = keys)
...     writer.writeheader()
...     writer.writerows(users)                                            
... 
13
>>> 
[26]  + 78509 suspended  python3
❯ cat employee.csv
name,salary
jamil,2000
kobbat,40000
```
# Working with `Regular Expression` 
```
>>> import re
>>> log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Perfuming package upgrade"
>>> regex = r"\[(\d+)\]"
>>> result = re.search(regex, log) 
>>> print(result)
<re.Match object; span=(39, 46), match='[12345]'>
>>> print(result[1])
12345
```
# Search using `grep` command in CLI: 
```
 grep me /Users/student/Desktop/Courses/coursera_python_automate/demo.txt
Georgia, wrap me up in all your beauty, You are an angleI 
```
```
❯ grep -i ar /Users/student/Desktop/Courses/coursera_python_automate/demo.txt
Georgia, wrap me up in all your beauty, You are an angleI 
// this selects strings of both upper and lower case if `-i` flag is used 
```
# For finding any character suppose are use `a.l` command as follows:
```
 grep a.l /Users/student/Desktop/Courses/coursera_python_automate/demo.txt
Georgia, wrap me up in all your beauty, You are an angleI 
```
# `^` to find words start with a specific word and `$` to find words end with a specific character
```
grep ^are /Users/student/Desktop/Courses/coursera_python_automate/demo.txt
❯ grep are$ /Users/student/Desktop/Courses/coursera_python
```
