from flask import request
from models import client

db = client.flask_db
user_collections = db.user_collections

def hello_world():
    print("Hello world")
    return "Hello World"

def insert_form_data():
    try:
        name = request.form.get("name")
        gender = request.form.get("gender")
        f_name = request.form.get("f_name")
        m_name = request.form.get("m_name")
        phn_num = request.form.get("phn_num")

        user_data = {
            "Name" : name,
            "Gender": gender,
            "Father's Name": f_name,
            "Mother's Name": m_name,
            "Contact": phn_num
        }

        user_collections.insert_one(user_data)

        response = {
            "success": True,
            "message": "Data inserted Succesfully"
        }, 201

    except Exception as e:
        response = {
            "success": False,
            "message": "error occurred"
        }, 400

    return response

def get_form_data():
    try:
        sample = db.user_collections.find_one({"Name": "Mridul"})
        print(sample)
        del sample["_id"]

        response = {
            "success": True,
            "data": sample
        }, 201

    except Exception as e:
        response = {
            "success": False,
            "message": "error occurred"
        }, 404

    return response

def delete_form_data():
    try:
        name = request.args.get("Name")
        my_query = {"Name":name}
        db.user_collections.delete_one(my_query)
        response = {
            "success": True,
            "message": "data deleted succesfully"
        }, 200

    except Exception as e:
        response = {
            "success": False,
            "message": "error occurred"
        }, 400

    return response

def update_form_data():
    try:
        new_name = request.args.get("name")
        sample = db.user_collections.find_one_and_update({"Contact": "7728918056"}, {"$set": {"Name": new_name}})
        response = {
            "success": True,
            "message": "data updated succesfully"
        }, 200

    except Exception as e:
        response = {
            "success": False,
            "message": "error occurred"
        }, 400

    return response

    
    
