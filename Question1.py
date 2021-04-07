from flask import Flask
import string
app = Flask(__name__)


@app.route("/<name>")
def generateResponse(name):
    temp = ""

    if name.isalpha():
        if name.isupper():
            return f"<h1>Welcome, {name.lower()}, to my CSCB20 website!</h1>"
            
        elif name.islower():
            return f"<h1>Welcome, {name.upper()}, to my CSCB20 website!</h1>"
    else:
        for a in name:
            if a.isalpha():
                temp = temp + a
        if temp != "":
            return f"<h1>Welcome, {temp}, to my CSCB20 website!</h1>"
        
    return f"<h1>Welcome, {name}, to my CSCB20 website!</h1>"


if __name__ == '__main__':
    app.run(debug=True)