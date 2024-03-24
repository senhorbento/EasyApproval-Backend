from flask import Blueprint, jsonify, request
from flasgger import Swagger

from src.Repositories.DocumentRepository import DocumentRepository

document_bp = Blueprint('document_bp', __name__)

@document_bp.route('/read', methods=['GET'])
def get_all_document():
    """
    Get a all documents
    ---
    responses:
      200:
        description: Document found
      404:
        description: Document not found
    """
    _repository = DocumentRepository()
    return jsonify(_repository.Select_All()), 404


@document_bp.route('/<string:documentGuid>', methods=['GET'])
def get_document(documentGuid):
    """
    Get a document with all approvals by document GUID
    ---
    responses:
      200:
        description: Document found
      404:
        description: Document not found
    """
    return jsonify({"error": "Approvals not found"}), 404


@document_bp.route('/list/<string:approverGuid>', methods=['GET'])
def get_all_to_approver(approverGuid):
    """
    Get all document for a specific user
    ---
    responses:
      200:
        description: Documents found
      404:
        description: Document not found
    """
    return jsonify({"error": "Approvals not found"}), 404


@document_bp.route('/Pdf/<string:documentGuid>', methods=['GET'])
def get_all_documents(documentGuid):
    """
    Get the pdf file from a specific document
    ---
    responses:
      200:
        description: Documents found
      404:
        description: Document not found
    """
    return jsonify({"error": "Approvals not found"}), 404


@document_bp.route('/create', methods=['POST'])
def create_document():
    """
    Create a new document
    ---
    post:
      summary: Creates a new user.
      consumes:
        - application/json
      parameters:
        - in: body
          name: user
          description: The user to create.
          schema:
            type: object
            required:
              - requesterId
              - documentName
              - pdfOriginal
              - approvals
            properties:
              requesterId:
                type: string
              documentName:
                type: string
              pdfOriginal:
                type: string
              approvals:
                type: object
    responses:
      201:
        description: Document created
      400:
        description: Some field is empty
    """
    data = request.form
    return jsonify(data), 400
