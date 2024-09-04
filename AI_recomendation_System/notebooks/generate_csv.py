import csv
import random
from datetime import datetime, timedelta
from typing import List, Optional
from pydantic import BaseModel, Field

#
def generate_id():
    return str(random.randint(1000, 9999))
class Embeddings(BaseModel):
    id_embeddings: Optional[str] = Field(default_factory=generate_id, alias='_id')
    entity_type: str = Field(description="Ex: user, item")
    entity_id: str = Field(default_factory=generate_id)
    embedings_vector: List[float]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    update_at: Optional[datetime] = Field(default_factory=datetime.now)
    
    class Config:
        arbitrary_types_allowed = True

def generate_fake_embeddings(num_records: int):
    fake_data = []
    for _ in range(num_records):
        entity_type = random.choice(['user', 'item'])
        entity_id = generate_id()
        embedings_vector = [round(random.random(), 5) for _ in range(10)] 
        created_at = datetime.now() - timedelta(days=random.randint(0, 365))
        update_at = created_at + timedelta(days=random.randint(0, 30))
        
        fake_data.append(Embeddings(
            id_embeddings=generate_id(),
            entity_type=entity_type,
            entity_id=entity_id,
            embedings_vector=embedings_vector,
            created_at=created_at,
            update_at=update_at
        ))
    return fake_data

data = generate_fake_embeddings(50)


with open('embeddings_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['id_embeddings', 'entity_type', 'entity_id', 'embedings_vector', 'created_at', 'update_at']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in data:
        writer.writerow({
            'id_embeddings': item.id_embeddings,
            'entity_type': item.entity_type,
            'entity_id': item.entity_id,
            'embedings_vector': ','.join(map(str, item.embedings_vector)), 
            'created_at': item.created_at.isoformat(),
            'update_at': item.update_at.isoformat()
        })

print("CSV gerado com sucesso!")