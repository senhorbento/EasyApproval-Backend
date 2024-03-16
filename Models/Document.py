class DocumentInsert:
    def __init__(self):
        self.requesterGuid = ""
        self.requesterName = ""
        self.documentName = ""
        self.observation = ""
        self.pdfOriginal = ""
        self.approvals = []

class DocumentRead:
    def __init__(self):
        self.guid = ""
        self.number = ""
        self.name = ""
        self.requesterName = ""
        self.documentStatus = ""
        self.requestDate = ""

class DocumentWithApprovals:
    def __init__(self):
        self.guid = ""
        self.requesterName = ""
        self.requesterEmail = ""
        self.documentName = ""
        self.documentNumber = ""
        self.observation = ""
        self.pdfOriginal = ""
        self.requestedDate = ""
        self.approvals = []
