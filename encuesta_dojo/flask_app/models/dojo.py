from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name,location,language,comment,created_at,updated_at) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s,NOW(),NOW())"
        return connectToMySQL('esquema_encuesta_dojo').query_db(query,data)


    @classmethod
    def getSurvey(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        return Dojo(results[0])
    
    @staticmethod
    def validate_survey(dojo):
        is_valid = True
        if len(dojo["name"]) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if  (dojo["location"]) == "":
            flash("Must choose a location.")
            is_valid = False
        if  (dojo["language"]) == "":
            flash("Must choose a favorite language.")
            is_valid = False
        return is_valid

