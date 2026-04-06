import os
import streamlit as st
from pinecone import Pinecone

try:
    api_key = st.secrets["PINECONE_API_KEY"]
    host = st.secrets["PINECONE_HOST"]
except Exception:
    api_key = os.getenv("PINECONE_API_KEY")
    host = os.getenv("PINECONE_HOST")

if not api_key or not host:
    st.error("Missing Pinecone credentials. Set Streamlit secrets or environment variables.")
    st.stop()

pc = Pinecone(api_key=api_key)
index = pc.Index(host=host)

st.set_page_config(page_title="Recipe Search", page_icon="🍽️")

st.title("🍽️ Pinecone Recipe Search")
st.write("Enter ingredients or a meal idea, and find the closest recipes.")

query_text = st.text_input(
    "What ingredients do you have?",
    placeholder="chicken, feta, carrots, rice"
)

if st.button("Search"):
    if not query_text.strip():
        st.warning("Please enter some ingredients first.")
    else:
        with st.spinner("Searching recipes..."):
            results = index.search(
                namespace="recipes",
                query={
                    "inputs": {"text": query_text},
                    "top_k": 3
                },
                fields=["title", "text", "cuisine"]
            )

        hits = results["result"]["hits"]

        if not hits:
            st.info("No matching recipes found.")
        else:
            st.subheader("Top matches")
            for i, hit in enumerate(hits, start=1):
                fields = hit.get("fields", {})
                title = fields.get("title", "Unknown")
                cuisine = fields.get("cuisine", "Unknown")
                text = fields.get("text", "")
                score = hit.get("_score", None)

                with st.container():
                    st.markdown(f"### {i}. {title}")
                    st.write(f"**Cuisine:** {cuisine}")
                    if score is not None:
                        st.write(f"**Score:** {score:.4f}")
                    st.write(text)
                    st.divider()