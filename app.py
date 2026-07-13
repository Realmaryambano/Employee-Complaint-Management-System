from database.db import get_connection
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# ==========================================
# Secret Key
# ==========================================

app.secret_key = "ecms_secret_key_2026"


# ==========================================
# Login Page
# ==========================================

@app.route("/", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Employee_ID, Role
            FROM Employees
            WHERE Email = :email
            AND Password = :password
        """,
        email=username,
        password=password)

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:

            employee_id = user[0]
            role = user[1]

            session["employee_id"] = employee_id
            session["role"] = role

            if role == "Admin":

                return redirect(url_for("it_dashboard"))

            elif role == "Employee":

                return redirect(url_for("employee_dashboard"))

        else:

            error = "Invalid Email or Password."

    return render_template(
        "login.html",
        error=error
    )


# ==========================================
# IT Support
# ==========================================

@app.route("/it-support")
def it_support():

    return render_template("it_support.html")


# ==========================================
# Employee Dashboard
# ==========================================

@app.route("/employee-dashboard")
def employee_dashboard():

    employee_id = session.get("employee_id")

    if not employee_id:
        return redirect(url_for("login"))

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            e.Employee_Name,
            e.Employee_ID,
            d.Department_Name,
            e.Email
        FROM Employees e
        JOIN Departments d
            ON e.Department_ID = d.Department_ID
        WHERE e.Employee_ID = :employee_id
    """,
    employee_id=employee_id)

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    return render_template(
        "employee_dashboard.html",
        employee=employee
    )

# ==========================================
# Complaint Form
# ==========================================
# ==========================================
# Complaint Form
# ==========================================

@app.route("/complaint-form", methods=["GET", "POST"])
def complaint_form():

    employee_id = session.get("employee_id")

    if not employee_id:
        return redirect(url_for("login"))


    connection = get_connection()
    cursor = connection.cursor()



    # ==========================
    # Submit Complaint
    # ==========================

    if request.method == "POST":


        issue_title = request.form["issue_title"]
        category = request.form["category"]
        priority = request.form["priority"]
        store_location = request.form["store_location"]
        contact_number = request.form["contact_number"]
        device_name = request.form["device_name"]
        description = request.form["description"]



        cursor.execute("""
            INSERT INTO Complaints
            (
                Employee_ID,
                Issue_Title,
                Category,
                Priority,
                Store_Location,
                Contact_Number,
                Device_Name,
                Description
            )

            VALUES
            (
                :employee_id,
                :issue_title,
                :category,
                :priority,
                :store_location,
                :contact_number,
                :device_name,
                :description
            )
        """,
        employee_id=employee_id,
        issue_title=issue_title,
        category=category,
        priority=priority,
        store_location=store_location,
        contact_number=contact_number,
        device_name=device_name,
        description=description
        )



        connection.commit()



        # Get generated Complaint ID

        cursor.execute("""
            SELECT MAX(Complaint_ID)
            FROM Complaints
            WHERE Employee_ID = :employee_id
        """,
        employee_id=employee_id)


        complaint_id = cursor.fetchone()[0]



        cursor.close()
        connection.close()



        return render_template(
            "complaint_success.html",
            complaint_id=complaint_id
        )




    # ==========================
    # Load Employee Information
    # ==========================


    cursor.execute("""
        SELECT
            e.Employee_Name,
            e.Employee_ID,
            d.Department_Name,
            e.Email

        FROM Employees e

        JOIN Departments d
        ON e.Department_ID = d.Department_ID

        WHERE e.Employee_ID = :employee_id

    """,
    employee_id=employee_id)



    employee = cursor.fetchone()



    cursor.close()
    connection.close()



    return render_template(
        "complaint_form.html",
        employee=employee
    )

    # ==========================
    # Submit Complaint
    # ==========================

    if request.method == "POST":


        issue_title = request.form["issue_title"]
        category = request.form["category"]
        priority = request.form["priority"]
        store_location = request.form["store_location"]
        contact_number = request.form["contact_number"]
        device_name = request.form["device_name"]
        description = request.form["description"]



        cursor.execute("""
            INSERT INTO Complaints
            (
                Employee_ID,
                Issue_Title,
                Category,
                Priority,
                Store_Location,
                Contact_Number,
                Device_Name,
                Description
            )

            VALUES
            (
                :employee_id,
                :issue_title,
                :category,
                :priority,
                :store_location,
                :contact_number,
                :device_name,
                :description
            )
        """,
        employee_id=employee_id,
        issue_title=issue_title,
        category=category,
        priority=priority,
        store_location=store_location,
        contact_number=contact_number,
        device_name=device_name,
        description=description
        )


        connection.commit()


        cursor.close()
        connection.close()


        return render_template(
        "complaint_success.html",
        complaint_id=cursor.lastrowid
)



    # ==========================
    # Display Employee Data
    # ==========================


    cursor.execute("""
        SELECT
            e.Employee_Name,
            e.Employee_ID,
            d.Department_Name,
            e.Email

        FROM Employees e

        JOIN Departments d
        ON e.Department_ID = d.Department_ID

        WHERE e.Employee_ID = :employee_id
    """,
    employee_id=employee_id)



    employee = cursor.fetchone()



    cursor.close()
    connection.close()



    return render_template(
        "complaint_form.html",
        employee=employee
    )

# ==========================================
# My Complaints
# ==========================================

@app.route("/my-complaints")
def my_complaints():

    return render_template("my_complaints.html")


# ==========================================
# IT Dashboard
# ==========================================

@app.route("/it-dashboard")
def it_dashboard():

    return render_template("it_dashboard.html")


# ==========================================
# Complaint Details
# ==========================================

@app.route("/complaint-details", methods=["GET", "POST"])
def complaint_details():

    if request.method == "POST":

        # Update Complaint Later
        pass

    return render_template("complaint_details.html")


# ==========================================
# 404 Error Page
# ==========================================

@app.errorhandler(404)
def page_not_found(error):

    return """
    <h1>404 - Page Not Found</h1>
    <a href="/">Return Home</a>
    """, 404


# ==========================================
# Test Oracle Connection
# ==========================================

try:

    connection = get_connection()

    print("✅ Connected to Oracle Database Successfully!")

    connection.close()

except Exception as e:

    print("❌ Connection Failed")
    print(e)


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)