import re
url = input("Enter your URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(matches.group(1))