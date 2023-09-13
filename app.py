from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#configure the database using SQLite

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crudtask.db"
db = SQLAlchemy(app)

# person model for the database
class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer)
    country =db.Column(db.String(100))
    email = db.Column(db.String(100))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "country": self.country,
            "email": self.email
        }

with app.app_context():
    db.create_all()

# CREATE (POST) endpoint
@app.route('/api/', methods=['POST'])
def create_person():
    data = request.get_json()  # Get JSON data from the request body

    # Validate and process the data (e.g., add to the data store)
    new_person = Person(name=data["name"], age=data['age'], country=data['country'], email=data['email'])
    
    #check for exceptions
    try:
        db.session.add(new_person)
        db.session.commit()
        return jsonify({"message": "Person has been added successfully", "person": new_person.serialize()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Failed to add person", "error": str(e)}), 500
# READ (GET) endpoint
@app.route('/api/<int:person_id>', methods=['GET'])
def get_person(person_id):
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({"message": "Person not found"}), 404
    return jsonify(person.serialize()), 200

# UPDATE (PUT) endpoint
@app.route('/api/<int:person_id>', methods=['PUT'])
def update_person(person_id):
    data = request.get_json()  # Get JSON data from the request body

    # Find the person to update by ID
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({"message": "Person not found"}), 404

    # Update the person's data
    person.name = data.get('name', person.name)
    person.age = data.get('age', person.age)
    person.country = data.get('country', person.country)
    person.email = data.get('email', person.email)

    db.session.commit()
    return jsonify({"message": "Person updated successfully", "person": person.serialize()}), 200

# DELETE (DELETE) endpoint
@app.route('/api/<int:person_id>', methods=['DELETE'])
def delete_person(person_id):
    person = Person.query.get(person_id)
    if person is None:
        return jsonify({"message": "Person not found"}), 404

    # Remove the person from the data store
    db.session.delete(person)
    db.session.commit()

    return jsonify({"message": "Person deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode for development
