from app import app, db

# Create the Flask app context
with app.app_context():
    # Create the database tables
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
