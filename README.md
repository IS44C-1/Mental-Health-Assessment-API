# Mental-Health Assessment API

A REST API for submitting and retrieving mental health assessments. 
Built with Flask. Returns JSON.

## Setup
```bash
git clone <repo-url>
cd mental-health-assessment-api
python -m venv .venv
.venv\Scripts\activate.ps1
pip install -r requirements.txt
python app.py
```
**Stack:** Python, Flask

## End Points

### POST /assessments
Submits a new assessment.

Request body:
{
  "name": "string",
  "status": "string"
}

Response:
{
  "name": "string",
  "status": "string"
}

### GET /assessments
Retrieves all the assessments.

Response:
{
  "name": "string",
  "status": "string"
}

### GET /assessments/<int:id>
Retrieves a given assessment by id.

URL parameter: id (integer)
Example: GET /assessments/3

Response:
{
  "name": "string",
  "status": "string"
}
