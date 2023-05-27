import pinecone

pinecone.init(api_key="<YOUR_API_KEY">, environment="<ENVIRONMENT>"
pinecone.create_index("quickstart", dimension=8, metric="euclidean")