from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/dashboard')
def dashboard():
    return render_template('main/dashboard.html')


@main.route('/users')
def users():
    return render_template('main/user_list.html')


@main.route('/orders')
def orders():
    return render_template('main/order_list.html')
