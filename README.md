# Python Automation
##### Lists the materials and files I needed to learn the automation in Python.

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
# working with basic `regular expressions`
```
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


Here is your output:
True
False
True

Great work! You've written your first regular expression!

```
# For ignoring case 
```
>>> print(re.search(r"Pan", "pantho panda pong", re.IGNORECASE))
<re.Match object; span=(0, 3), match='pan'>
```
# Wildcards and character classes
```
>>> import re
>>> text ="Python is a very user friendly language, I use python everyday"
>>> print(re.search(r"[Pp]ython", text))
<re.Match object; span=(0, 6), match='Python'>
```
```
>>> print(re.search(r"[a-zA-Z]way", "The end of highway"))
<re.Match object; span=(14, 18), match='hway'>
>>> print(re.search(r"[a-zA-Z]gh", "The end of highway"))
<re.Match object; span=(12, 15), match='igh'>
>>> print(re.search(r"[a-zA-Z]e", "The end of highway"))
<re.Match object; span=(1, 3), match='he'>
>>> print(re.search(r"[a-zA-Z]ay\d+", "The end of highway79y"))
<re.Match object; span=(15, 20), match='way79'>

>>> print(re.search(r"highway[a-zA-z0-9]", "the highway7890 is the best highway9908"))
<re.Match object; span=(4, 12), match='highway7'>

>>> print(re.search(r"highway[a-zA-z0-9]", "the highway7890 100 is the best highway9908"))
<re.Match object; span=(4, 12), match='highway7'>

>>> print(re.search(r"highway[a-zA-z0-9]", "the highwayCalifornia7890 100 is the best highway9908"))
<re.Match object; span=(4, 12), match='highwayC'>
>>> print(re.search(r"highway[a-zA-z0-9]+", "the highwayCalifornia7890 100 is the best highway9908"))
<re.Match object; span=(4, 25), match='highwayCalifornia7890'>

r"highway[a-zA-z0-9]+", "the highwaynowhere3447890asdada100 is the best highway9908"))
<re.Match object; span=(4, 34), match='highwaynowhere3447890asdada100'>


```

*Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.*

```
import re
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
```
*if you want to find the character that are not letter use this `r"[a-zA-Z ]+"`*
```
>>> print(re.search(r"[^a-zA-Z]", "The is highway 90: i love it"))
<re.Match object; span=(3, 4), match=' '>
>>> print(re.search(r"[^a-zA-Z ]", "The is highway 90: i love it"))
<re.Match object; span=(15, 16), match='9'>
>>> print(re.search(r"[^a-zA-Z ]+", "The is highway 90: i love it"))
<re.Match object; span=(15, 18), match='90:'>
```
# `re.findall() for finding all the matches
```

>>> print(re.findall(r"cat|dog", "I love cats and dogs"))
['cat', 'dog']

>>> print(re.findall(r"cat|dog", "I love cats and dogs. But sometimes cats make me sad"))
['cat', 'dog', 'cat']

>>> print(re.findall(r"[^a-zA-Z ]", "The is highway 90: i love it"))
['9', '0', ':']

>>> print(re.findall(r"[,./;@$%&]", "I love:there ,.;@#$%"))
[',', '.', ';', '@', '$', '%']
>>> print(re.findall(r"[^,./;@$%&]", "I love:there ,.;@#$%"))
['I', ' ', 'l', 'o', 'v', 'e', ':', 't', 'h', 'e', 'r', 'e', ' ', '#']

>>> print(re.findall(r"\d+", "I love:there 32 1 3 4 2 ,.;@#$%"))
['32', '1', '3', '4', '2']
>>> 


```

