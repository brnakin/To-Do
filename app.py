from flask import Flask, redirect, render_template, request, url_for
from generative_utils import util

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method == "POST":
            prompt = request.form["prompt"]

            # Assuming util() function returns values or raises an exception if something goes wrong
            need_action, actions, action_time, advice, flag = util(prompt)
            return render_template(
                "index.html",
                need_action=need_action,
                actions=actions,
                action_time=action_time,
                advice=advice,
                flag=flag,
            )
    except Exception as e:
        render_template("error.html", error_message="Oops! Something Went Wrong")
        return

    return render_template("index.html")


@app.route("/<path:invalid_path>")
def redirect_to_root(invalid_path):
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
