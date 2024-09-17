from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    # Run Flask on a specific IP and port
    app.run(host='159.69.244.232', port=80, debug=True)
