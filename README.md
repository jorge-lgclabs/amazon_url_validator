# amazon_url_validator
Web endpoint which validates an Amazon product URL

Will validate URLs for Amazon products from any of the Amazon domains (.com, .co.uk, ect). Ignores any additional url parameters after the ASIN.

1. Run main.py, it will default to hosting on 127.0.0.1:5000 (port 5000)
2. make a POST request to '/validate' with the following parameters
   a. "Content-type" : "application/json" (if you you use python request module, using json will do this automatically)
   b. in the POST body should be: {"URL" : "[the URL you would like to validate]"}

3. It should return the following with a code 200
   If the URL is valid:
   {
     "status": "valid"
     "ASIN": "[the ASIN of the url]"
     "domain": "[the Amazon domain contained in the URL]"
   }

   If the URL is invalid:
   {
     "status": "invalid"
     "reason": "[the specific part of the URL that is invalid]"
   }

   These are the possible reasons for invalid:
   1. HTTP header is malformed
   2. The domain is invalid
   3. the product name is missing
   4. the '/dp/' is missing
   5. the ASIN is invalid
  
Examples:
1. Request: {"URL": "https://www.amazon.com/Anker-PowerCore-Portable-Charger-Compatible/dp/B09VPHVT2Z/"}
   Response: {"status": "valid", "ASIN": "B09vPHVT2Z", "domain": "amazon.com"}
2. Request: {"URL": "https://www.amazon.co.uk/Anker-PowerCore-Portable-Charger-Compatible/dp/B09VPHVT2Z/"}
   Response: {"status": "valid", "ASIN": "B09vPHVT2Z", "domain": "amazon.co.uk"}
3. Request: {"URL": "https://www.amaz0n.com/Anker-PowerCore-Portable-Charger-Compatible/dp/B09VPHVT2Z/"}
   Response: {"status": "invalid", "reason": "invalid domain"}
4. Request: {"URL": "https://www.amazon.com/Anker-PowerCore-Portable-Charger-Compatible/dp/B09VPHFVT2Z/"}
   Response: {"status": "invalid", "reason": "invalid ASIN/ISBN"}
  
[UML Diagram](diagram.png)

<img width="1864" height="1463" alt="image" src="https://github.com/user-attachments/assets/a6f23c67-0e41-47b7-a071-39fc915c5a53" />

   
