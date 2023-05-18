from flask import Flask, render_template, request, redirect
from telegram.models.client import client


app = Flask(__name__)


@app.route('/<int:id>', methods=['POST', 'GET'])
def add_coffe(id):
    infoUser = client.ReturnInfoUser(id)
    if request.method == "POST":
        client.add_coffee(int(id), int(request.form.get('plusCoffeCup')))
        return redirect(f'/{id}')
    return render_template('add.html', client=infoUser)


app.run(debug=True, host='192.168.1.54', port=5002)
