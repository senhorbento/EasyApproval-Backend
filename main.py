from flask import Flask
from flasgger import Swagger
from src.Controllers.ApprovalController import approval_bp
from src.Controllers.DocumentController import document_bp
from src.Core.DB import DB

with open('./src/Core/creation_script.sql', 'r') as file:
    create_table_queries = file.read().split(';')

db = DB()
for query in create_table_queries:
    if query.strip():
        db.create_table(query)

app = Flask(__name__)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "version": "1.0",
            "title": "EasyApproval API",
            "description": "The EasyApproval API",
            "endpoint": "apispec_1",
            "route": "/swagger.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
    "tags": [
        {"name": "Approval", "description": "Operations related to approvals"},
        {"name": "Document", "description": "Operations related to documents"},
    ]
}
swagger = Swagger(app, config=swagger_config)

app.register_blueprint(approval_bp, url_prefix="/approval")
app.register_blueprint(document_bp, url_prefix="/document")

if __name__ == '__main__':
    app.run(debug=True)
