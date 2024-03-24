from flask import Blueprint, jsonify, request
from flasgger import Swagger

approval_bp = Blueprint('approval_bp', __name__)

@approval_bp.route('/<string:documentGuid>', methods=['GET'])
def get_all_by_guid(documentGuid):
    """
    Get all approvals from a document by document GUID
    ---
    responses:
      200:
        description: Approvals found
      404:
        description: Approvals not found
    """
    return jsonify({"error": "Approvals not found"}), 404

@approval_bp.route('/update', methods=['PUT'])
def update_by_guid():
    """
    Update the approval status from a document by approval GUID and document GUID
    ---
    responses:
      200:
        description: Approvals found
      404:
        description: Approvals not found
    """
    return jsonify({"error": "Approvals not found"}), 404
