from flask import Flask, request
import german_2000


app = Flask(__name__)

@app.route("/")
def get_random_sentence():
    return german_2000.get_random_sentence()

if __name__ == "__main__":
    app.run(debug=True)