# Repetition Qualifiers
```
>>> print(re.search(r"py.*n", "python pygmalion pygramon")) // `.*` selects any character in between `py` and `n`
<re.Match object; span=(0, 25), match='python pygmalion pygramon'>

>>> print(re.search(r"py.*n", "python pygmalion py4345amon"))
<re.Match object; span=(0, 27), match='python pygmalion py4345amon'>

>>> print(re.search(r"py[a-z]*n", "python Programming"))
<re.Match object; span=(0, 6), match='python'>

>>> print(re.search(r"py[a-zA-Z]*n", "python Programming"))
<re.Match object; span=(0, 6), match='python'>
>>> print(re.search(r"py[a-zA-Z ]*n", "python Programming"))
<re.Match object; span=(0, 17), match='python Programmin'>
>>> 

>>> print(re.search(r"o+l+","whole whoolly holly"))
<re.Match object; span=(2, 4), match='ol'>
>>> print(re.search(r"o+l+","holly"))
<re.Match object; span=(1, 4), match='oll'>

import re
def repeating_letter_a(text):
  result = re.search(r"(?i)a.*a", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

>>> print(re.search(r"p?an", "an pen antho"))
<re.Match object; span=(0, 2), match='an'> // here `?` makes p optional


```
# Escape character
*using the scape character `\` to select `.\com`*
```
>>> print(re.search(r"\.com", "welcome"))
None

>>> print(re.search(r"\.com", "jubairpantho@gmail.com"))
<re.Match object; span=(18, 22), match='.com'>

```
*`\w` matches letters, numbers and underscores (alphanumeric character) 
```
>>> print(re.search(r"\w*", "jubairpantho@gmail.com"))
<re.Match object; span=(0, 12), match='jubairpantho'>
>>> print(re.search(r"\w*", "jubairpantho_gmail.com"))
<re.Ma
```
www.regex101.com 

``` 
>>> print(re.search(r"^A.*a$", "Alabamaanp"))// chooses only countries start with `A` and ends with `a`
None

