"""
Main point of entry for the web application

"""

import flask_sijax
from flask import render_template, g, request
from app import app
from sijax_handlers.setup_handler import setup_handler


@flask_sijax.route(app, '/')
def login():
    # Check if is a sijax request
    if g.sijax.is_sijax_request:

        # Create a new handler
        g.sijax.register_object(setup_handler())

        # Process the request
        return g.sijax.process_request()

    # Return index page
    return render_template('index.html')

