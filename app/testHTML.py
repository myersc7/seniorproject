from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():

    sprints = [1, 2, 3, 4]
    totalDiff = [50, 65, 80, 70]
    completeDiff = [0, 20, 33, 55]

    return render_template('projectNEW.html', sprints=sprints, totalDiff=totalDiff, completeDiff=completeDiff)

    #return render_template('Card.html')


if __name__ == "__main__":
    app.run(debug=True)