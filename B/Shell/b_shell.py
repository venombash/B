# b_shell.py
# Ben Fellers 2019
# For B language

import os
import random

variables = {}

def compile_script(file_name):
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
            compile_script(line[4:])
         elif "yield" in line and "command" in line and "@" not in line:
            os.system(line[14:])
         elif "read" in line and "@" not in line:
            file_to_read = open(line[5:], "r")
            print(file_to_read.read())
            file_to_read.close()
            input("Press enter to continue...")

def main():
   while True:
      command = input("> ")
      if "print" in command and "printvar" not in command:
         print(command[6:])
      elif command == "exit":
         exit()
      elif "raw_input" in command and "raw_input$" not in command:
         variables[command[10:11]] = input(command[12:])
         #print(variables)
      elif "printvar" in command:
         print(variables[command[9:10]])
      elif "raw_input$" in command:
         variables[command[11:12]] = int(input(command[13:]))
         #print(variables)
      elif "yield" in command and "command" in command:
         os.system(command[14:])
      elif "var" in command and "int" in command:
         variables[command[8:9]] = int(command[10:])
         #print(variables)
      elif "var" in command and "float" in command:
         variables[command[10:11]] = float(command[12:])
      elif "var" in command and "string" in command:
         variables[command[11:12]] = str(command[13:])
      elif "var" in command and "bool" in command:
         variables[command[9:10]] = bool(command[11:])
      elif "var" in command and "rand" in command:
         variables[command[9:10]] = random.randint(1, 10)
      elif "math" in command:
         print(eval(command[5:]))
      elif "use" in command:
         compile_script(command[4:])
      elif "read" in command:
         file_to_read = open(command[5:], "r")
         print(file_to_read.read())
         file_to_read.close()
         input("Press enter to continue...")
      elif command == "help":
         print("""
         print - Prints a string | print Hello World!
         raw_input - Grabs the users answer and stores it in a variable | raw_input v What's your name?: 
         printvar - Prints a variable | printvar v
         raw_input$ - Grabs the users answer and stores it as a integer | raw_input$ i Enter number: 
         yield command - Runs a command in the CMD / Terminal | yield command echo "Hello World!"
         var (int, float, string, bool, rand) - Creates a variable | var int a 1
         math - Calculates a math expression | math 1 + 1
         use - Runs a .b script | use /B_Scripts/hello_world.b
         read - Reads a file | read /B/Compiler/b_compile.py
         exit - Exits the shell
         """
         )
      else:
         print("Command %s not found" % (command))
         
if __name__ == "__main__":
   try:
      os.system("title Shell")
   except:
      print("running on linux/mac name change fail...")
   print("""
   B Shell
   Ben Fellers 2019
   V 1.0.0
   """
   )
   main()