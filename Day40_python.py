#Implement a decorator to measure the execution time of a function.
print ("\nSubi - Day 40 of #100DaysOfCode\n") 
print("\nImplement a decorator to measure the execution time of a function\n")

import time

def execution_time(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()

    print(f"Function {func.__name__} executed in {end_time - start_time} seconds")

    return result
  
  return wrapper

@execution_time

def calculate_multiply(x, y):
  
  return x * y

calculate_multiply(5, 10)