from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import desc
from datetime import datetime, timedelta

# Creating the Flask app
app = Flask(__name__)

# Configuring the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TODO_PER_PAGE'] = 5
db = SQLAlchemy(app)

# Defining the ToDo model
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    in_progress = db.Column(db.Boolean, default=False)
    tags = db.Column(db.String(100))
    due_date = db.Column(db.Date)
    priority = db.Column(db.Integer)

# Route for the home page
@app.route('/')
def index():
    # Pagination and sorting logic
    page = request.args.get('page', 1, type=int)
    sort_by = request.args.get('sort_by', 'id')
    query = ToDo.query
    search_title = request.args.get('search_title', '')
    if search_title:
        query = query.filter(ToDo.title.ilike(f"%{search_title}%"))

    search_complete = request.args.get('search_complete', '')
    if search_complete.lower() in ['true', 'false']:
        complete_bool = search_complete.lower() == 'true'
        query = query.filter(ToDo.complete == complete_bool)

    if sort_by == 'title':
        ToDo_list = query.order_by(ToDo.title).paginate(page=page, per_page=app.config['TODO_PER_PAGE'], error_out=False)
    elif sort_by == 'complete':
        ToDo_list = query.order_by(desc(ToDo.complete)).paginate(page=page, per_page=app.config['TODO_PER_PAGE'], error_out=False)
    else:
        ToDo_list = query.order_by(ToDo.id).paginate(page=page, per_page=app.config['TODO_PER_PAGE'], error_out=False)

    now = datetime.now()
    return render_template("index.html", ToDo_list=ToDo_list, now=now)

# Route for adding a new ToDo item
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    tags = request.form.get("tags")
    due_date_str = request.form.get("due_date")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    priority = request.form.get("priority")
    new_ToDo = ToDo(title=title, complete=False, tags=tags, due_date=due_date, priority=priority)
    db.session.add(new_ToDo)
    db.session.commit()
    return redirect(url_for("index"))

# Route for updating the completion status of a ToDo item
@app.route("/update/<int:ToDo_id>")
def update(ToDo_id):
    ToDo_item = ToDo.query.get_or_404(ToDo_id)
    ToDo_item.complete = not ToDo_item.complete
    db.session.commit()
    return redirect(url_for("index"))

# Route for deleting a ToDo item
@app.route("/delete/<int:ToDo_id>")
def delete(ToDo_id):
    ToDo_item = ToDo.query.get_or_404(ToDo_id)
    db.session.delete(ToDo_item)
    db.session.commit()
    return redirect(url_for("index"))

# Route for sorting all ToDo items
@app.route("/sort_all", methods=["POST"])
def sort_all():
    sort_by = request.form.get("sort_by")
    return redirect(url_for("index", sort_by=sort_by))

# Route for searching ToDo items
@app.route("/search", methods=["GET"])
def search():
    # Searching ToDo items based on various criteria
    search_title = request.args.get('search_title', '')
    search_complete = request.args.get('search_complete', '')
    search_priority = request.args.get('priority','')
    start_date_str = request.args.get('start_date','')
    end_date_str = request.args.get('end_date','')
    sort_by = request.args.get('sort_by', 'id')

    query = ToDo.query

    if search_title:
        query = query.filter(ToDo.title.ilike(f"%{search_title}%"))

    if search_complete.lower() in ['true', 'false']:
        complete_bool = search_complete.lower() == 'true'
        query = query.filter(ToDo.complete == complete_bool)

    if search_priority:
        query = query.filter(ToDo.priority == int(search_priority))
    
    if start_date_str and end_date_str:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        query = query.filter(ToDo.due_date.between(start_date, end_date))

    if sort_by == 'title':
        ToDo_list = query.order_by(ToDo.title).paginate(page=1, per_page=app.config['TODO_PER_PAGE'], error_out=False)
    elif sort_by == 'complete':
        ToDo_list = query.order_by(desc(ToDo.complete)).paginate(page=1, per_page=app.config['TODO_PER_PAGE'], error_out=False)
    else:
        ToDo_list = query.order_by(ToDo.id).paginate(page=1, per_page=app.config['TODO_PER_PAGE'], error_out=False)

    now = datetime.now()

    return render_template("index.html", ToDo_list=ToDo_list, now=now)

# Route for editing a ToDo item
@app.route("/edit/<int:ToDo_id>", methods=["GET", "POST"])
def edit(ToDo_id):
    # Editing a ToDo item
    ToDo_item = ToDo.query.get_or_404(ToDo_id)

    if request.method == "POST":
        title = request.form["title"]
        tags = request.form["tags"]
        due_date_str = request.form["due_date"]
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        priority = request.form["priority"]
        status = request.form["status"]

        ToDo_item.title = title
        ToDo_item.tags = tags
        ToDo_item.due_date = due_date
        ToDo_item.priority = priority
        ToDo_item.complete = status == "1"
        ToDo_item.in_progress = status == "2"
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("edit.html", ToDo_item=ToDo_item)

# Route for setting the status of all ToDo items
@app.route("/set_all_status", methods=["GET"])
def set_all_status():
    # Setting the status of all ToDo items
    status = request.args.get('status')
    if status == 'completed':
        ToDo.query.update({'complete': True, 'in_progress': False})
    elif status == 'not_completed':
        ToDo.query.update({'complete': False, 'in_progress': False})
    elif status == 'in_progress':
        ToDo.query.update({'complete': False, 'in_progress': True})
    db.session.commit()
    return redirect(url_for("index"))

# Running the Flask app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(host='0.0.0.0', port=81)