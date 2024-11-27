import requests

domain = "(any domain here)"
headers = requests.get(domain).headers

if 'X-Frame-Options' in headers:
        print (domain + " NOT VUNERABLE FOR X-FRAME-OPTIONS aka click jacking")
else:
        print (domain + " VULNERABLE FOR X-FRAME-OPTIONS aka click jacking")

if 'Content-Security-Policy' in headers:
        print (domain + " NOT VULNERABLE FOR Content-Security-Policy")
else:
        print (domain + " VULNERABLE FOR Content-Security-Policy")

if 'X-Content-Type-Options' in headers:
        print (domain + " NOT VULNERABLE FOR X-Content-Type-Options")
else:
        print (domain + " VULNERABLE FOR X-Content-Type-Options")
if 'Referrer-Policy' in headers:
        print (domain + " NOT VULNERABLE FOR Referrer-Policy")
else:
        print (domain + " VULNERABLE FOR Referrer-Policy")

if 'Permissions-Policy' in headers:
        print (domain + " NOT VULNERABLE FOR Permissions-Policy")
else:
        print (domain + "VULNERABLE FOR Permissions-Policy")
