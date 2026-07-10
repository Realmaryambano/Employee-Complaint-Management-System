from flask import Flask, render_template

app = Flask(__name__)


# ==========================
# Login Page
# ==========================

@app.route("/")
def login():
    return render_template("login.html")


# ==========================
# IT Support Page
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
# Temporary Route
# ==========================

@app.route("/complaint-form")
def complaint_form():
    return "<h1>Complaint Form Page - Coming Soon</h1>"


# ==========================
# My Complaints
# Temporary Route
# ==========================

@app.route("/my-complaints")
def my_complaints():
    return "<h1>My Complaints Page - Coming Soon</h1>"


if __name__ == "__main__":
    app.run(debug=True)