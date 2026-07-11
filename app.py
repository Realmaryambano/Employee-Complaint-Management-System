from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Needed later for sessions/authentication
app.secret_key = "ecms_secret_key_2026"
# ==========================
# Login Page
# ==========================

@app.route("/", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]


        # Temporary Demo Authentication
        # IT Admin

        if username == "admin@bonanza.com" and password == "admin123":

            return redirect(url_for("it_dashboard"))



        # Employee

        elif username == "employee@bonanza.com" and password == "12345":

            return redirect(url_for("employee_dashboard"))



        else:

            error = "Invalid email or password"



    return render_template(
        "login.html",
        error=error
    )


# ==========================
# IT Support
# ==========================

@app.route("/it-support")
def it_support():

    return render_template("it_support.html")


# ==========================
# Employee Dashboard
# ==========================

@app.route("/employee-dashboard")
def employee_dashboard():

    return render_template("employee_dashboard.html")

# ==========================
# Complaint Form
# ==========================

@app.route("/complaint-form", methods=["GET", "POST"])
def complaint_form():

    if request.method == "POST":

        # Later:
        # Save complaint into Oracle Database

        pass


    return render_template("complaint_form.html")

# ==========================
# My Complaints
# ==========================

@app.route("/my-complaints")
def my_complaints():

    return render_template("my_complaints.html")

# ==========================
# IT Dashboard
# ==========================

@app.route("/it-dashboard")
def it_dashboard():

    return render_template("it_dashboard.html")

# ==========================
# Complaint Details
# ==========================

@app.route("/complaint-details", methods=["GET", "POST"])
def complaint_details():

    if request.method == "POST":

        # Later:
        # Update complaint status
        # Save remarks

        pass


    return render_template("complaint_details.html")

# ==========================
# 404 Error Page
# ==========================

@app.errorhandler(404)
def page_not_found(error):

    return """
    <h1>404 - Page Not Found</h1>
    <a href="/">Return Home</a>
    """, 404
# ==========================
# Run Application
# ==========================

if __name__ == "__main__":

    app.run(debug=True)