import os
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index(host=os.environ["PINECONE_HOST"])

recipes = [
    {
        "_id": "recipe1",
        "text": "Mediterranean chicken rice bowl with chicken breast, rice, feta, roasted carrots, garlic, olive oil, lemon, and oregano. Cook chicken with garlic and oregano, roast carrots, serve over rice, top with feta and lemon.",
        "title": "Mediterranean Chicken Rice Bowl",
        "cuisine": "Mediterranean",
        "protein": "chicken"
    },
    {
        "_id": "recipe2",
        "text": "Greek chicken salad bowl with chicken, feta, cucumber, tomato, red onion, olive oil, lemon, and herbs. Grill the chicken and serve with chopped vegetables and feta.",
        "title": "Greek Chicken Salad Bowl",
        "cuisine": "Greek",
        "protein": "chicken"
    },
    {
        "_id": "recipe3",
        "text": "Teriyaki chicken rice bowl with chicken breast, rice, soy sauce, ginger, garlic, carrots, and broccoli. Cook chicken in a sweet savory sauce and serve with rice and vegetables.",
        "title": "Teriyaki Chicken Rice Bowl",
        "cuisine": "Asian",
        "protein": "chicken"
    },
    {
        "_id": "recipe4",
        "text": "Roasted veggie feta bowl with rice, feta, carrots, zucchini, chickpeas, olive oil, and paprika. Roast vegetables, serve over rice, and top with feta.",
        "title": "Roasted Veggie Feta Bowl",
        "cuisine": "Vegetarian",
        "protein": "chickpeas"
    },
]

index.upsert_records("recipes", recipes)
print("Uploaded recipes.")