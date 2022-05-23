from crypt import methods
from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__)



# -------- funções do banco -------------

def get_db():

    conn = sqlite3.connect("main/database.db")

    # row factory
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    
    return conn, cur

def get_all_posts(ordem = "asc"):

    select_posts_asc = """
    select * from posts
    order by id asc
    ;
    """

    select_posts_desc = """
    select * from posts
    order by id desc
    ;
    """

    conn, cur = get_db()

    if ordem == "desc":
        cur.execute(select_posts_desc)
    elif ordem == "asc":
        cur.execute(select_posts_asc)
    
    posts = cur.fetchall()

    conn.close()

    return posts



# ---------------------------------------



@app.route("/")
@app.route("/blog/")
def index():

    output = None

    conn, cur = get_db()

    output = get_all_posts(ordem = "desc")

    conn.close()

    return render_template("index.html", output=output)


@app.route("/admin/")
def admin():
    return render_template("admin.html")


@app.route("/admin/blog/")
def admin_blog():

    output = None

    output = get_all_posts()

    return render_template("admin_blog.html", output = output)


@app.route("/admin/blog/create/", methods= ("POST", "GET"))
def admin_blog_create():

    input = output = None

    insert_post = """
    insert into posts (título, conteúdo)
    values
    (?, ?)
    ;
    """

    if request.method == "POST":
        input = request.form

        conn, cur = get_db()

        cur.execute(insert_post, (input['título'], input['conteúdo']))

        conn.commit()
        conn.close()

    return render_template('admin_blog_create.html', output = input)


@app.route("/admin/blog/update/")
def admin_blog_update():
    return "em contrução"


@app.route("/admin/blog/<int:id>/delete/")
def admin_blog_delete(id = id):

    output = id

    delete_post = """
    delete from posts
    where id = ?
    ;
    """

    conn, cur = get_db()

    cur.execute(delete_post, (id,))

    conn.commit()
    conn.close()


    return render_template("admin_blog_delete.html", output = output)



    