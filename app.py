from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>CI/CD Cloud Demo</h1><p>Application deployed successfully!</p>"

if __name__ == '__main__':
    app.run(debug=True)

