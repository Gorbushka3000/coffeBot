from flask import Flask, render_template, request, redirect
from telegram.control.usercontrol import add_coffee, returnInfoUser
from telegram.models.client import client
from telegram.models.vsegdaCoffeDb import Session
from sqlalchemy.orm import Session as SqlSession

app = Flask(__name__)


@app.route('/<int:id>', methods=['POST', 'GET'])
def add_coffe(id):
    client = returnInfoUser(id)
    if request.method == "POST":
        add_coffee(int(id), int(request.form.get('plusCoffeCup')))
        return redirect(f'/{id}')
    return render_template('add.html', client=client)


app.run(debug=True, host='192.168.1.54', port=5002)
