CREATE TABLE IF NOT EXISTS Document (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    requesterId INTEGER NOT NULL,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    pdfOriginal TEXT NOT NULL,
    requestedDate TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Approval (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    documentId INTEGER NOT NULL,
    approverId TEXT NOT NULL,
    approved INTEGER,
    approvalDate TEXT NOT NULL,
    FOREIGN KEY (documentId) REFERENCES Document(id)
);

CREATE TABLE IF NOT EXISTS Requester (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    password TEXT NOT NULL
);
