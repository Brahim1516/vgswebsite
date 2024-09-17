from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == "__main__":
    # Set the host and port to make the app accessible on a specific IP and port
    app.run(host='159.69.244.232', port=8080, debug=True)
