from flask import Flask, render_template

app = Flask(__name__)

# This acts as our database for the Goldilocks prototype
# Each key is a floor number, containing details about that specific goal
tower_data = {
    1: {"subject": "Chemistry", "progress": 47, "status": "In Progress"},
    2: {"subject": "Programming", "progress": 15, "status": "Locked"},
    3: {"subject": "Fitness", "progress": 80, "status": "Active"},
}

@app.route('/')
def index():
    # This renders the HTML file located in your 'templates' folder
    return render_template('index.html', floors=tower_data)

if __name__ == '__main__':
    # Setting debug=True allows the app to refresh automatically when you change code
    app.run(debug=True)