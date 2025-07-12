from flask import Flask

app = Flask(__name__)

# routes
@app.route("/") # decorator
def home():
    return "Hello world! I mean Home Page!"

if __name__ == "__main__":
    app.run()