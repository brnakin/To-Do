# Import necessary Flask modules for web application development,
# and import utility functions from generative_utils.
from flask import Flask, redirect, render_template, request, url_for
from generative_utils import util

# Initialize Flask app with the specified template folder for HTML templates.
app = Flask(__name__, template_folder="templates")


# Define a route for the index page which supports both GET and POST methods.
@app.route("/", methods=["GET", "POST"])
def index():
    """
    Serve the index page.

    If method is POST, it processes the form data to generate responses based on the utility function.
    If any exception occurs, it redirects the user to an error page.
    """
    try:
        # Check if the request method is POST to process form data.
        if request.method == "POST":
            # Retrieve 'prompt' from form data.
            prompt = request.form["prompt"]

            # Utilize the utility function to process the prompt and get necessary information.
            need_action, actions, action_time, advice, flag = util(prompt)

            # Render the index page with the results from the utility function.
            return render_template(
                "index.html",
                need_action=need_action,
                actions=actions,
                action_time=action_time,
                advice=advice,
                flag=flag,
            )
    except Exception as e:
        # In case of any exception, render an error page with a custom message.
        return render_template("error.html", error_message="Oops! Something Went Wrong")

    # For GET requests, simply render the index page without any context.
    return render_template("index.html")


# Define a route to catch any invalid paths and redirect them to the index page.
@app.route("/<path:invalid_path>")
def redirect_to_root(invalid_path):
    """
    Redirect any invalid URL paths to the index page.
    """
    return redirect(url_for("index"))


# Check if this script is executed as the main program and run the app in debug mode.
if __name__ == "__main__":
    app.run(debug=True)
