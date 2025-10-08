from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint(
    'auth', 
    __name__, 
    url_prefix='/auth',
)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

