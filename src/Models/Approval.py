class ApprovalInsert:
    def __init__(self):
        self.documentGuid = ""
        self.approverId = []


class ApprovalRead:
    def __init__(self):
        self.documentId = ""
        self.approverId = ""
        self.approvalDate = ""
        self.approved = False

class ApprovalUpdate:
    def __init__(self):
        self.documentId = ""
        self.approverId = ""
        self.approved = False
