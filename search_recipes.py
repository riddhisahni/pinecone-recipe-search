import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index(host=os.environ["PINECONE_HOST"])

query_text = input("What ingredients do you have? ").strip()

results = index.search(
    namespace="recipes",
    query={
        "inputs": {"text": query_text},
        "top_k": 3
    },
    fields=["title", "text", "cuisine"]
)

print("\nTop matches:\n")

for hit in results["result"]["hits"]:
    fields = hit["fields"]
    print(f"Title: {fields.get('title', 'Unknown')}")
    print(f"Cuisine: {fields.get('cuisine', 'Unknown')}")
    print(f"Text: {fields.get('text', '')}")
    print(f"Score: {hit.get('_score', 'N/A')}")
    print("-" * 50)