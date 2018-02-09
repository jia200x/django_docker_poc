Django and Docker Proof of Concept
==================================
# Description

This PoC implements a simple RESTful API using:
* Django Rest Framework
* PostgreSQL
* Docker (with docker-compose)

# Install
Install Docker and Docker-compose (sudo apt-get install docker python-pip docker-compose).

Then, simply run `docker-compose up --build`. Docker compose will:
* Build a postgresql container
* Install Django, DRF and all dependencies
* Apply all DB migrations
* Serve the website at localhost:8000

# How to use
* After serving the website, go to localhost:8000.
* You will see the Django Rest Framework panel showing all available entry points. The nice GUI will obly appear if a web browser is used. Otherwise it will be plain JSON (try the same with curl!)
* Go to the entry point /dummy
* Use the post textbox to post a "one-field" object with Dummy field.
* Check the list of objects at /dummy/
* Access a single object by its ID. E.g /dummy/1

# Extending
* Add more models in api/models.py.
* Add serializers for a model in api/serializers.py
* Add a view for that serializer in api/views.py
* Add an entry in composeexample/settings.py
* Last but not least, generate migrations file (since new models make changes in DB) with: `docker-compose run web python manage.py makemigrations`
* Then, run `docker-compose up --build` again.

