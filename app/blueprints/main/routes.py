from . import main
from flask import render_template, jsonify
from app.blueprints.api.github import ReposList
from flask_babel import _


@main.route('/')
def home():
    username = 'paulof9'
    repos_obj = ReposList(username).get_user()

    user = {
        "name": repos_obj.get("name"),
        "avatar_url": repos_obj.get("avatar_url"),
        "location": repos_obj.get("location")
    }

    return render_template('index.html', user=user)

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/projects')
def projects():
    username = 'paulof9'
    repos_obj = ReposList(username).get_repos()

    repos = [{
        "name": repo["name"],
        "description": repo.get("description"),
        "html_url": repo["html_url"],
        "language": repo["language"]
    } for repo in repos_obj]

    return render_template('projects.html', repos=repos)

@main.route('/api/projects')
def api_projects():
    repos = ReposList("paulof9").get_repos()
    return jsonify(repos), 200

@main.route('/api/user')
def api_user():
    user = ReposList("paulof9").get_user()
    return jsonify(user), 200

