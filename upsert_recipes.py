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
    {
        "_id": "recipe5",
        "text": "Lemon herb chicken with potatoes and green beans using chicken breast, baby potatoes, green beans, garlic, olive oil, lemon juice, and parsley. Roast everything on one sheet pan until golden and tender.",
        "title": "Lemon Herb Chicken Sheet Pan",
        "cuisine": "American",
        "protein": "chicken"
    },
    {
        "_id": "recipe6",
        "text": "Spicy chicken burrito bowl with chicken breast, rice, black beans, corn, salsa, avocado, chili powder, and lime. Cook seasoned chicken and serve over rice with beans and toppings.",
        "title": "Spicy Chicken Burrito Bowl",
        "cuisine": "Mexican",
        "protein": "chicken"
    },
    {
        "_id": "recipe7",
        "text": "Garlic parmesan chicken pasta with chicken breast, pasta, garlic, parmesan, spinach, cream, and black pepper. Sear chicken, cook pasta, and toss everything into a creamy garlic sauce.",
        "title": "Garlic Parmesan Chicken Pasta",
        "cuisine": "Italian",
        "protein": "chicken"
    },
    {
        "_id": "recipe8",
        "text": "Honey mustard chicken with roasted carrots and rice using chicken thighs, carrots, rice, Dijon mustard, honey, garlic, and olive oil. Roast the chicken and carrots and serve with warm rice.",
        "title": "Honey Mustard Chicken Plate",
        "cuisine": "American",
        "protein": "chicken"
    },
    {
        "_id": "recipe9",
        "text": "Chicken shawarma bowl with chicken breast, rice, cucumber, tomato, red onion, yogurt sauce, garlic, cumin, paprika, and lemon. Cook spiced chicken and serve in a bowl with vegetables and sauce.",
        "title": "Chicken Shawarma Bowl",
        "cuisine": "Middle Eastern",
        "protein": "chicken"
    },
    {
        "_id": "recipe10",
        "text": "Pesto chicken pasta with chicken breast, pasta, basil pesto, cherry tomatoes, parmesan, and olive oil. Cook chicken and pasta and toss together with pesto and tomatoes.",
        "title": "Pesto Chicken Pasta",
        "cuisine": "Italian",
        "protein": "chicken"
    },
    {
        "_id": "recipe11",
        "text": "Greek lamb bowl with lamb, rice, cucumber, tomato, red onion, feta, olive oil, lemon, oregano, and yogurt sauce. Cook seasoned lamb and serve over rice with fresh toppings.",
        "title": "Greek Lamb Rice Bowl",
        "cuisine": "Greek",
        "protein": "lamb"
    },
    {
        "_id": "recipe12",
        "text": "Lamb kofta plate with ground lamb, parsley, garlic, cumin, rice, cucumber salad, and yogurt sauce. Form lamb into kofta, pan cook or grill, and serve with rice and salad.",
        "title": "Lamb Kofta Plate",
        "cuisine": "Middle Eastern",
        "protein": "lamb"
    },
    {
        "_id": "recipe13",
        "text": "Mediterranean lamb and roasted vegetables with lamb, zucchini, carrots, red onion, olive oil, garlic, lemon, and herbs. Roast vegetables and serve with seared lamb.",
        "title": "Mediterranean Lamb and Veggies",
        "cuisine": "Mediterranean",
        "protein": "lamb"
    },
    {
        "_id": "recipe14",
        "text": "Lamb pita wrap with lamb, pita bread, lettuce, tomato, cucumber, feta, red onion, and tzatziki. Warm the pita, fill with lamb and fresh vegetables, and drizzle with sauce.",
        "title": "Lamb Pita Wrap",
        "cuisine": "Greek",
        "protein": "lamb"
    },
    {
        "_id": "recipe15",
        "text": "Salmon rice bowl with salmon, rice, cucumber, avocado, soy sauce, sesame oil, and carrots. Bake or pan sear salmon and serve over rice with fresh vegetables.",
        "title": "Salmon Rice Bowl",
        "cuisine": "Asian",
        "protein": "salmon"
    },
    {
        "_id": "recipe16",
        "text": "Lemon garlic salmon with roasted potatoes and asparagus using salmon fillets, potatoes, asparagus, garlic, lemon juice, and olive oil. Roast everything until tender and flaky.",
        "title": "Lemon Garlic Salmon Tray Bake",
        "cuisine": "American",
        "protein": "salmon"
    },
    {
        "_id": "recipe17",
        "text": "Mediterranean salmon bowl with salmon, rice, feta, cucumber, tomato, olives, lemon, and olive oil. Cook salmon and serve with fresh chopped toppings over rice.",
        "title": "Mediterranean Salmon Bowl",
        "cuisine": "Mediterranean",
        "protein": "salmon"
    },
    {
        "_id": "recipe18",
        "text": "Honey soy salmon with rice and broccoli using salmon, rice, broccoli, soy sauce, honey, ginger, and garlic. Glaze salmon and serve with steamed broccoli and rice.",
        "title": "Honey Soy Salmon Bowl",
        "cuisine": "Asian",
        "protein": "salmon"
    },
    {
        "_id": "recipe19",
        "text": "Shrimp taco bowl with shrimp, rice, black beans, corn, avocado, lime, chili powder, and salsa. Cook shrimp with chili and lime and serve over rice with toppings.",
        "title": "Shrimp Taco Bowl",
        "cuisine": "Mexican",
        "protein": "shrimp"
    },
    {
        "_id": "recipe20",
        "text": "Garlic butter shrimp pasta with shrimp, pasta, garlic, butter, lemon, parsley, and parmesan. Sauté shrimp in garlic butter and toss with pasta and lemon.",
        "title": "Garlic Butter Shrimp Pasta",
        "cuisine": "Italian",
        "protein": "shrimp"
    },
    {
        "_id": "recipe21",
        "text": "Chickpea curry bowl with chickpeas, coconut milk, onion, garlic, ginger, tomatoes, curry powder, and rice. Simmer chickpeas in a spiced tomato coconut sauce and serve with rice.",
        "title": "Chickpea Curry Bowl",
        "cuisine": "Indian",
        "protein": "chickpeas"
    },
    {
        "_id": "recipe22",
        "text": "Vegetable stir fry with tofu, broccoli, carrots, bell peppers, soy sauce, garlic, ginger, and rice. Sauté vegetables and tofu and toss in a savory sauce.",
        "title": "Tofu Vegetable Stir Fry",
        "cuisine": "Asian",
        "protein": "tofu"
    },
    {
        "_id": "recipe23",
        "text": "Caprese pasta with pasta, mozzarella, cherry tomatoes, basil, olive oil, garlic, and balsamic glaze. Toss warm pasta with tomatoes, cheese, and basil.",
        "title": "Caprese Pasta",
        "cuisine": "Italian",
        "protein": "mozzarella"
    },
    {
        "_id": "recipe24",
        "text": "Roasted sweet potato quinoa bowl with quinoa, sweet potato, chickpeas, spinach, feta, olive oil, cumin, and lemon dressing. Roast the sweet potatoes and build a warm grain bowl.",
        "title": "Sweet Potato Quinoa Bowl",
        "cuisine": "Vegetarian",
        "protein": "chickpeas"
    },
    {
        "_id": "recipe25",
        "text": "Mushroom spinach pasta with pasta, mushrooms, spinach, garlic, parmesan, cream, and black pepper. Cook mushrooms until browned and toss with pasta and spinach.",
        "title": "Mushroom Spinach Pasta",
        "cuisine": "Italian",
        "protein": "parmesan"
    },
    {
        "_id": "recipe26",
        "text": "Falafel bowl with falafel, rice, cucumber, tomato, hummus, pickled onion, and tahini sauce. Serve crispy falafel over rice with chopped vegetables and sauces.",
        "title": "Falafel Rice Bowl",
        "cuisine": "Middle Eastern",
        "protein": "falafel"
    },
    {
        "_id": "recipe27",
        "text": "Paneer tikka bowl with paneer, rice, yogurt, garlic, ginger, chili powder, onion, and bell peppers. Roast or pan sear marinated paneer and vegetables and serve over rice.",
        "title": "Paneer Tikka Bowl",
        "cuisine": "Indian",
        "protein": "paneer"
    },
    {
        "_id": "recipe28",
        "text": "Egg fried rice with eggs, rice, peas, carrots, soy sauce, garlic, and green onion. Scramble eggs and stir fry with rice and vegetables.",
        "title": "Egg Fried Rice",
        "cuisine": "Asian",
        "protein": "egg"
    },
    {
        "_id": "recipe29",
        "text": "Turkey taco bowl with ground turkey, rice, black beans, corn, avocado, salsa, taco seasoning, and lime. Brown the turkey with spices and serve over rice.",
        "title": "Turkey Taco Bowl",
        "cuisine": "Mexican",
        "protein": "turkey"
    },
    {
        "_id": "recipe30",
        "text": "Turkey meatball pasta with ground turkey, pasta, tomato sauce, garlic, onion, parmesan, and basil. Bake or pan cook meatballs and serve with pasta and marinara.",
        "title": "Turkey Meatball Pasta",
        "cuisine": "Italian",
        "protein": "turkey"
    },
    {
        "_id": "recipe31",
        "text": "Steak rice bowl with steak, rice, mushrooms, garlic, soy sauce, green onions, and sesame oil. Sear steak and serve sliced over rice with mushrooms.",
        "title": "Steak Mushroom Rice Bowl",
        "cuisine": "Asian Fusion",
        "protein": "beef"
    },
    {
        "_id": "recipe32",
        "text": "Beef burrito bowl with ground beef, rice, beans, corn, cheddar, salsa, avocado, and taco seasoning. Cook seasoned beef and layer over rice with toppings.",
        "title": "Beef Burrito Bowl",
        "cuisine": "Mexican",
        "protein": "beef"
    },
    {
        "_id": "recipe33",
        "text": "Classic veggie omelet with eggs, spinach, mushrooms, onions, cheddar, and herbs. Cook a soft omelet and fill with sautéed vegetables and cheese.",
        "title": "Veggie Omelet",
        "cuisine": "Breakfast",
        "protein": "egg"
    },
    {
        "_id": "recipe34",
        "text": "Avocado toast with eggs using sourdough bread, avocado, eggs, chili flakes, lemon juice, and olive oil. Toast bread, mash avocado, and top with eggs.",
        "title": "Avocado Toast with Eggs",
        "cuisine": "Breakfast",
        "protein": "egg"
    },
    {
        "_id": "recipe35",
        "text": "Greek yogurt berry bowl with Greek yogurt, berries, banana, honey, granola, and chia seeds. Layer yogurt with fruit and crunchy toppings.",
        "title": "Greek Yogurt Berry Bowl",
        "cuisine": "Breakfast",
        "protein": "yogurt"
    }
]

index.upsert_records("recipes", recipes)
print("Uploaded recipes.")