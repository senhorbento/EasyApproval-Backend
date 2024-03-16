from flask import Flask
from Controllers.ApprovalController import approval_bp
from Controllers.DocumentController import document_bp
from flasgger import Swagger

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
