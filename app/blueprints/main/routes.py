from . import main
from flask import render_template
from app.blueprints.api.github import ReposList

@main.route('/')
def home():
    username = 'paulof9'
    repos_obj = ReposList(username)
    user = repos_obj.get_user()
    return render_template('index.html', user=user)

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/projects')
def projects():
    username = 'paulof9'  # Exemplo: 'paulof9'
    repos_obj = ReposList(username)
    repos = repos_obj.get_repos()
    return render_template('projects.html', repos=repos)