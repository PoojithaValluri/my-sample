from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'python Developer',
        'location': 'Banglore',
        'salary': '10,00,000',
    },
    {
        'id': 2,
        'title': 'java Developer',
        'location': 'Hyd',
        'salary': '12,00,000',
    },
    {
        'id': 3,
        'title': 'mulesoft',
        'location': 'Hyd',
    },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