>>> print(re.search(r"^A.*a$", "Australia"))
<re.Match object; span=(0, 9), match='Australia'>
```

*finding a valid variable name : *

```
>>> pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
>>> print(re.search(pattern, "_this_is highway 79"))
None
>>> print(re.search(pattern, "_this_is_highway_79"))
<re.Match object; span=(0, 19), match='_this_is_highway_79'>
```

*Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.

```
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
```

# Capturing groups 
```
>>> result = re.search(r"^(\w*), (\w*)$", "Jubair, Pantho")
>>> print(result)                                  
<re.Match object; span=(0, 14), match='Jubair, Pantho'>
>>> print(result.groups())
('Jubair', 'Pantho')
>>> print(result[0])
Jubair, Pantho
>>> print(result[1])
Jubair
>>> print(result[2])
Pantho
>>> "{} {}".format(result[2], result[1])
'Pantho Jubair'
```

```
import re
def rearrange_name(name):
  result = re.search(r"^(\w*), (\w.*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

Here is your output:
John F. Kennedy
```

*Repetition qualifiers
```
>>> print(re.search(r"[a-zA-Z]{5}", "a man was like ghost"))
<re.Match object; span=(15, 20), match='ghost'>
>>> 
```
*to find all the strings having length of five 
```
>>> print(re.findall(r"[a-zA-Z]{5}", "a man was like ghost and scary"))
['ghost', 'scary']

>>> print(re.findall(r"[a-zA-Z]{5}", "a man was like ghost and scary appeared "))
['ghost', 'scary', 'appea']
```
*to match exactly letters of length five use this
```
>>> print(re.findall(r"\b[a-zA-Z]{5}\b", "a man was like ghost and scary appeared "))
['ghost', 'scary']
```
*to find all the strings having length of five to ten 
```
>>> print(re.findall(r"\w{5,10}", "amar shonar bangla, ami tomai bhalobashi"))
['shonar', 'bangla', 'tomai', 'bhalobashi']
```
*to find all the strings having length of more than five 
```
>>> print(re.findall(r"\w{5,}", "amar shonar bangla, ami tomai bhalobashi omafagunetoramerbone"))
['shonar', 'bangla', 'tomai', 'bhalobashi', 'omafagunetoramerbone']
```
*to find all the words upto 20 characters long and starts with `s`
```
>>> print(re.findall(r"s\w{,20}", "I love strawberries and Bangladesh "))
['strawberries', 'sh']
```
*find the words that are at least 7 charcters long 
```
import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []
```
*getting `PID` from a log file 
```
>>> log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
>>> print(re.search(r"\[(\d+)\]", log))
<re.Match object; span=(39, 46), match='[12345]'>
>>> result = re.search(r"\[(\d+)\]", log)
>>> print(result)
<re.Match object; span=(39, 46), match='[12345]'>
>>> print(result[0[)
  File "<stdin>", line 1
    print(result[0[)
                   ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> print(result[0])
[12345]
>>> print(result[1])
12345
```
*fucntion for extracting a PID, if result is `None` it returns an empty string
```
>>> def extract_pid(log_line):
...     regex = r"\[(\d+)\]"
...     result = re.search(regex, log_line)
...     if result is None:
...             return ""
...     return result[1]
... 
>>> print(extract_pid("july [123444555]"))
123444555
>>> print(extract_pid("99 elephants in a [cage]"))

>>> 
```
*splitting and replacing
```
>>> re.split(r"[.?!]","One sentence ! second sentence. third senetence?")
['One sentence ', ' second sentence', ' third senetence', '']
>>> re.split(r"([.?!])","One sentence ! second sentence. third senetence?")
['One sentence ', '!', ' second sentence', '.', ' third senetence', '?', '']
>>> re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")
'Received an email for [REDACTED]'

>>> re.sub(r"^([\w.-]*), ([\w.-]*)$", r"\2 \1","Pantho, Jubair")
'Jubair Pantho'
>>> 
```

#Get the `environment` variable 
```
 env
TERM_PROGRAM=vscode
_P9K_TTY=/dev/ttys003
TERM=xterm-256color
S
```
*get the `PATH` variable
```
❯ echo $PATH
/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin:/usr/local/share/dotnet:/opt/X11/bin:~/.dotnet/tools:/Library/Apple/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Users/student/opt/anaconda3/bin:/Users/student/opt/anaconda3/condabin
❯ echo $DISPLAY
/private/tmp/com.apple.launchd.xbG9Rt7WPJ/org.xquartz:0
❯ echo $HOME
/Users/student
❯ echo $SHELL
/bin/zsh
❯ echo $FRUIT

❯ touch variables.py
❯ nano variables.py
❯ chmod +x variables.py
❯ ./variables.py
HOME: /Users/student
SHELL: /bin/zsh
FRUIT: 

//set the fruit variable to pineapple

❯ export FRUIT=Pineapple
❯ ./variables.py
HOME: /Users/student
SHELL: /bin/zsh
FRUIT: Pineapple

```
# Command line arguments are stored in the `sys` module
```
❯ touch parameters.py
❯ nano parameters.py
❯ cat parameters.py
#!/usr/bin/env python3

import sys
print(sys.argv)
❯ ./parameters.py
zsh: permission denied: ./parameters.py
❯ chmod +x parameters.py
❯ ./parameters.py
['./parameters.py']
❯ ./parameters.py one two three four
['./parameters.py', 'one', 'two', 'three', 'four']
```
# Exit status
```
`wc` counts the line word and character counts of a file.
❯ wc parameters.py
       4       5      51 parameters.py
❯ echo $?
0  //when returned zero that means ran successfully
❯ cat parameters.py
#!/usr/bin/env python3

import sys
print(sys.argv)
❯ wc notpresent.py
wc: notpresent.py: open: No such file or directory
❯ echo $?
1  // failed
```
# Running System Commands in Python
```
>>> import subprocess
>>> subprocess.run(["date"])
Tue Jun 13 16:48:31 EDT 2023
CompletedProcess(args=['date'], returncode=0)
>>> subprocess.run(["sleep"])
usage: sleep seconds
CompletedProcess(args=['sleep'], returncode=1)
>>> subprocess.run(["sleep"])
usage: sleep seconds
CompletedProcess(args=['sleep'], returncode=1)
>>> subprocess.run(["sleep", "5"])
CompletedProcess(args=['sleep', '5'], returncode=0)
>>> result = subprocess.run(["ls","this file does not exist"])
ls: this file does not exist: No such file or directory
>>> print(result.returncode)
1
```
# Obtaining the Output of a System Command
```
>>> import subprocess
>>> result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
>>> print(re
repr(     result    return    reversed(
>>> print(result.returncode)
0
>>> print(result.stdout)
b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
>>> print(result.stdout.decode().split())
['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']
>>>
```

```
>>> result = subprocess.run(["rm","does not exist"], capture_output = True)
>>> print(result.returncode)
1
>>> print(result.stderr)
b'rm: does not exist: No such file or directory\n'
>>> print(result.stderr.decode().split())
['rm:', 'does', 'not', 'exist:', 'No', 'such', 'file', 'or', 'directory']
>>>
>>> print(result.stdout)
b''
//stdout and stderr are totally different
```
```
>>> result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
>>> print(result.stdout)
b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
>>> print(result.stderr)
b''
```

# Terminating processes using the `kill` command 
```
❯ ping www.facebok.com
PING star.c10r.facebook.com (31.13.88.1): 56 data bytes
64 bytes from 31.13.88.1: icmp_seq=0 ttl=55 time=12.162 ms
64 bytes from 31.13.88.1: icmp_seq=1 ttl=55 time=12.514 ms
64 bytes from 31.13.88.1: icmp_seq=2 ttl=55 time=11.243 ms❯ ping 
```
*run this in a second terminal and `kill` , ps ax lists all the running processes, grep find the info related to the `ping`*

```
❯ ps ax | grep ping
55467 s003  S+     0:00.01 ping www.google.com
55471 s004  S+     0:00.00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn --exclude-dir=.idea --exclude-dir=.tox ping
❯ kill
kill: not enough arguments
❯ kill 55467
❯ kill 55471
kill: kill 55471 failed: no such process
❯ ps ax | grep ping
55536 s003  S+     0:00.01 ping www.facebok.com
55543 s004  S+     0:00.00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn --exclude-dir=.idea --exclude-dir=.tox ping
❯ kill 55536
```

*important note : control + c terminates the process, cntr + z stops the process which can be again inititated using the `fg` command.*

#Basic Linux Commands Cheat-Sheet
```
This list includes a bunch of different commands that are useful to know when working with Linux. Not all of these commands are covered in the videos, so feel free to investigate them on your own.

Managing files and directories
cd directory: changes the current working directory to the specified one

pwd: prints the current working directory

ls: lists the contents of the current directory

ls directory: lists the contents of the received directory  

ls -l: lists the additional information for the contents of the directory  

ls -a: lists all files, including those hidden  

ls -la: applies both the -l and the -a flags  

mkdir directory: creates the directory with the received name

rmdir directory: deletes the directory with the received name (if empty)

cp old_name new_name: copies old_name into new_name

mv old_name new_name: moves old_name into new_name

touch file_name: creates an empty file or updates the modified time if it exists

chmod modifiers files: changes the permissions for the files according to the provided modifiers; we've seen +x to make the file executable

chown user files: changes the owner of the files to the given user

chgrp group files: changes the group of the files to the given group

Operating with the content of files
cat file: shows the content of the file through standard output

wc file: counts the amount of characters, words, and lines in the given file; can also count the same values of whatever it receives via stdin

file file: prints the type of the given file, as recognized by the operating system

head file: shows the first 10 lines of the given file

tail file: shows the last 10 lines of the given file

less file: scrolls through the contents of the given file (press "q" to quit)

sort file: sorts the lines of the file alphabetically

cut -dseparator -ffields file: for each line in the given file, splits the line according to the given separator and prints the given fields (starting from 1)

Additional commands
echo "message": prints the message to standard output

date: prints the current date

who: prints the list of users currently logged into the computer

man command: shows the manual page of the given command; manual pages contain a lot of information explaining how to use each command (press "q" to quit)

uptime: shows how long the computer has been running

free: shows the amount of unused memory on the current system
``` 
