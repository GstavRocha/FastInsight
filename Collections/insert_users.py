from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['seu_banco_de_dados']
collection = db['USER']

# Dados dos usuários
usuarios = [
    {
        username: "alice.smith",
        "email": "alice.smith@example.com",
        "preference": ["tech", "music"],
        "history": [],
        "created_at": "2024-09-03 12:00:00"
    },
    {
        "username": "bob.jones",
        "email": "bob.jones@example.com",
        "preference": ["movies", "gaming"],
        "history": [],
        "created_at": "2024-09-03 12:01:00"
    },
    {
        "username": "charlie.brown",
        "email": "charlie.brown@example.com",
        "preference": ["books", "tech"],
        "history": [],
        "created_at": "2024-09-03 12:02:00"
    },
    {
        "username": "david.johnson",
        "email": "david.johnson@example.com",
        "preference": ["sports", "music"],
        "history": [],
        "created_at": "2024-09-03 12:03:00"
    },
    {
        "username": "emily.davis",
        "email": "emily.davis@example.com",
        "preference": ["art", "fashion"],
        "history": [],
        "created_at": "2024-09-03 12:04:00"
    },
    {
        "username": "frank.miller",
        "email": "frank.miller@example.com",
        "preference": ["gaming", "tech"],
        "history": [],
        "created_at": "2024-09-03 12:05:00"
    },
    {
        "username": "grace.wilson",
        "email": "grace.wilson@example.com",
        "preference": ["books", "movies"],
        "history": [],
        "created_at": "2024-09-03 12:06:00"
    },
    {
        "username": "henry.moore",
        "email": "henry.moore@example.com",
        "preference": ["sports", "gaming"],
        "history": [],
        "created_at": "2024-09-03 12:07:00"
    },
    {
        "username": "isabella.taylor",
        "email": "isabella.taylor@example.com",
        "preference": ["fashion", "art"],
        "history": [],
        "created_at": "2024-09-03 12:08:00"
    }
]

# Inserir múltiplos documentos na coleção
result = collection.insert_many(usuarios)

print(f"Usuários inseridos com IDs: {result.inserted_ids}")
