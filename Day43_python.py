#Write a program that uses multithreading to perform tasks concurrently.
print ("\nSubi - Day 43 of #100DaysOfCode\n") 
print("\nprogram that uses multithreading to perform tasks concurrently\n")

import threading

def print_message(message):
    print(message)

messages = ["Hai", "Everyone", "This", "Is", "Subi"]

threads = []

for message in messages:
    thread = threading.Thread(target=print_message, args=(message,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished.")
