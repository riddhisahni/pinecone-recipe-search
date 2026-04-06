import os
from dotenv import load_dotenv
import streamlit as st
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index(host=os.environ["PINECONE_HOST"])

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