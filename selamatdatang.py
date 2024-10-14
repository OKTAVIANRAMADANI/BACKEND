from flask import Flask
app = Flask(__name__)
app.config["DEGUG"] = True

@app.route('/')
def home():
    return 'Selamat Datang'

app.run()