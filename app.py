from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def ussd():
    session_id = request.values.get("sessionId",None)
    servicecode =  request.values.get("serviceCode",None)
    phone_number = request.values.get("phoneNumber",None)
    text = request.values.get("text",None)

    if text == "":
        response = "CON What would you like to check?\n"
        response = "1. My Account\n"
        response = "2. My phone number\n"
    elif text == "1":
        response = "CON Choose a service that you require:\n"
        response = "1. My account number\n"
        response = "2. My account balance\n"
    else:
        response = "END Invalid choice"

    return response

if __name__ == "__main__":
    app.run(debug=True)
