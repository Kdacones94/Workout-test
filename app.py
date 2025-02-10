from flask import Flask, request, render_template, redirect, url_for
from models import User, engine, SQLModel
from crud import create_user, get_user, update_user, delete_user

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        create_user(username, email)
        return redirect(url_for('users'))
    else:
        with Session(engine) as session:
            statement = select(User)
            users = session.exec(statement).all()
        return render_template('users.html', users=users)

@app.route('/user/<int:user_id>', methods=['GET', 'POST'])
def user(user_id):
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        update_user(user_id, username, email)
        return redirect(url_for('users'))
    else:
        user = get_user(user_id)
        return render_template('user.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user_route(user_id):
    delete_user(user_id)
    return redirect(url_for('users'))

if __name__ == "__main__":
    app.run(debug=True)