"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Welcome to Our Website!',
        year=datetime.now().year,
        greeting="Welcome to our homepage! We're glad to have you here."
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact Us',
        year=datetime.now().year,
        message='Feel free to reach out to us for any inquiries!'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About Us',
        year=datetime.now().year,
        message='We are passionate about helping our clients achieve their goals with top-notch services.'
    )

@app.route('/services')
def services():
    """Renders the services page."""
    return render_template(
        'services.html',
        title='Our Services',
        year=datetime.now().year,
        services_list=['Web Development', 'Mobile App Development', 'Digital Marketing', 'SEO Optimization'],
        description='We offer a wide range of services to help your business grow and succeed.'
    )
