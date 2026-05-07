# Cascading
for i in range(20):
    print(" " * i + "Hello World!")

# Growing
message = "Hello World!"
for i in range(1, len(message) + 1):
    print(message[:i])

# Wave
import time

for i in range(20):
    spaces = " " * (10 + int(10 * __import__('math').sin(i * 0.5)))
    print(spaces + "Hello World!")
    time.sleep(0.1)  # Adds animation delay

# Matrix-style
import random
import time

for _ in range(20):
    spaces = random.randint(0, 50)
    chars = random.choice(["Hello World!", "HELLO WORLD!", "HeLLo WoRLd!"])
    print(" " * spaces + chars)
    time.sleep(0.05)

# Exploding
message = "Hello World!"
center = 40

for i in range(15):
    left_spaces = center - i * 2
    if left_spaces < 0:
        left_spaces = 0
    print(" " * left_spaces + message + " " * (i * 4) + message)
    
for i in range(15, 0, -1):
    left_spaces = center - i * 2
    if left_spaces < 0:
        left_spaces = 0
    print(" " * left_spaces + message + " " * (i * 4) + message)