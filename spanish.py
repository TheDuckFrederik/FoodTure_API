from flask import Flask, jsonify

app = Flask(__name__)

# List of national dishes with updated measurements and detailed steps
dishes = [
    {
        "country": "Spain",
        "dish": "Paella",
        "recipe": {
            "ingredients": [
                "400g rice",
                "1g saffron threads",
                "500g chicken, cut into pieces",
                "300g rabbit, cut into pieces",
                "150g green beans",
                "2 tomatoes, grated",
                "60ml olive oil",
                "4 garlic cloves, minced",
                "1 tsp smoked paprika",
                "1.5L chicken broth",
                "Salt to taste"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a large paella pan over medium heat.",
                "Step 2: Add the chicken and rabbit pieces and brown them on all sides.",
                "Step 3: Add the green beans and sauté for 5 minutes.",
                "Step 4: Add the grated tomatoes, minced garlic, and smoked paprika, and cook for another 5 minutes.",
                "Step 5: Add the rice and stir to coat it in the mixture.",
                "Step 6: Pour in the saffron-infused chicken broth and stir once.",
                "Step 7: Bring to a boil, then reduce the heat and let it simmer without stirring until the rice is cooked and the broth has evaporated (about 20 minutes).",
                "Step 8: Let it rest for a few minutes before serving."
            ]
        },
        "origin": "Valencia, Spain",
        "history": "Paella originated in Valencia in the mid-19th century, traditionally made by laborers using locally available ingredients."
    },
    {
        "country": "Italy",
        "dish": "Pizza Margherita",
        "recipe": {
            "ingredients": [
                "500g pizza dough",
                "200g canned tomatoes, crushed",
                "200g mozzarella cheese, sliced",
                "10 fresh basil leaves",
                "2 tbsp olive oil",
                "1 tsp salt"
            ],
            "instructions": [
                "Step 1: Preheat the oven to 250°C (480°F).",
                "Step 2: Roll out the pizza dough on a floured surface.",
                "Step 3: Spread the crushed tomatoes evenly over the dough.",
                "Step 4: Place the mozzarella slices evenly over the tomato sauce.",
                "Step 5: Scatter fresh basil leaves on top.",
                "Step 6: Drizzle with olive oil and sprinkle with salt.",
                "Step 7: Bake in the preheated oven for 8-10 minutes or until the crust is golden and the cheese is melted."
            ]
        },
        "origin": "Naples, Italy",
        "history": "Pizza Margherita was created in Naples in 1889 to honor Queen Margherita of Savoy, reflecting the colors of the Italian flag."
    },
    {
        "country": "Germany",
        "dish": "Sauerbraten",
        "recipe": {
            "ingredients": [
                "1kg beef roast",
                "500ml red wine vinegar",
                "2 onions, sliced",
                "2 carrots, sliced",
                "10 black peppercorns",
                "5 juniper berries",
                "2 bay leaves",
                "1 tbsp sugar",
                "Salt to taste",
                "50g gingerbread, crumbled"
            ],
            "instructions": [
                "Step 1: Marinate the beef in a mixture of vinegar, onions, carrots, peppercorns, juniper berries, and bay leaves for 3-5 days in the refrigerator.",
                "Step 2: Remove the beef from the marinade and pat it dry.",
                "Step 3: Sear the beef in a hot pot until browned on all sides.",
                "Step 4: Add the marinade, sugar, and gingerbread crumbs to the pot.",
                "Step 5: Cover and simmer on low heat for 2-3 hours until the meat is tender.",
                "Step 6: Remove the meat, strain the sauce, and serve it with the sliced beef."
            ]
        },
        "origin": "Germany",
        "history": "Sauerbraten is a traditional German pot roast dating back to the Middle Ages, initially used to preserve meat."
    },
    {
        "country": "Greece",
        "dish": "Moussaka",
        "recipe": {
            "ingredients": [
                "3 large eggplants, sliced",
                "500g minced beef or lamb",
                "1 onion, chopped",
                "400g canned tomatoes, chopped",
                "60ml olive oil",
                "1 tsp cinnamon",
                "1 tsp salt",
                "1/2 tsp pepper",
                "50g flour",
                "500ml milk",
                "60g butter",
                "2 egg yolks"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F).",
                "Step 2: Fry the eggplant slices in olive oil until golden and set aside.",
                "Step 3: In a separate pan, cook the minced meat with onions until browned.",
                "Step 4: Add the tomatoes, cinnamon, salt, and pepper, and simmer for 20 minutes.",
                "Step 5: For the béchamel, melt butter in a pan, stir in flour, and cook for 1 minute. Gradually add milk, stirring until thickened.",
                "Step 6: Remove from heat and stir in egg yolks.",
                "Step 7: Layer half the eggplants in a baking dish, cover with meat sauce, and add the remaining eggplants.",
                "Step 8: Pour the béchamel sauce on top and bake for 45 minutes until golden."
            ]
        },
        "origin": "Greece",
        "history": "Moussaka is a popular dish in Greece, with roots tracing back to the Ottoman Empire, blending Middle Eastern and European influences."
    },
    {
        "country": "Portugal",
        "dish": "Bacalhau à Brás",
        "recipe": {
            "ingredients": [
                "400g salted cod, soaked and shredded",
                "2 onions, thinly sliced",
                "4 potatoes, cut into thin strips",
                "4 eggs, beaten",
                "100g black olives",
                "2 tbsp chopped parsley",
                "60ml olive oil",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Sauté onions in olive oil until translucent.",
                "Step 2: Add the shredded cod and cook for 5 minutes.",
                "Step 3: Fry the potatoes separately until golden and crispy.",
                "Step 4: Add the fried potatoes to the cod mixture.",
                "Step 5: Pour in the beaten eggs, stirring gently until creamy.",
                "Step 6: Garnish with olives and parsley before serving."
            ]
        },
        "origin": "Portugal",
        "history": "Bacalhau à Brás is one of many dishes made with salted cod, which has been a staple in Portuguese cuisine since the Age of Exploration."
    },
    {
        "country": "Sweden",
        "dish": "Köttbullar (Swedish Meatballs)",
        "recipe": {
            "ingredients": [
                "250g ground beef",
                "250g ground pork",
                "100g breadcrumbs",
                "1 onion, finely chopped",
                "1 egg",
                "100ml milk",
                "50g butter",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Mix the ground beef and pork with breadcrumbs, chopped onion, egg, and milk.",
                "Step 2: Season with salt and pepper.",
                "Step 3: Form small meatballs from the mixture.",
                "Step 4: Fry the meatballs in butter until browned and cooked through.",
                "Step 5: Serve with gravy, lingonberry jam, and mashed potatoes."
            ]
        },
        "origin": "Sweden",
        "history": "Köttbullar, or Swedish meatballs, have been part of Swedish cuisine since the 18th century and became internationally famous through IKEA."
    },
    {
        "country": "Hungary",
        "dish": "Goulash",
        "recipe": {
            "ingredients": [
                "800g beef, cubed",
                "2 onions, chopped",
                "3 tbsp paprika",
                "3 potatoes, diced",
                "3 carrots, sliced",
                "2 bell peppers, chopped",
                "4 garlic cloves, minced",
                "1L beef broth",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Sauté onions in a pot until golden.",
                "Step 2: Add beef and brown on all sides.",
                "Step 3: Stir in paprika and garlic.",
                "Step 4: Add potatoes, carrots, bell peppers, and beef broth.",
                "Step 5: Season with salt and pepper.",
                "Step 6: Simmer for 2 hours until the meat and vegetables are tender."
            ]
        },
        "origin": "Hungary",
        "history": "Goulash is a traditional Hungarian stew originating in the 9th century, originally cooked by herdsmen over an open fire."
    },
    {
        "country": "Poland",
        "dish": "Pierogi",
        "recipe": {
            "ingredients": [
                "300g flour",
                "1 egg",
                "120ml water",
                "1/2 tsp salt",
                "400g potatoes, mashed",
                "200g cottage cheese",
                "1 onion, chopped",
                "50g butter"
            ],
            "instructions": [
                "Step 1: Mix flour, egg, water, and salt to make the dough, knead until smooth, and let rest for 30 minutes.",
                "Step 2: Mix mashed potatoes with cottage cheese and season with salt.",
                "Step 3: Roll out the dough and cut into circles.",
                "Step 4: Place a spoonful of filling on each circle and fold over, sealing the edges.",
                "Step 5: Boil pierogi in salted water until they float to the surface.",
                "Step 6: Fry the chopped onion in butter and serve over the cooked pierogi."
            ]
        },
        "origin": "Poland",
        "history": "Pierogi are a staple in Polish cuisine dating back to the 13th century, introduced by nobility and enjoyed across all social classes."
    },
    {
        "country": "Belgium",
        "dish": "Moules-frites",
        "recipe": {
            "ingredients": [
                "1kg mussels, cleaned",
                "200ml white wine",
                "2 garlic cloves, minced",
                "2 shallots, chopped",
                "2 tbsp chopped parsley",
                "50g butter",
                "500g fries"
            ],
            "instructions": [
                "Step 1: In a large pot, melt butter and sauté garlic and shallots until soft.",
                "Step 2: Add the mussels and white wine.",
                "Step 3: Cover and cook on high heat for 5 minutes until mussels open.",
                "Step 4: Sprinkle with chopped parsley.",
                "Step 5: Serve immediately with fries."
            ]
        },
        "origin": "Belgium",
        "history": "Moules-frites is a classic Belgian dish of mussels and fries, popularized in the 18th century."
    },
    {
        "country": "Austria",
        "dish": "Wiener Schnitzel",
        "recipe": {
            "ingredients": [
                "4 veal cutlets (about 150g each)",
                "100g flour",
                "2 eggs, beaten",
                "200g breadcrumbs",
                "Salt to taste",
                "100g butter"
            ],
            "instructions": [
                "Step 1: Season the veal cutlets with salt.",
                "Step 2: Dredge each cutlet in flour, then dip in beaten eggs, and coat with breadcrumbs.",
                "Step 3: Heat butter in a large pan over medium heat.",
                "Step 4: Fry each cutlet until golden brown and crisp on both sides.",
                "Step 5: Drain on paper towels and serve immediately."
            ]
        },
        "origin": "Austria",
        "history": "Wiener Schnitzel is a traditional Austrian dish that dates back to the 19th century and has become a symbol of Austrian cuisine."
    }
]

# Route to get all dishes
@app.route('/dishes', methods=['GET'])
def get_dishes():
    return jsonify(dishes)

# Route to get a dish by country
@app.route('/dishes/<country>', methods=['GET'])
def get_dish_by_country(country):
    dish = next((d for d in dishes if d["country"].lower() == country.lower()), None)
    if dish:
        return jsonify(dish)
    return jsonify({"message": "Dish not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)