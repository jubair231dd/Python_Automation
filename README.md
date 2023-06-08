# Python_Automation
Lists the materials and files I needed to learn the automation in Python.

For opening file and reading the file:


`file = open("file_name")` // pass the absolute `PATH` if the file is in another `dir`


`print(file.readlines())` //reads a single line each time and updates the next time


`print(file.read())` //reads to the end 


`file.close()` // close the file after opening 

For automatically closing the opened file in `terminal` use this :


`with open("health_check.py") as file:`


`   print(file.readline())`


For reading each line in the text file after making it `upper case`:


`with open("demo.txt") as file:`

`  for line in file:`

`     print(line.strip().upper())`
      
      
   for stripping the new line chracter after each line do this 
      
      
         `print(line.strip().upper()`
        
