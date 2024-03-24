class DocumentInsert:
    def __init__(self):
        self.requesterId = ""
        self.documentName = ""
        self.pdfOriginal = ""
        self.approvals = []

class DocumentRead:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.status = ""
        self.requesterId = ""
        self.requestDate = ""

class DocumentWithApprovals:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.status = ""
        self.requesterId = ""
        self.requestedDate = ""
        self.pdfOriginal = ""
        self.approvals = []
