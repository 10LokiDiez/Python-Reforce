import re

name = input("Whats your name? ").strip()
matches = re.search(r"^(.+), *(.+)$")
if matches:
    #          grupos de parentesis
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")