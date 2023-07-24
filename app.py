from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<center>Hello Mahesh Finally you did it.</center>"
if __name__=="__main__":
    app.run()