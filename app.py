from flask import Flask, redirect, render_template, request, url_for
from generative_utils import util


app = Flask(__name__, template_folder="templates")


# My existing route for "/"
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form["prompt"]

        try:
            need_action, actions, action_time, advice = util(prompt)
            return render_template(
                "index.html",
                need_action=need_action,
                actions=actions,
                action_time=action_time,
                advice=advice,
            )

        except ValueError:
            return render_template(
                "error.html",
                error_message="Request blocked due to harmful content.",
            )

    return render_template("index.html")


# Additional route to handle other endpoints
@app.route("/<path:invalid_path>")
def redirect_to_root(invalid_path):
    return redirect(url_for("index"))


# Entry point for script execution
if __name__ == "__main__":
    app.run(debug=True)
