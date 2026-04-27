from flask import Flask, request, jsonify,Blueprint

assessment_bp = Blueprint('assessment', __name__)


@assessment_bp.post("/assessments")
def get_data():
    data = request.get_json()

    name  = data.get("name")
    status = data.get("status")

    return {"name":name, "status": status}

@assessment_bp.get("/assessments")
def give_data():
    data = {"name": "Isaac" , "status": "sick"}
    return jsonify(data)

assessments = {
    1: {"name": "Isaac", "phq": "severe", "gad7": "mild"},
    2: {"name": "John", "phq": "moderate", "gad7": "severe"},
    3: {"name": "Jane", "phq": "mild", "gad7": "moderate"},
}

@assessment_bp.get("/assessments/<int:id>")
def return_data_via_id(id):
    assessment = assessments.get(id)

    if assessment is None:
        return{"error": f"Assessment of {id} does not exist"},404
    
    return assessment