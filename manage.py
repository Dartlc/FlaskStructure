from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager

from app import app
from models import database

manager = Manager(app, database)
migrate = Migrate(app, database)
manager.add_command('database', MigrateCommand)

if __name__ == '__main__':
    manager.run()
