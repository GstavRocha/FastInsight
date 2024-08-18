# COLECTIONS 

### 1. **users**
   - **Descrição:** Armazena as informações dos usuários.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "username": "string",
       "email": "string",
       "preferences": ["string"],
       "history": [{"item_id": "ObjectId", "timestamp": "datetime"}],
       "created_at": "datetime",
       "updated_at": "datetime"
     }
     ```

### 2. **items**
   - **Descrição:** Contém informações sobre os itens que podem ser recomendados (produtos, filmes, cursos, etc.).
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "name": "string",
       "description": "string",
       "category": "string",
       "tags": ["string"],
       "metadata": {"key": "value"},
       "created_at": "datetime",
       "updated_at": "datetime"
     }
     ```

### 3. **interactions**
   - **Descrição:** Registra as interações dos usuários com os itens, como visualizações, compras, cliques, etc.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "user_id": "ObjectId",
       "item_id": "ObjectId",
       "interaction_type": "string",  // Ex: view, click, purchase
       "timestamp": "datetime",
       "metadata": {"key": "value"}
     }
     ```

### 4. **recommendations**
   - **Descrição:** Armazena as recomendações feitas para cada usuário.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "user_id": "ObjectId",
       "recommended_items": [{"item_id": "ObjectId", "score": "float"}],
       "created_at": "datetime"
     }
     ```

### 5. **embeddings**
   - **Descrição:** Armazena os embeddings gerados para usuários e itens, utilizados pelo sistema de recomendação.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "entity_type": "string",  // Ex: user, item
       "entity_id": "ObjectId",
       "embedding_vector": ["float"],
       "created_at": "datetime",
       "updated_at": "datetime"
     }
     ```

### 6. **logs**
   - **Descrição:** Registra logs de atividades e eventos para monitoramento e auditoria.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "event_type": "string",
       "description": "string",
       "user_id": "ObjectId",
       "item_id": "ObjectId",
       "timestamp": "datetime",
       "metadata": {"key": "value"}
     }
     ```

### 7. **categories**
   - **Descrição:** Armazena as categorias de itens, permitindo uma organização e filtragem mais eficazes.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "category_name": "string",
       "parent_category": "ObjectId",  // Para subcategorias
       "created_at": "datetime",
       "updated_at": "datetime"
     }
     ```

### 8. **feedback**
   - **Descrição:** Armazena feedback dos usuários sobre as recomendações recebidas, permitindo ajuste fino do modelo de IA.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "user_id": "ObjectId",
       "item_id": "ObjectId",
       "feedback_type": "string",  // Ex: like, dislike, rating
       "rating": "float",  // Caso o feedback seja um rating
       "timestamp": "datetime",
       "metadata": {"key": "value"}
     }
     ```

### 9. **sessions**
   - **Descrição:** Armazena informações sobre as sessões de usuários, útil para análises temporais e contextuais.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "user_id": "ObjectId",
       "session_start": "datetime",
       "session_end": "datetime",
       "device_info": "string",
       "location": "string",
       "metadata": {"key": "value"}
     }
     ```

### 10. **models**
   - **Descrição:** Armazena informações sobre diferentes versões dos modelos de IA utilizados para fazer as recomendações.
   - **Campos sugeridos:**
     ```json
     {
       "_id": "ObjectId",
       "model_name": "string",
       "version": "string",
       "trained_at": "datetime",
       "metadata": {"key": "value"}
     }
     ```