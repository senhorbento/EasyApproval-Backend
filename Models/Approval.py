class ApprovalInsert:
    def __init__(self):
        self.documentGuid = ""
        self.approverGuid = []


class ApprovalRead:
    def __init__(self):
        self.documentGuid = ""
        self.approverGuid = ""
        self.observation = ""
        self.approved = False

class ApprovalUpdate:
    def __init__(self):
        self.documentGuid = ""
        self.approverGuid = ""
        self.observation = ""
        self.approved = False
