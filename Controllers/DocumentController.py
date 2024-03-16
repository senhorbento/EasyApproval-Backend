from flask import Blueprint, jsonify, request
from flasgger import Swagger

document_bp = Blueprint('document_bp', __name__)

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
    parameters:
      - name: requesterGuid
        in: formData
        type: string
        required: true
      - name: requesterName
        in: formData
        type: string
        required: true
      - name: documentName
        in: formData
        type: string
        required: true
      - name: observation
        in: formData
        type: string
        required: true
      - name: pdfOriginal
        in: formData
        type: string
        required: true
      - name: approvals
        in: formData
        type: string
        required: true
    responses:
      201:
        description: Document created
      400:
        description: Some field is empty
    """
    data = request.form
    return jsonify(data), 400