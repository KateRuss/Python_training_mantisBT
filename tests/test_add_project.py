from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + string.punctuation + " "*10
    return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


def test_create_project(app):
    old_project = app.project.get_project_list()
    project = Project(name=random_string("project: ", 10))
    app.project.create(project)
    new_project = app.project.get_project_list()
    assert len(old_project) + 1 == len(new_project)
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
