from flask import Flask, render_template, request, redirect

from user_model import User

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route("/")
def index():
    return render_template("create.html")

@app.route("/users/new")
def new_user_page():
    return render_template("create.html")

@app.route("/users/create", methods = ["POST"])
def create_user():
    print(request.form)
    User.create(request.form)
    return redirect("/users")

@app.route("/users")
def show_all():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

@app.route("/show/<int:id>")
def show_one(id):
    data = {
        'id' : id
    }
    one_user = User.get_one(id)
    print(one_user)
    return render_template("read_one.html", one_user=User.get_one(data))


@app.route("/user/edit/<int:id>")
def edit(id):
    data = {"id":id}
    return render_template("edit_user.html",user=User.get_one(data))


@app.route("/user/update", methods=["POST"])
def update():
    User.update(request.form)
    return redirect("/users")

@app.route("/user/delete/<int:id>")
def delete(id):
    data = {"id":id}
    User.delete(data)
    return redirect("/users")



if __name__ == "__main__":
    app.run(debug=True)