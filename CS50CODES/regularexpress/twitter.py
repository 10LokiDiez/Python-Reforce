import re
url = input("Enter your URL: ").strip()


username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(username)