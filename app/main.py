from flask import render_template, request, redirect, url_for
from app.models import db
from app.models import Employee
from app import create_app

# ======== DON'T TOUCH AREA ===========
app = create_app()

@app.before_request
def create_tables():
    db.create_all()
# ====================================

@app.route("/")
def index():
    employees = Employee.query.all()
    return render_template("index.html", employees=employees)

@app.route("/create", methods=["GET"])
def show_create_employee():
    return render_template("create_employee.html")

@app.route("/create", methods=["POST"])
def create_employee():
    name=request.form["name"]
    position=request.form["position"]
    birth_date=request.form["birth_date"]
    gender=request.form["gender"]
    hire_date=request.form["hire_date"]

    new_employee = Employee(
        name=name,
        position=position,
        birth_date=birth_date,
        gender=gender,
        hire_date=hire_date
    )

    db.session.add(new_employee)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<int:employee_id>", methods=["GET"])
def show_update_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    return render_template("update_employee.html", employee=employee)

@app.route("/update/<int:employee_id>", methods=["POST"])
def update_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)

    name=request.form["name"]
    position=request.form["position"]
    birth_date=request.form["birth_date"]
    gender=request.form["gender"]
    hire_date=request.form["hire_date"]

    employee.name = name
    employee.position = position
    employee.birth_date = birth_date
    employee.gender = gender
    employee.hire_date = hire_date

    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for("index"))
