from ..Core.DB import DB

class DocumentRepository:
    def __init__(self):
        self.db = DB()

    def Select_All(self):
        select_query = 'SELECT id, requesterId, name, pdfOriginal, requestedDate FROM Document;'
        result = self.db.execute_return(select_query)
        if result:
            print("Document records:")
            for row in result:
                print(row)
        else:
            print("No records found.")

    def Select_From_User(self, requesterId):
        select_query = 'SELECT id, requesterId, name, pdfOriginal, requestedDate FROM Document WHERE requesterId = ?;'
        result = self.db.execute_return(select_query)
        if result:
            print("Document records:")
            for row in result:
                print(row)
        else:
            print("No records found.")

    def Select_To_User(self):
        select_query = 'SELECT d.id, requesterId, d.name, pdfOriginal, requestedDate FROM Document as D JOIN Approval as A ON a.documentId = d.id;'
        result = self.db.execute_return(select_query)
        if result:
            print("Document records:")
            for row in result:
                print(row)
        else:
            print("No records found.")

