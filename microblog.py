import sqlalchemy as sa
import sqlalchemy.orm as so
from appl import app, db
from appl.models import User, Post


@app.shell_context_processor
def make_shell_context():
  return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post}