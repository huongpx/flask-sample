from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')


@main.route('/dashboard')
def dashboard():
    legend = 'Monthly Data'
    months = ["January", "February", "March", "April", "May", "June", "July", "August", 
              "September", "October", "November", "December"
              ]
    values = [10, 9, 8, 7, 6, 4, 7, 8, 9, 10, 11, 12]
    return render_template('main/dashboard.html', values=values, months=months, legend=legend)


@main.route('/users')
def users():
    return render_template('main/user_list.html')


@main.route('/orders')
def orders():
    return render_template('main/order_list.html')
