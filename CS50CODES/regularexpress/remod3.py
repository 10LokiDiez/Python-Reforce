import re

email = input("Enter your email address: ").strip()
"""
. ANY CHARACTER (COMODIN DE EXPRESION)
* 0 OR MORE REP (CIERRE ESTRELLA)
+ 1 OR MORE REP (CIERRE POSITIVO)
? 0 OR 1 REP
{m} m REP
{m,n} m-n REP
^ AT THE START
$ AT THE END
[abcde] CHARACTERS THAT WE WANT  [a-zA-Z]
[^@] ALL EXCEPT (COMPLEMENTING OR IN SPANISH EL COMPLEMENTO)
"""
"""
Just one back slash
#\\w word char... as well as numbers and underscore
#\\d decimal digit
#\\W not a word char
#\\D not a decimal digit
#\\s whitespace char
#\\S not a whitespace chat
"""
"""
()group
A|B or
WE COULD DO THIS (\\w|\\s) JUST ONE BACK SLASH
"""
"""
re.IGNORECASE CASE SENSITIVE FALSE
re.MULTILINE
re.DOTALL
"""


#raw string (r" \");
#todo menos arroba (r"[^@]");
if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|net|gov|org)$",email,re.IGNORECASE):
    print("VALID")
else:
    print("INVALID")