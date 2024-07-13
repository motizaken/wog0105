from flask import Flask

app = Flask(__name__)

def read_score():
    with open("scores.txt", 'r') as file:
        return file.read()

@app.route("/")
def hello_world():
    score = read_score()
    return f"""
    <html>
        <head>
            <title>Score Game</title>
        </head>
        <body>
            <h1>The score is:</h1>
            <div id="score"> {score} </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(port=5000)