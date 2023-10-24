#Handle file-related exceptions while reading or writing files.
print ("\nSubi - Day 38 of #100DaysOfCode\n") 
print("\nHandle file-related exceptions while reading or writing files\n")

import os

def read_file(filename):
  
  try:
    with open("filename", "r") as file:
      content = file.read()
  except FileNotFoundError:
    print("File not found.")
  except PermissionError:
    print("Permission denied to access the file.")
  except Exception as e:
    print(f"An error occurred: {e}")

def write_file(filename, contents):

  try:
    with open("filename", "w") as file:
      file.write("hello")
  except PermissionError:
    print("Permission denied to access the file.")
  except Exception as e:
    print(f"An error occurred: {e}")


#Import and use the math library to perform mathematical operations.
print("\nImport and use the math library to perform mathematical operations\n")

import math

print(math.sin(math.pi/2))
print(math.cos(math.pi))
print(math.tan(math.pi/4))



