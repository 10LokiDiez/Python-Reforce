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
#raw string (r" \");
#todo menos arroba (r"[^@]");
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.edu$",email):
    print("VALID")
else:
    print("INVALID")