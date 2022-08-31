# import blueprint from flask and make a main blueprint
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
main = Blueprint('main', __name__, url_prefix='/')
# import adminrequired 
from .funcs import loginrequired
#home route 
@main.route('/')
# @loginrequired
def home():
    return render_template('main/base.html')

@main.route('/calls/<dest>', methods=['POST'])
def calls(dest):
    print(dest)
    print('call arrived')
    return jsonify({
        'data':render_template(f'main/{dest}.html', title=dest, test='here is a test')
    })

print()