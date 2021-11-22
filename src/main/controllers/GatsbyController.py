from flask import Blueprint, make_response, redirect, url_for, render_template
from flask_classful import FlaskView, route

class GatsbyController(FlaskView):
    #
    # Constructor
    #
    def __init__(self):
        return

    #
    # Routes
    #
    @route('/')
    def index(self):
        return make_response(redirect('/gatsby'), 302)

    @route('/gatsby')
    def gatsby(self):
        return make_response(render_template('gatsby.html'), 200)