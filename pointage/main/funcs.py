# import modules needed
import functools
from flask import session, redirect, url_for

def loginrequired(view):
    """
    Creates wrap that prevents unlogged in viewers from accessing admin-only routes.
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('isadmin') is None:
            return redirect(url_for('main.login'))

        return view(**kwargs)

    return wrapped_view

# function to save uploaded images
def save_image(form_image):
    """
    Saves image to static/images folder.
    """
    pass