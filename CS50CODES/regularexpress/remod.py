import re

email = input("Enter your email address: ").strip()
"""
. ANY CHARACTER (COMODIN DE EXPRESION)
* 0 OR MORE REP (CIERRE ESTRELLA)
+ 1 OR MORE REP (CIERRE POSITIVO)
? 0 OR 1 REP
{m} m REP
{m,n} m-n REP
"""
#raw string (r" \")
if re.search(".+@.+\\.edu",email):
    print("VALID")
else:
    print("INVALID")