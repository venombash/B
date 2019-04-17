# b_compile.py
# Ben Fellers 2019
# 
# For language B

import time
import random
import sys
import os

variables = {}
         
def main(file_name):
   #file_name = input("Enter path of file to be complied: ") # User enters the path of the script to be compiled
   with open(file_name, "r") as f:
      # we have opened the file to read
      for line in f:
         # we will read each line
         if "print" in line and "printvar" not in line and "@" not in line:
            # we have found the keyword print
            print(line[5:]) # prints the desired message
         elif "end" in line and "delay" in line and "@" not in line and "no_delay" not in line:  
            input("Press enter to exit...")
         elif "raw_input" in line and "@" not in line and "raw_input$" not in line:
            variables[line[10:11]] = input(line[12:])
            #print(variables)
         elif "raw_input$" in line and "@" not in line:
            variables[line[11:12]] = int(input(line[13:]))
            #print(variables)
         #elif "raw_input_int" in line and "@" not in line:
            #variables[line[14:15]] = int(input(line[16:]))
         elif "printvar" in line and "@" not in line:
            print(variables[line[9:10]])
         elif "var" in line and "int" in line and "@" not in line:
            variables[line[8:9]] = int(line[10:])
            #print(variables)
         elif "@" in line:
            continue 
         elif "var" in line and "float" in line and "@" not in line:
            variables[line[10:11]] = float(line[12:])
            #print(variables)
         elif "var" in line and "string" in line and "@" not in line:
            variables[line[11:12]] = str(line[13:])
            #print(variables)
         elif "end" in line and "no_delay" in line and "@" not in line:
            break
         elif "if" in line and "@" not in line:
            true_statment = f.readline()
            false_statement = f.readline()
            to_break = f.readline()
            var1 = variables[line[3:4]]
            var2 = variables[line[5:6]]
            #print(var1)
            #print(var2)
            if var1 == var2:
               #print(true_statment)
               if "return" in to_break:
                  print(true_statment)
                  time.sleep(2)
                  os._exit()
               else:
                  print(true_statment)
            else:
               print(false_statement)
         elif "yield" in line and "delay" in line and "@" not in line:
            time.sleep(line[10:])
         elif "var" in line and "bool" in line and "@" not in line:
            variables[line[9:10]] = bool(line[11:12])
            #print(variables)
         elif "var" in line and "rand" in line and "@" not in line:
            variables[line[9:10]] = random.randint(1, 10)
         elif "math" in line and "@" not in line:
            print(eval(line[5:]))
         elif "use" in line and "@" not in line:
            main(line[4:])
         elif "yield" in line and "command" in line and "@" not in line:
            os.system(line[14:])
         elif "read" in line and "@" not in line:
            file_to_read = open(line[5:], "r")
            print(file_to_read.read())
            file_to_read.close()
            input("Press enter to continue...")
            
file_name = input("Enter name of file to be compiled: ")
   
if __name__ == "__main__":
   main(file_name)
