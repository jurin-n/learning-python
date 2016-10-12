from factory import create_app, db

app = create_app('/path/to/config.cfg')

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db.drop_all(app=app)
    db.create_all(app=app)
    print 'Initialized the database.'
