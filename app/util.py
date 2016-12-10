from flask import session, url_for,redirect
from functools import wraps


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        if not session.get('user_name'):
            return redirect(url_for('login'))
        return func(*args, **kwds)
    return wrapper
