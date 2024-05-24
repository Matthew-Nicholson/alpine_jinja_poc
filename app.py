from flask import Flask, render_template, request

app = Flask(__name__)

planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
    "Pluto",
]


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        # Handle the post request here
        selected_planet = request.form.get("planet")
        print(f"Selected planet: {selected_planet}")
    return render_template("index.jinja", planets=planets)


if __name__ == "__main__":
    app.run(debug=True)
