from flask import *
app = Flask(__name__)

with open("id.txt", "r") as f:
    ctn = f.readline(0)
    global GOOGLE_APPS_SCRIPT_ID
    GOOGLE_APPS_SCRIPT_ID = ctn

status = {
    "site": 0,
    "statistics": 0
}

@app.route("/")
def master():
    return render_template("index.html",
    site=status["site"])

@app.route("/bilet")
def bilet_redirect():
    return """
        <script>
            window.location.href = "../";
        </script>
    """

@app.route("/bilet/<ticket>")
def bilet(ticket):
    return render_template(
        "ticket.html", ticket=ticket,
        GOOGLE_APPS_SCRIPT_ID=GOOGLE_APPS_SCRIPT_ID,
        site=status["site"]
    )

@app.route("/istatistikler")
def istatistikler():
    return render_template(
        "statistics.html",
        GOOGLE_APPS_SCRIPT_ID=GOOGLE_APPS_SCRIPT_ID,
        statistics=status["statistics"]
    )

@app.errorhandler(404)
def not_found(err):
    return render_template("404.html", err=err)

if __name__ == "__main__":
    app.run()


