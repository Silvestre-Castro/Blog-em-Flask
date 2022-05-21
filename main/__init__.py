from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)



# -------- funções do banco -------------

def get_db():

    conn = sqlite3.connect("main/database.db")

    # row factory
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    
    return conn, cur


# ---------------------------------------



@app.route("/")
@app.route("/blog/")
def index():

    output = None

    conn, cur = get_db()

    select_posts = """
    select * from posts
    order by id desc
    ;
    """
    cur.execute(select_posts)
    output = cur.fetchall()

    conn.close()

    return render_template("index.html", output=output)


@app.route("/admin/")
def admin():
    return "em contrução"


@app.route("/admin/blog/")
def admin_blog():
    return "em contrução"


@app.route("/admin/create/")
def admin_blog_create():
    return "em contrução"


@app.route("/admin/update/")
def admin_blog_update():
    return "em contrução"


@app.route("/admin/delete/")
def admin_blog_delete():
    return "em contrução"



    