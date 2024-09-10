#
from flask import Flask, jsonify
#
app = Flask(__name__)
#
Dishes = [
    {
        "country": "Spain",
        "dish": "Paella Valenciana",
        "recipe": {
            "ingredients": [
                "400g Bomba rice",
                "1g saffron threads",
                "500g chicken, cut into pieces",
                "300g rabbit, cut into pieces",
                "150g green beans",
                "2 ripe tomatoes, grated",
                "60ml olive oil",
                "4 garlic cloves, minced",
                "1 tsp smoked paprika",
                "1.5L chicken broth",
                "Salt to taste"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a large paella pan over medium heat.",
                "Step 2: Add the chicken and rabbit pieces, browning them on all sides.",
                "Step 3: Add the green beans and sauté for about 5 minutes.",
                "Step 4: Stir in the grated tomatoes, minced garlic, and smoked paprika, cooking for 5 minutes.",
                "Step 5: Add the rice and mix well to coat with the other ingredients.",
                "Step 6: Pour in the saffron-infused chicken broth and stir.",
                "Step 7: Bring to a boil, reduce heat, and simmer without stirring for about 20 minutes until rice is cooked.",
                "Step 8: Let it rest for 5 minutes before serving."
            ]
        },
        "origin": "Valencia, Spain",
        "history": "Paella originated in Valencia in the 19th century, traditionally cooked over an open fire with locally sourced ingredients."
    },
    {
        "country": "Spain",
        "dish": "Gazpacho",
        "recipe": {
            "ingredients": [
                "1kg ripe tomatoes, chopped",
                "1 cucumber, peeled and diced",
                "1 green bell pepper, chopped",
                "2 garlic cloves, minced",
                "50g stale bread, soaked in water",
                "60ml olive oil",
                "30ml red wine vinegar",
                "Salt to taste"
            ],
            "instructions": [
                "Step 1: Combine tomatoes, cucumber, green pepper, garlic, and soaked bread in a blender.",
                "Step 2: Blend until smooth.",
                "Step 3: Add olive oil, vinegar, and salt, blending again until well mixed.",
                "Step 4: Chill the gazpacho in the refrigerator for at least 2 hours before serving.",
                "Step 5: Serve cold, optionally garnished with diced vegetables or croutons."
            ]
        },
        "origin": "Andalusia, Spain",
        "history": "Gazpacho is a cold soup from Andalusia, perfect for hot summer days, with roots in ancient Roman and Moorish culinary traditions."
    },
    {
        "country": "Spain",
        "dish": "Tortilla Española (Spanish Omelette)",
        "recipe": {
            "ingredients": [
                "4 large potatoes, peeled and thinly sliced",
                "1 large onion, thinly sliced",
                "6 eggs",
                "150ml olive oil",
                "Salt to taste"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a large frying pan over medium heat.",
                "Step 2: Fry the potatoes and onions until soft but not browned, about 15 minutes.",
                "Step 3: Drain excess oil and let the potatoes and onions cool slightly.",
                "Step 4: Beat the eggs in a bowl, season with salt, and add the potato mixture.",
                "Step 5: Pour the mixture back into the pan and cook over medium heat until the edges are set.",
                "Step 6: Flip the tortilla onto a plate, slide it back into the pan, and cook until fully set.",
                "Step 7: Let it rest for a few minutes before slicing and serving."
            ]
        },
        "origin": "Spain",
        "history": "The Spanish omelette, or tortilla, is a classic dish believed to have originated in the 19th century as a humble, filling meal for farmers."
    },
    {
        "country": "Spain",
        "dish": "Patatas Bravas",
        "recipe": {
            "ingredients": [
                "500g potatoes, peeled and cut into cubes",
                "60ml olive oil",
                "1 tsp smoked paprika",
                "2 garlic cloves, minced",
                "200ml tomato sauce",
                "1 tsp hot chili powder",
                "Salt to taste"
            ],
            "instructions": [
                "Step 1: Preheat oven to 200°C (400°F).",
                "Step 2: Toss the potato cubes with olive oil and salt, then spread them on a baking sheet.",
                "Step 3: Roast the potatoes for 30-35 minutes until golden and crispy.",
                "Step 4: For the sauce, heat olive oil in a pan and sauté the garlic.",
                "Step 5: Add the tomato sauce, paprika, and chili powder, simmering for 10 minutes.",
                "Step 6: Serve the potatoes topped with the spicy tomato sauce."
            ]
        },
        "origin": "Madrid, Spain",
        "history": "Patatas Bravas, meaning 'fierce potatoes,' are a popular tapas dish known for their spicy tomato sauce, often served in bars across Spain."
    },
    {
        "country": "Spain",
        "dish": "Croquetas de Jamón (Ham Croquettes)",
        "recipe": {
            "ingredients": [
                "150g serrano ham, finely chopped",
                "50g butter",
                "50g flour",
                "500ml milk",
                "Salt, pepper, and nutmeg to taste",
                "2 eggs, beaten",
                "100g breadcrumbs",
                "Oil for frying"
            ],
            "instructions": [
                "Step 1: Melt butter in a pan, add flour, and cook for 2 minutes to form a roux.",
                "Step 2: Gradually whisk in the milk, cooking until thickened.",
                "Step 3: Stir in chopped ham, salt, pepper, and nutmeg. Cook for a few minutes until combined.",
                "Step 4: Let the mixture cool, then shape it into small cylinders.",
                "Step 5: Dip each croquette in beaten egg, then coat with breadcrumbs.",
                "Step 6: Fry in hot oil until golden brown. Drain on paper towels before serving."
            ]
        },
        "origin": "Spain",
        "history": "Croquetas de Jamón are a beloved Spanish snack often found in tapas bars, combining béchamel sauce with chopped ham, breaded and fried to perfection."
    },
    {
        "country": "Spain",
        "dish": "Pulpo a la Gallega (Galician Octopus)",
        "recipe": {
            "ingredients": [
                "1kg octopus, cleaned",
                "4 potatoes, peeled and sliced",
                "2 tbsp olive oil",
                "1 tsp smoked paprika",
                "1 tsp coarse salt"
            ],
            "instructions": [
                "Step 1: Bring a large pot of water to a boil.",
                "Step 2: Dip the octopus into the boiling water three times to curl the tentacles, then fully submerge and cook for 40 minutes.",
                "Step 3: In the last 10 minutes of cooking, add the sliced potatoes to the pot.",
                "Step 4: Drain the octopus and potatoes, slice the octopus, and arrange on a plate with the potatoes.",
                "Step 5: Drizzle with olive oil, sprinkle with paprika and coarse salt, and serve warm."
            ]
        },
        "origin": "Galicia, Spain",
        "history": "Pulpo a la Gallega is a traditional dish from Galicia, featuring tender octopus served with potatoes, olive oil, and paprika."
    },
    {
        "country": "Spain",
        "dish": "Pisto Manchego",
        "recipe": {
            "ingredients": [
                "2 zucchinis, diced",
                "2 red bell peppers, diced",
                "1 onion, chopped",
                "3 garlic cloves, minced",
                "500g tomatoes, chopped",
                "60ml olive oil",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a large pan over medium heat.",
                "Step 2: Sauté onions and garlic until translucent.",
                "Step 3: Add the bell peppers and cook for 5 minutes.",
                "Step 4: Stir in the diced zucchinis and cook until slightly tender.",
                "Step 5: Add the chopped tomatoes, salt, and pepper, and simmer for 20 minutes.",
                "Step 6: Serve hot, optionally topped with a fried egg or with bread."
            ]
        },
        "origin": "La Mancha, Spain",
        "history": "Pisto Manchego is a vegetable stew similar to ratatouille, originating from the region of La Mancha and often served as a side dish or main meal."
    },
    {
        "country": "Spain",
        "dish": "Calamares a la Romana (Fried Squid Rings)",
        "recipe": {
            "ingredients": [
                "500g squid rings",
                "100g flour",
                "1 egg, beaten",
                "100ml milk",
                "Salt to taste",
                "Oil for frying"
            ],
            "instructions": [
                "Step 1: Season squid rings with salt.",
                "Step 2: Mix flour, beaten egg, and milk to form a batter.",
                "Step 3: Dip squid rings into the batter, ensuring they are well coated.",
                "Step 4: Fry in hot oil until golden and crispy.",
                "Step 5: Drain on paper towels and serve with lemon wedges."
            ]
        },
        "origin": "Spain",
        "history": "Calamares a la Romana are a popular tapa in Spain, known for their crispy texture and are often enjoyed with a squeeze of lemon."
    },
    {
        "country": "Spain",
        "dish": "Fabada Asturiana",
        "recipe": {
            "ingredients": [
                "500g dried white beans, soaked overnight",
                "200g chorizo",
                "150g morcilla (blood sausage)",
                "200g pork belly, cut into chunks",
                "1 onion, chopped",
                "3 garlic cloves, minced",
                "1 bay leaf",
                "Salt to taste"
            ],
            "instructions": [
                "Step 1: Drain the soaked beans and place them in a large pot.",
                "Step 2: Add the chorizo, morcilla, pork belly, onion, garlic, and bay leaf.",
                "Step 3: Cover with water and bring to a boil.",
                "Step 4: Reduce heat and simmer for 2-3 hours until the beans are tender.",
                "Step 5: Season with salt and serve hot."
            ]
        },
        "origin": "Asturias, Spain",
        "history": "Fabada Asturiana is a hearty bean stew from Asturias, featuring various meats and sausages, traditionally eaten during colder months."
    },
    {
        "country": "Spain",
        "dish": "Gambas al Ajillo (Garlic Shrimp)",
        "recipe": {
            "ingredients": [
                "500g shrimp, peeled and deveined",
                "6 garlic cloves, thinly sliced",
                "60ml olive oil",
                "1 tsp smoked paprika",
                "1 dried chili, crushed",
                "Salt to taste",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a large skillet over medium heat.",
                "Step 2: Add the garlic and chili, sautéing until fragrant but not browned.",
                "Step 3: Add the shrimp, cooking until pink and opaque.",
                "Step 4: Stir in the smoked paprika and season with salt.",
                "Step 5: Garnish with chopped parsley and serve immediately with crusty bread."
            ]
        },
        "origin": "Spain",
        "history": "Gambas al Ajillo is a classic tapa in Spain, featuring succulent shrimp cooked in a garlic and chili-infused olive oil."
    },
    {
        "country": "Italy",
        "dish": "Spaghetti Carbonara",
        "recipe": {
            "ingredients": [
                "200g spaghetti",
                "100g pancetta, diced",
                "2 large eggs",
                "50g Parmesan cheese, grated",
                "2 garlic cloves, minced",
                "30ml olive oil",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Cook the spaghetti according to package instructions until al dente.",
                "Step 2: Heat olive oil in a pan over medium heat, add pancetta, and cook until crispy.",
                "Step 3: Add minced garlic and cook for another minute.",
                "Step 4: In a bowl, whisk together eggs and Parmesan cheese.",
                "Step 5: Drain the spaghetti and add it to the pan with pancetta and garlic.",
                "Step 6: Remove from heat and quickly stir in the egg mixture until creamy.",
                "Step 7: Season with salt and black pepper before serving."
            ]
        },
        "origin": "Rome, Italy",
        "history": "Spaghetti Carbonara is a traditional Roman dish that gained popularity in the mid-20th century, known for its rich, creamy sauce made without cream."
    },
    {
        "country": "Italy",
        "dish": "Margherita Pizza",
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
                "Step 3: Spread crushed tomatoes evenly over the dough.",
                "Step 4: Place mozzarella slices on top.",
                "Step 5: Scatter basil leaves and drizzle with olive oil.",
                "Step 6: Bake in the preheated oven for 8-10 minutes until the crust is golden and the cheese is melted."
            ]
        },
        "origin": "Naples, Italy",
        "history": "Pizza Margherita was created in Naples in 1889 to honor Queen Margherita of Savoy, reflecting the colors of the Italian flag."
    },
    {
        "country": "Italy",
        "dish": "Lasagna",
        "recipe": {
            "ingredients": [
                "300g lasagna sheets",
                "500g ground beef",
                "2 onions, chopped",
                "400g canned tomatoes, crushed",
                "200g mozzarella cheese, shredded",
                "50g Parmesan cheese, grated",
                "2 cloves garlic, minced",
                "60ml olive oil",
                "1 tsp dried oregano",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F).",
                "Step 2: Heat olive oil in a pan, add onions and garlic, and cook until softened.",
                "Step 3: Add ground beef and cook until browned.",
                "Step 4: Stir in crushed tomatoes, oregano, salt, and pepper, and simmer for 20 minutes.",
                "Step 5: In a baking dish, layer lasagna sheets, meat sauce, and mozzarella cheese.",
                "Step 6: Repeat layers, finishing with a layer of cheese and Parmesan.",
                "Step 7: Bake for 30-35 minutes until bubbling and golden on top."
            ]
        },
        "origin": "Emilia-Romagna, Italy",
        "history": "Lasagna is a classic Italian dish dating back to ancient Rome, with the modern version evolving in the Emilia-Romagna region during the Middle Ages."
    },
    {
        "country": "Italy",
        "dish": "Risotto alla Milanese",
        "recipe": {
            "ingredients": [
                "300g Arborio rice",
                "1 onion, finely chopped",
                "60ml white wine",
                "1L beef broth, heated",
                "50g Parmesan cheese, grated",
                "1g saffron threads",
                "60g butter",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Melt butter in a pan, add onions, and cook until translucent.",
                "Step 2: Stir in Arborio rice and cook for 2 minutes until slightly toasted.",
                "Step 3: Add white wine and cook until absorbed.",
                "Step 4: Gradually add beef broth, one ladle at a time, stirring frequently until the rice is creamy and cooked.",
                "Step 5: Stir in saffron, Parmesan cheese, salt, and pepper.",
                "Step 6: Serve hot, garnished with additional Parmesan if desired."
            ]
        },
        "origin": "Milan, Italy",
        "history": "Risotto alla Milanese is a rich, creamy rice dish from Milan, known for its distinctive yellow color from saffron, a prized ingredient in Northern Italy."
    },
    {
        "country": "Italy",
        "dish": "Osso Buco",
        "recipe": {
            "ingredients": [
                "4 veal shanks, with bone",
                "1 onion, chopped",
                "2 carrots, diced",
                "2 celery stalks, diced",
                "200ml white wine",
                "400g canned tomatoes, crushed",
                "1L beef broth",
                "60ml olive oil",
                "1 tsp dried thyme",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a large pot, brown veal shanks on all sides, then remove and set aside.",
                "Step 2: In the same pot, sauté onions, carrots, and celery until softened.",
                "Step 3: Add white wine, scraping up any browned bits from the pot.",
                "Step 4: Return veal shanks to the pot, add tomatoes, beef broth, thyme, salt, and pepper.",
                "Step 5: Cover and simmer for 2 hours until the meat is tender and falling off the bone.",
                "Step 6: Serve with gremolata and risotto or polenta."
            ]
        },
        "origin": "Milan, Italy",
        "history": "Osso Buco is a traditional Milanese dish featuring braised veal shanks, renowned for its rich flavor and tender meat."
    },
    {
        "country": "Italy",
        "dish": "Bruschetta",
        "recipe": {
            "ingredients": [
                "1 baguette or Italian bread, sliced",
                "4 ripe tomatoes, diced",
                "2 garlic cloves, minced",
                "60ml olive oil",
                "10 fresh basil leaves, chopped",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Toast the bread slices under a broiler or in a toaster until golden.",
                "Step 2: In a bowl, mix diced tomatoes, minced garlic, basil, olive oil, salt, and pepper.",
                "Step 3: Spoon the tomato mixture onto the toasted bread slices.",
                "Step 4: Serve immediately as an appetizer or snack."
            ]
        },
        "origin": "Central Italy",
        "history": "Bruschetta is a traditional Italian appetizer originating from Central Italy, typically served with fresh tomatoes and basil on toasted bread."
    },
    {
        "country": "Italy",
        "dish": "Tiramisu",
        "recipe": {
            "ingredients": [
                "250g mascarpone cheese",
                "3 large eggs, separated",
                "100g granulated sugar",
                "200ml strong coffee, cooled",
                "150g ladyfingers",
                "30ml coffee liqueur (optional)",
                "Cocoa powder for dusting"
            ],
            "instructions": [
                "Step 1: Whisk egg yolks with sugar until pale and creamy.",
                "Step 2: Fold in mascarpone cheese until smooth.",
                "Step 3: In a separate bowl, whip egg whites until stiff peaks form and gently fold into the mascarpone mixture.",
                "Step 4: Combine coffee and liqueur (if using) and briefly dip ladyfingers in the mixture.",
                "Step 5: Layer dipped ladyfingers in a serving dish, followed by mascarpone mixture.",
                "Step 6: Repeat layers and refrigerate for at least 4 hours.",
                "Step 7: Dust with cocoa powder before serving."
            ]
        },
        "origin": "Veneto, Italy",
        "history": "Tiramisu is a classic Italian dessert from Veneto, known for its layers of coffee-soaked ladyfingers and creamy mascarpone filling."
    },
    {
        "country": "Italy",
        "dish": "Panzanella",
        "recipe": {
            "ingredients": [
                "400g stale bread, cubed",
                "4 ripe tomatoes, chopped",
                "1 cucumber, diced",
                "1 red onion, thinly sliced",
                "60ml olive oil",
                "30ml red wine vinegar",
                "Salt and black pepper to taste",
                "Fresh basil leaves for garnish"
            ],
            "instructions": [
                "Step 1: Toast bread cubes in the oven or on a pan until crispy.",
                "Step 2: In a large bowl, combine tomatoes, cucumber, and red onion.",
                "Step 3: Add toasted bread cubes and toss.",
                "Step 4: Whisk together olive oil and red wine vinegar, then drizzle over the salad.",
                "Step 5: Season with salt and pepper, and garnish with fresh basil leaves.",
                "Step 6: Let the salad sit for 30 minutes before serving to allow flavors to meld."
            ]
        },
        "origin": "Tuscany, Italy",
        "history": "Panzanella is a traditional Tuscan salad made with stale bread, tomatoes, and cucumbers, often enjoyed during the summer months."
    },
    {
        "country": "Italy",
        "dish": "Fettuccine Alfredo",
        "recipe": {
            "ingredients": [
                "250g fettuccine",
                "100g unsalted butter",
                "100g Parmesan cheese, grated",
                "60ml heavy cream",
                "Salt and black pepper to taste",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: Cook fettuccine according to package instructions until al dente.",
                "Step 2: In a pan, melt butter over medium heat, then stir in heavy cream.",
                "Step 3: Add grated Parmesan cheese and stir until melted and smooth.",
                "Step 4: Drain the pasta and toss with the Alfredo sauce.",
                "Step 5: Season with salt and pepper, and garnish with chopped parsley before serving."
            ]
        },
        "origin": "Rome, Italy",
        "history": "Fettuccine Alfredo is a rich pasta dish invented in Rome in the early 20th century, known for its creamy cheese and butter sauce."
    },
    {
        "country": "Italy",
        "dish": "Ratatouille",
        "recipe": {
            "ingredients": [
                "1 eggplant, diced",
                "1 zucchini, diced",
                "1 bell pepper, diced",
                "2 tomatoes, chopped",
                "1 onion, chopped",
                "2 garlic cloves, minced",
                "60ml olive oil",
                "1 tsp dried thyme",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a large pan over medium heat.",
                "Step 2: Sauté onions and garlic until translucent.",
                "Step 3: Add bell pepper, eggplant, and zucchini, cooking until softened.",
                "Step 4: Stir in tomatoes, thyme, salt, and pepper, and simmer for 20 minutes.",
                "Step 5: Serve warm as a side dish or with crusty bread."
            ]
        },
        "origin": "Provence, Italy",
        "history": "Ratatouille is a vegetable stew from Provence, often enjoyed as a summer dish featuring a medley of fresh vegetables."
    },
    {
        "country": "Germany",
        "dish": "Wiener Schnitzel",
        "recipe": {
            "ingredients": [
                "4 veal cutlets",
                "100g all-purpose flour",
                "2 large eggs, beaten",
                "150g breadcrumbs",
                "60ml vegetable oil",
                "Salt and black pepper to taste",
                "Lemon wedges for serving"
            ],
            "instructions": [
                "Step 1: Pound the veal cutlets to about 0.5cm thickness.",
                "Step 2: Season the veal with salt and pepper.",
                "Step 3: Dredge each cutlet in flour, then dip in beaten eggs, and coat with breadcrumbs.",
                "Step 4: Heat vegetable oil in a large skillet over medium heat.",
                "Step 5: Fry the cutlets until golden brown and crispy, about 3-4 minutes per side.",
                "Step 6: Drain on paper towels and serve with lemon wedges."
            ]
        },
        "origin": "Vienna, Austria (popular in Germany)",
        "history": "Wiener Schnitzel is an Austrian dish that has become popular in Germany, known for its breaded veal cutlets traditionally served with lemon."
    },
    {
        "country": "Germany",
        "dish": "Bratwurst",
        "recipe": {
            "ingredients": [
                "500g ground pork",
                "250g ground veal",
                "100g ice cubes",
                "20g salt",
                "1 tsp black pepper",
                "1 tsp ground nutmeg",
                "1 tsp paprika",
                "1/4 cup milk",
                "Sausage casings (optional)"
            ],
            "instructions": [
                "Step 1: Mix ground pork and veal in a large bowl.",
                "Step 2: Add salt, pepper, nutmeg, paprika, and ice cubes. Mix thoroughly.",
                "Step 3: Gradually mix in milk until the mixture is well combined.",
                "Step 4: Stuff the sausage casings with the mixture if using, or shape into patties.",
                "Step 5: Grill or pan-fry the sausages over medium heat until cooked through and browned."
            ]
        },
        "origin": "Germany",
        "history": "Bratwurst is a traditional German sausage made from pork and veal, enjoyed in various forms across Germany, especially during festivals."
    },
    {
        "country": "Germany",
        "dish": "Sauerkraut",
        "recipe": {
            "ingredients": [
                "1kg sauerkraut",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "1 bay leaf",
                "1 tsp caraway seeds",
                "200ml vegetable broth",
                "2 tbsp vegetable oil",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Heat vegetable oil in a large pot over medium heat.",
                "Step 2: Sauté onions and garlic until translucent.",
                "Step 3: Add sauerkraut, bay leaf, caraway seeds, and vegetable broth.",
                "Step 4: Simmer for 30-40 minutes until flavors meld and sauerkraut is tender.",
                "Step 5: Season with salt and pepper before serving."
            ]
        },
        "origin": "Germany",
        "history": "Sauerkraut is a fermented cabbage dish popular in German cuisine, known for its tangy flavor and digestive benefits."
    },
    {
        "country": "Germany",
        "dish": "Kartoffelsalat (Potato Salad)",
        "recipe": {
            "ingredients": [
                "1kg potatoes, peeled and cubed",
                "100g pickles, diced",
                "1 small onion, finely chopped",
                "200ml mayonnaise",
                "2 tbsp mustard",
                "Salt and black pepper to taste",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: Boil potatoes in salted water until tender, then drain and cool.",
                "Step 2: In a large bowl, combine mayonnaise, mustard, salt, and pepper.",
                "Step 3: Add cooled potatoes, pickles, and onion, and mix gently.",
                "Step 4: Chill the salad in the refrigerator for at least 1 hour.",
                "Step 5: Garnish with chopped parsley before serving."
            ]
        },
        "origin": "Germany",
        "history": "Kartoffelsalat is a staple side dish in German cuisine, often served with sausages or meats, and varies regionally in its ingredients and dressing."
    },
    {
        "country": "Germany",
        "dish": "Sauerbraten",
        "recipe": {
            "ingredients": [
                "1kg beef roast",
                "250ml red wine vinegar",
                "250ml water",
                "1 onion, chopped",
                "2 carrots, chopped",
                "2 cloves garlic, minced",
                "2 bay leaves",
                "1 tsp black peppercorns",
                "2 tbsp sugar",
                "Salt to taste",
                "2 tbsp vegetable oil"
            ],
            "instructions": [
                "Step 1: Marinate the beef roast in a mixture of red wine vinegar, water, onion, carrots, garlic, bay leaves, peppercorns, and sugar for 3-5 days in the refrigerator.",
                "Step 2: Remove the roast from the marinade and pat dry.",
                "Step 3: Heat vegetable oil in a large pot, brown the roast on all sides.",
                "Step 4: Add the marinade and bring to a boil, then reduce heat and simmer for 2-3 hours until the meat is tender.",
                "Step 5: Slice and serve with the gravy from the pot."
            ]
        },
        "origin": "Germany",
        "history": "Sauerbraten is a pot roast marinated in a sour vinegar mixture, a traditional German dish often served with red cabbage and dumplings."
    },
    {
        "country": "Germany",
        "dish": "Königsberger Klopse",
        "recipe": {
            "ingredients": [
                "500g ground beef",
                "100g ground pork",
                "1 onion, finely chopped",
                "1 egg",
                "50g breadcrumbs",
                "200ml beef broth",
                "100ml sour cream",
                "2 tbsp capers",
                "2 tbsp vegetable oil",
                "Salt and pepper to taste"
            ],
            "instructions": [
                "Step 1: Mix ground beef, ground pork, onion, egg, breadcrumbs, salt, and pepper in a bowl.",
                "Step 2: Shape mixture into meatballs.",
                "Step 3: Heat vegetable oil in a pan and brown meatballs on all sides.",
                "Step 4: Add beef broth and simmer for 20 minutes.",
                "Step 5: Stir in sour cream and capers, cook for an additional 5 minutes.",
                "Step 6: Serve with the sauce."
            ]
        },
        "origin": "Germany",
        "history": "Königsberger Klopse is a traditional German meatball dish with a creamy caper sauce, originating from Königsberg (now Kaliningrad)."
    },
    {
        "country": "Germany",
        "dish": "Bierwurst",
        "recipe": {
            "ingredients": [
                "500g pork shoulder, finely chopped",
                "250g beef, finely chopped",
                "100g pork fat, finely chopped",
                "1 tsp salt",
                "1 tsp black pepper",
                "1 tsp paprika",
                "1 tsp ground caraway seeds",
                "1/2 cup beer",
                "Sausage casings (optional)"
            ],
            "instructions": [
                "Step 1: Mix pork shoulder, beef, and pork fat in a large bowl.",
                "Step 2: Add salt, pepper, paprika, caraway seeds, and beer. Mix thoroughly.",
                "Step 3: Stuff the mixture into sausage casings if using, or shape into patties.",
                "Step 4: Cook sausages or patties in a pan over medium heat until browned and cooked through."
            ]
        },
        "origin": "Germany",
        "history": "Bierwurst is a traditional German sausage made with beer and various spices, known for its flavorful and hearty taste."
    },
    {
        "country": "Germany",
        "dish": "Spätzle",
        "recipe": {
            "ingredients": [
                "250g all-purpose flour",
                "3 large eggs",
                "150ml milk",
                "1 tsp salt",
                "2 tbsp butter",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: In a bowl, mix flour, eggs, milk, and salt until a smooth batter forms.",
                "Step 2: Bring a large pot of salted water to a boil.",
                "Step 3: Press the batter through a Spätzle maker or a colander with large holes into the boiling water.",
                "Step 4: Cook until the Spätzle float to the surface, then remove with a slotted spoon.",
                "Step 5: Melt butter in a pan and sauté the Spätzle until slightly crispy.",
                "Step 6: Garnish with chopped parsley before serving."
            ]
        },
        "origin": "Swabia, Germany",
        "history": "Spätzle is a traditional Swabian egg noodle, often served as a side dish with meats or in hearty stews."
    },
    {
        "country": "Germany",
        "dish": "Apfelstrudel",
        "recipe": {
            "ingredients": [
                "1 sheet puff pastry",
                "3 large apples, peeled and sliced",
                "50g granulated sugar",
                "1 tsp cinnamon",
                "50g raisins",
                "30g breadcrumbs",
                "30g melted butter",
                "Powdered sugar for dusting"
            ],
            "instructions": [
                "Step 1: Preheat oven to 200°C (400°F).",
                "Step 2: Mix apples with sugar, cinnamon, and raisins in a bowl.",
                "Step 3: Roll out puff pastry on a floured surface and sprinkle with breadcrumbs.",
                "Step 4: Spread the apple mixture evenly over the pastry.",
                "Step 5: Roll the pastry into a log and place on a baking sheet.",
                "Step 6: Brush with melted butter and bake for 25-30 minutes until golden brown.",
                "Step 7: Dust with powdered sugar before serving."
            ]
        },
        "origin": "Austria (popular in Germany)",
        "history": "Apfelstrudel is a famous Austrian dessert that has become popular in Germany, known for its flaky pastry and spiced apple filling."
    },
    {
        "country": "Germany",
        "dish": "Käsespätzle",
        "recipe": {
            "ingredients": [
                "250g Spätzle (see recipe above)",
                "150g grated Emmental cheese",
                "1 large onion, sliced",
                "2 tbsp butter",
                "Salt and black pepper to taste",
                "Chopped chives for garnish"
            ],
            "instructions": [
                "Step 1: Prepare Spätzle according to the recipe above.",
                "Step 2: In a pan, melt butter and sauté sliced onions until caramelized.",
                "Step 3: Layer cooked Spätzle with grated cheese in a baking dish.",
                "Step 4: Bake at 180°C (350°F) for 10-15 minutes until cheese is melted and bubbly.",
                "Step 5: Top with caramelized onions and garnish with chopped chives before serving."
            ]
        },
        "origin": "Swabia, Germany",
        "history": "Käsespätzle is a comforting German dish made with Spätzle and melted cheese, similar to macaroni and cheese but with a unique regional twist."
    },
    {
        "country": "Greece",
        "dish": "Moussaka",
        "recipe": {
            "ingredients": [
                "2 large eggplants, sliced",
                "500g ground beef",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "400g canned tomatoes, crushed",
                "2 tbsp tomato paste",
                "1 tsp dried oregano",
                "1 tsp ground cinnamon",
                "60g butter",
                "60g all-purpose flour",
                "500ml milk",
                "2 large eggs",
                "100g grated Parmesan cheese",
                "Salt and black pepper to taste",
                "Olive oil for frying"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F).",
                "Step 2: Brush eggplant slices with olive oil and bake for 25 minutes until tender.",
                "Step 3: Heat olive oil in a pan, add onions and garlic, and cook until softened.",
                "Step 4: Add ground beef, cook until browned, then stir in tomatoes, tomato paste, oregano, cinnamon, salt, and pepper. Simmer for 20 minutes.",
                "Step 5: For the béchamel sauce, melt butter in a pan, stir in flour, and cook for 2 minutes. Gradually whisk in milk and cook until thickened. Remove from heat, beat in eggs, and mix in Parmesan cheese.",
                "Step 6: In a baking dish, layer eggplant slices, meat sauce, and béchamel sauce.",
                "Step 7: Bake for 45-50 minutes until golden brown and bubbling. Let cool slightly before serving."
            ]
        },
        "origin": "Greece",
        "history": "Moussaka is a traditional Greek casserole, known for its layers of eggplant, spiced meat sauce, and creamy béchamel, with influences from Middle Eastern cuisine."
    },
    {
        "country": "Greece",
        "dish": "Souvlaki",
        "recipe": {
            "ingredients": [
                "500g pork or chicken, cut into cubes",
                "3 tbsp olive oil",
                "2 tbsp lemon juice",
                "2 cloves garlic, minced",
                "1 tsp dried oregano",
                "Salt and black pepper to taste",
                "Pita bread and tzatziki for serving"
            ],
            "instructions": [
                "Step 1: In a bowl, mix olive oil, lemon juice, garlic, oregano, salt, and pepper.",
                "Step 2: Marinate the meat in the mixture for at least 1 hour.",
                "Step 3: Thread the meat onto skewers.",
                "Step 4: Grill over medium heat for 8-10 minutes, turning occasionally, until cooked through.",
                "Step 5: Serve with pita bread and tzatziki sauce."
            ]
        },
        "origin": "Greece",
        "history": "Souvlaki is a popular Greek street food consisting of grilled meat skewers, often served with pita and tzatziki. It's a staple of Greek fast food and barbecue culture."
    },
    {
        "country": "Greece",
        "dish": "Spanakopita",
        "recipe": {
            "ingredients": [
                "500g fresh spinach, chopped",
                "200g feta cheese, crumbled",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "1/4 cup olive oil",
                "2 large eggs",
                "12 sheets phyllo dough",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Preheat oven to 190°C (375°F).",
                "Step 2: Heat olive oil in a pan, add onions and garlic, and cook until softened.",
                "Step 3: Add spinach and cook until wilted. Remove from heat and let cool.",
                "Step 4: Mix in feta cheese and eggs. Season with salt and pepper.",
                "Step 5: Brush a baking dish with olive oil and layer with 6 sheets of phyllo dough, brushing each sheet with oil.",
                "Step 6: Spread the spinach mixture over the phyllo dough, then top with remaining 6 sheets of phyllo, brushing each with oil.",
                "Step 7: Bake for 30-35 minutes until golden and crisp. Cool slightly before serving."
            ]
        },
        "origin": "Greece",
        "history": "Spanakopita is a savory Greek pastry made with spinach and feta cheese wrapped in crispy phyllo dough, traditionally enjoyed as a snack or appetizer."
    },
    {
        "country": "Greece",
        "dish": "Tzatziki",
        "recipe": {
            "ingredients": [
                "500g Greek yogurt",
                "1 cucumber, grated and drained",
                "2 cloves garlic, minced",
                "2 tbsp olive oil",
                "1 tbsp lemon juice",
                "1 tbsp chopped fresh dill",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: In a bowl, combine Greek yogurt, grated cucumber, garlic, olive oil, lemon juice, and dill.",
                "Step 2: Mix well and season with salt and pepper.",
                "Step 3: Chill in the refrigerator for at least 1 hour before serving."
            ]
        },
        "origin": "Greece",
        "history": "Tzatziki is a refreshing Greek dip made from yogurt, cucumber, and garlic, often served as an appetizer or accompaniment to grilled meats."
    },
    {
        "country": "Greece",
        "dish": "Dolmades",
        "recipe": {
            "ingredients": [
                "1 jar grape leaves, drained",
                "200g ground beef",
                "100g rice",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp olive oil",
                "1 tsp dried dill",
                "1 tsp dried mint",
                "1/2 cup pine nuts",
                "Salt and black pepper to taste",
                "1 lemon, juiced"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a pan, add onions and garlic, and cook until softened.",
                "Step 2: Add ground beef and cook until browned.",
                "Step 3: Stir in rice, dill, mint, pine nuts, salt, and pepper, and cook for 5 minutes.",
                "Step 4: Place a spoonful of filling in each grape leaf, fold sides, and roll up tightly.",
                "Step 5: Place dolmades seam side down in a pot, cover with water, and add lemon juice.",
                "Step 6: Simmer for 30-40 minutes until rice is cooked and leaves are tender."
            ]
        },
        "origin": "Greece",
        "history": "Dolmades are grape leaves stuffed with a savory mixture of rice, meat, and spices, traditionally enjoyed as a part of Greek mezze or as a main dish."
    },
    {
        "country": "Greece",
        "dish": "Gyro",
        "recipe": {
            "ingredients": [
                "500g pork or chicken, thinly sliced",
                "3 tbsp olive oil",
                "2 tbsp lemon juice",
                "2 cloves garlic, minced",
                "1 tsp dried oregano",
                "Salt and black pepper to taste",
                "Pita bread and tzatziki for serving"
            ],
            "instructions": [
                "Step 1: Marinate the meat in a mixture of olive oil, lemon juice, garlic, oregano, salt, and pepper for at least 1 hour.",
                "Step 2: Grill or pan-fry the meat over medium heat until cooked through and crispy.",
                "Step 3: Slice thinly and serve in pita bread with tzatziki sauce."
            ]
        },
        "origin": "Greece",
        "history": "Gyro is a popular Greek street food made with seasoned, grilled meat, usually served in pita bread with fresh vegetables and tzatziki sauce."
    },
    {
        "country": "Greece",
        "dish": "Saganaki",
        "recipe": {
            "ingredients": [
                "200g Kasseri or other Greek cheese, sliced",
                "1/4 cup all-purpose flour",
                "2 eggs, beaten",
                "1/2 cup breadcrumbs",
                "Vegetable oil for frying",
                "Lemon wedges for serving"
            ],
            "instructions": [
                "Step 1: Dredge cheese slices in flour, then dip in beaten eggs, and coat with breadcrumbs.",
                "Step 2: Heat vegetable oil in a pan over medium heat.",
                "Step 3: Fry the cheese slices until golden brown and crispy, about 2 minutes per side.",
                "Step 4: Drain on paper towels and serve with lemon wedges."
            ]
        },
        "origin": "Greece",
        "history": "Saganaki is a Greek appetizer featuring fried cheese, typically enjoyed with a squeeze of lemon juice. It's named after the small frying pan used to cook it."
    },
    {
        "country": "Greece",
        "dish": "Fasolada",
        "recipe": {
            "ingredients": [
                "1 cup dried beans (such as cannellini or kidney beans), soaked overnight",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "2 carrots, sliced",
                "2 celery stalks, sliced",
                "400g canned tomatoes, chopped",
                "2 tbsp olive oil",
                "1 tsp dried oregano",
                "Salt and black pepper to taste",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: Drain and rinse soaked beans. Cook in a pot with fresh water until tender, about 1 hour.",
                "Step 2: In another pot, heat olive oil and sauté onions, garlic, carrots, and celery until softened.",
                "Step 3: Add tomatoes, oregano, salt, and pepper. Cook for 10 minutes.",
                "Step 4: Add cooked beans and simmer for 20 minutes.",
                "Step 5: Garnish with chopped parsley before serving."
            ]
        },
        "origin": "Greece",
        "history": "Fasolada is a traditional Greek bean soup, often considered a national dish. It's hearty and nutritious, typically enjoyed during cooler months."
    },
    {
        "country": "Greece",
        "dish": "Baklava",
        "recipe": {
            "ingredients": [
                "250g phyllo dough",
                "200g walnuts, finely chopped",
                "100g almonds, finely chopped",
                "1 tsp ground cinnamon",
                "200g unsalted butter, melted",
                "200g granulated sugar",
                "200ml water",
                "100g honey"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F).",
                "Step 2: Mix walnuts, almonds, and cinnamon in a bowl.",
                "Step 3: Brush a baking dish with melted butter. Layer 8 sheets of phyllo dough, brushing each sheet with butter.",
                "Step 4: Spread a layer of nut mixture over the phyllo. Add another 8 sheets of phyllo, brushing each with butter.",
                "Step 5: Cut into diamond shapes and bake for 45-50 minutes until golden and crisp.",
                "Step 6: In a saucepan, combine sugar, water, and honey. Bring to a boil, then simmer for 10 minutes.",
                "Step 7: Pour the hot syrup over the baked baklava. Let cool before serving."
            ]
        },
        "origin": "Greece",
        "history": "Baklava is a sweet pastry made with layers of phyllo dough, nuts, and honey, known for its rich, sweet flavor and flaky texture."
    },
    {
        "country": "Greece",
        "dish": "Horiatiki (Greek Salad)",
        "recipe": {
            "ingredients": [
                "4 ripe tomatoes, cut into wedges",
                "1 cucumber, sliced",
                "1 red onion, sliced",
                "200g feta cheese, crumbled",
                "100g Kalamata olives",
                "60ml olive oil",
                "1 tsp dried oregano",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: In a large bowl, combine tomatoes, cucumber, red onion, feta cheese, and olives.",
                "Step 2: Drizzle with olive oil and sprinkle with oregano, salt, and pepper.",
                "Step 3: Toss gently to combine and serve immediately."
            ]
        },
        "origin": "Greece",
        "history": "Horiatiki, or Greek Salad, is a traditional Greek salad featuring fresh vegetables, feta cheese, and olives, typically enjoyed as a refreshing appetizer or side dish."
    },
    {
        "country": "Portugal",
        "dish": "Bacalhau à Brás",
        "recipe": {
            "ingredients": [
                "500g salt cod (bacalhau), desalted and shredded",
                "4 large potatoes, peeled and julienned",
                "1 onion, finely chopped",
                "2 cloves garlic, minced",
                "4 large eggs, beaten",
                "100g black olives",
                "2 tbsp olive oil",
                "Salt and black pepper to taste",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a pan and fry the potatoes until crispy. Drain on paper towels.",
                "Step 2: In the same pan, sauté onions and garlic until translucent.",
                "Step 3: Add shredded salt cod and cook for 5 minutes.",
                "Step 4: Add the fried potatoes and mix well.",
                "Step 5: Pour in the beaten eggs and cook, stirring gently, until eggs are just set.",
                "Step 6: Season with salt and pepper, garnish with olives and parsley, and serve."
            ]
        },
        "origin": "Portugal",
        "history": "Bacalhau à Brás is a traditional Portuguese dish made with shredded cod, potatoes, and eggs. It's a classic way to prepare cod, which is a staple in Portuguese cuisine."
    },
    {
        "country": "Portugal",
        "dish": "Caldo Verde",
        "recipe": {
            "ingredients": [
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp olive oil",
                "500g potatoes, peeled and diced",
                "1 liter chicken or vegetable broth",
                "200g kale, thinly sliced",
                "200g chorizo sausage, sliced",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a pot and sauté onions and garlic until softened.",
                "Step 2: Add diced potatoes and cook for 5 minutes.",
                "Step 3: Pour in the broth and bring to a boil. Reduce heat and simmer until potatoes are tender.",
                "Step 4: Use an immersion blender to blend the soup until smooth.",
                "Step 5: Stir in the kale and chorizo and cook for 5 minutes until kale is wilted.",
                "Step 6: Season with salt and pepper and serve hot."
            ]
        },
        "origin": "Portugal",
        "history": "Caldo Verde is a traditional Portuguese soup made with kale, potatoes, and chorizo. It's a comforting and hearty dish, often enjoyed as a starter or light meal."
    },
    {
        "country": "Portugal",
        "dish": "Bacalhau à Gomes de Sá",
        "recipe": {
            "ingredients": [
                "500g salt cod (bacalhau), desalted and flaked",
                "4 large potatoes, peeled and sliced",
                "1 onion, thinly sliced",
                "2 cloves garlic, minced",
                "2 tbsp olive oil",
                "100g black olives",
                "2 tbsp chopped fresh parsley",
                "2 large eggs, hard-boiled and sliced",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F).",
                "Step 2: In a pan, heat olive oil and sauté onions and garlic until soft.",
                "Step 3: Layer sliced potatoes in a baking dish, followed by cod, onions, and garlic.",
                "Step 4: Bake for 30 minutes until potatoes are tender.",
                "Step 5: Garnish with olives, parsley, and sliced hard-boiled eggs before serving."
            ]
        },
        "origin": "Portugal",
        "history": "Bacalhau à Gomes de Sá is a traditional Portuguese dish made with salt cod, potatoes, and onions. It's named after its creator, José Gomes de Sá, a Portuguese restaurateur."
    },
    {
        "country": "Portugal",
        "dish": "Arroz de Marisco",
        "recipe": {
            "ingredients": [
                "200g shrimp, peeled and deveined",
                "200g clams, scrubbed",
                "200g mussels, scrubbed",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "1 red bell pepper, chopped",
                "400g canned tomatoes, chopped",
                "250g rice",
                "1 liter seafood or chicken broth",
                "2 tbsp olive oil",
                "1 tsp paprika",
                "Salt and black pepper to taste",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a pot and sauté onions, garlic, and bell pepper until softened.",
                "Step 2: Add tomatoes, paprika, and rice, and cook for 2 minutes.",
                "Step 3: Pour in the broth and bring to a boil. Reduce heat and simmer for 15 minutes.",
                "Step 4: Stir in the seafood and cook for an additional 10 minutes until cooked through.",
                "Step 5: Season with salt and pepper, garnish with parsley, and serve."
            ]
        },
        "origin": "Portugal",
        "history": "Arroz de Marisco is a Portuguese seafood rice dish, often enjoyed as a hearty and flavorful meal. It's a celebration of the rich maritime resources of Portugal."
    },
    {
        "country": "Portugal",
        "dish": "Pasteis de Nata",
        "recipe": {
            "ingredients": [
                "1 sheet puff pastry",
                "300ml whole milk",
                "200g granulated sugar",
                "6 large egg yolks",
                "2 tbsp all-purpose flour",
                "1 tsp vanilla extract",
                "1 tsp ground cinnamon",
                "Powdered sugar for dusting"
            ],
            "instructions": [
                "Step 1: Preheat oven to 220°C (425°F).",
                "Step 2: Roll out the puff pastry and cut into circles to fit a muffin tin.",
                "Step 3: Press pastry circles into the muffin tin to form cups.",
                "Step 4: In a saucepan, heat milk and sugar until just boiling. In a bowl, whisk egg yolks and flour together.",
                "Step 5: Gradually whisk the hot milk into the egg yolk mixture, then return to the saucepan and cook until thickened.",
                "Step 6: Stir in vanilla extract and ground cinnamon.",
                "Step 7: Pour custard into the pastry cups and bake for 15-20 minutes until golden and puffed.",
                "Step 8: Dust with powdered sugar before serving."
            ]
        },
        "origin": "Portugal",
        "history": "Pasteis de Nata, or Portuguese custard tarts, are a beloved Portuguese pastry with a crisp pastry shell and creamy custard filling. They are often enjoyed with a sprinkle of cinnamon and powdered sugar."
    },
    {
        "country": "Portugal",
        "dish": "Feijoada",
        "recipe": {
            "ingredients": [
                "300g black beans, soaked overnight",
                "200g pork shoulder, cubed",
                "150g chorizo sausage, sliced",
                "150g bacon, diced",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "2 bay leaves",
                "1 tsp paprika",
                "Salt and black pepper to taste",
                "2 tbsp olive oil",
                "Rice for serving"
            ],
            "instructions": [
                "Step 1: In a large pot, heat olive oil and sauté onions and garlic until softened.",
                "Step 2: Add pork, chorizo, and bacon, and cook until browned.",
                "Step 3: Stir in soaked beans, bay leaves, paprika, salt, and pepper.",
                "Step 4: Cover with water and simmer for 1.5-2 hours until beans and meat are tender.",
                "Step 5: Serve over rice."
            ]
        },
        "origin": "Portugal",
        "history": "Feijoada is a traditional Portuguese stew made with black beans, various meats, and spices. It's a hearty and flavorful dish, often enjoyed as a communal meal."
    },
    {
        "country": "Portugal",
        "dish": "Cataplana de Mariscos",
        "recipe": {
            "ingredients": [
                "200g shrimp, peeled and deveined",
                "200g clams, scrubbed",
                "200g mussels, scrubbed",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "1 red bell pepper, chopped",
                "200g canned tomatoes, chopped",
                "1/2 cup white wine",
                "2 tbsp olive oil",
                "1 tsp paprika",
                "Salt and black pepper to taste",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat olive oil in a cataplana or large pot and sauté onions, garlic, and bell pepper until softened.",
                "Step 2: Add tomatoes, paprika, and white wine. Simmer for 10 minutes.",
                "Step 3: Add seafood and cook until shells open and shrimp are cooked through.",
                "Step 4: Season with salt and pepper, garnish with parsley, and serve."
            ]
        },
        "origin": "Portugal",
        "history": "Cataplana de Mariscos is a traditional Portuguese seafood stew cooked in a cataplana, a clam-shaped copper pot. It highlights the rich seafood tradition of Portugal."
    },
    {
        "country": "Portugal",
        "dish": "Prego no Pão",
        "recipe": {
            "ingredients": [
                "500g beef steak, thinly sliced",
                "4 cloves garlic, minced",
                "2 tbsp olive oil",
                "4 rolls of Portuguese bread",
                "Salt and black pepper to taste",
                "Chopped parsley for garnish"
            ],
            "instructions": [
                "Step 1: Marinate beef with garlic, olive oil, salt, and pepper for at least 1 hour.",
                "Step 2: Grill or pan-fry beef until cooked to your liking.",
                "Step 3: Toast the bread rolls and fill with the cooked beef.",
                "Step 4: Garnish with chopped parsley and serve."
            ]
        },
        "origin": "Portugal",
        "history": "Prego no Pão is a Portuguese sandwich made with marinated and grilled beef, served in a crusty roll. It's a popular street food and casual meal in Portugal."
    },
    {
        "country": "Portugal",
        "dish": "Bacalhau com Natas",
        "recipe": {
            "ingredients": [
                "500g salt cod (bacalhau), desalted and flaked",
                "4 large potatoes, peeled and diced",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "200ml heavy cream",
                "2 large eggs",
                "2 tbsp olive oil",
                "Salt and black pepper to taste",
                "Grated cheese for topping"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F).",
                "Step 2: In a pan, heat olive oil and sauté onions and garlic until softened.",
                "Step 3: Add potatoes and cook for 5 minutes.",
                "Step 4: Stir in cod and cook for another 5 minutes.",
                "Step 5: In a bowl, mix cream and eggs, then pour over the cod and potato mixture.",
                "Step 6: Transfer to a baking dish, top with grated cheese, and bake for 30-35 minutes until golden and bubbling."
            ]
        },
        "origin": "Portugal",
        "history": "Bacalhau com Natas is a Portuguese casserole made with salt cod, potatoes, and a creamy sauce. It's a rich and comforting dish, showcasing the versatility of bacalhau."
    },
    {
        "country": "Portugal",
        "dish": "Francesinha",
        "recipe": {
            "ingredients": [
                "4 slices of bread",
                "500g beef steak, grilled",
                "100g ham",
                "4 slices cheese",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "400ml tomato sauce",
                "200ml beef broth",
                "2 tbsp olive oil",
                "1 tbsp flour",
                "Salt and black pepper to taste",
                "1 egg for frying (optional)"
            ],
            "instructions": [
                "Step 1: In a pan, heat olive oil and sauté onions and garlic until softened.",
                "Step 2: Stir in flour and cook for 1 minute.",
                "Step 3: Add tomato sauce and beef broth, and simmer for 10 minutes until thickened.",
                "Step 4: Place a slice of bread in a baking dish, top with steak, ham, and cheese, then cover with another slice of bread.",
                "Step 5: Pour sauce over the sandwich and bake for 15 minutes at 200°C (400°F).",
                "Step 6: Fry an egg if desired and place on top of the sandwich before serving."
            ]
        },
        "origin": "Portugal",
        "history": "Francesinha, or 'Little Frenchie', is a Portuguese sandwich featuring layers of meat, cheese, and a rich tomato-beef sauce. It's a hearty and indulgent dish, often enjoyed with a fried egg on top."
    },
    {
        "country": "Sweden",
        "dish": "Köttbullar (Swedish Meatballs)",
        "recipe": {
            "ingredients": [
                "500g ground beef",
                "250g ground pork",
                "1 onion, finely chopped",
                "1 clove garlic, minced",
                "1 egg",
                "50g breadcrumbs",
                "100ml milk",
                "1/2 tsp ground allspice",
                "1/2 tsp ground nutmeg",
                "Salt and black pepper to taste",
                "2 tbsp butter for frying"
            ],
            "instructions": [
                "Step 1: In a large bowl, combine ground beef, ground pork, onion, garlic, egg, breadcrumbs, and milk.",
                "Step 2: Season with allspice, nutmeg, salt, and pepper. Mix until well combined.",
                "Step 3: Form the mixture into small meatballs.",
                "Step 4: Heat butter in a pan over medium heat and fry the meatballs until browned and cooked through, about 10 minutes.",
                "Step 5: Serve with lingonberry sauce and creamy mashed potatoes."
            ]
        },
        "origin": "Sweden",
        "history": "Köttbullar, or Swedish meatballs, are a traditional Swedish dish commonly served with lingonberry sauce and creamy mashed potatoes. They are a staple of Swedish cuisine and are often enjoyed during holidays and special occasions."
    },
    {
        "country": "Sweden",
        "dish": "Gravlax",
        "recipe": {
            "ingredients": [
                "500g salmon fillet, skin on",
                "50g granulated sugar",
                "50g salt",
                "1 tbsp crushed black pepper",
                "1 bunch fresh dill, chopped",
                "1 tbsp mustard seeds (optional)"
            ],
            "instructions": [
                "Step 1: Mix sugar, salt, black pepper, and mustard seeds (if using) in a bowl.",
                "Step 2: Rub the mixture all over the salmon fillet.",
                "Step 3: Place the salmon in a dish, cover with chopped dill, and wrap tightly with plastic wrap.",
                "Step 4: Refrigerate for 48 hours, turning the salmon occasionally.",
                "Step 5: Rinse the salmon under cold water, pat dry, and slice thinly to serve."
            ]
        },
        "origin": "Sweden",
        "history": "Gravlax is a traditional Scandinavian dish made from raw salmon cured with a mixture of salt, sugar, and dill. It is commonly served with mustard sauce and crispbread."
    },
    {
        "country": "Sweden",
        "dish": "Kanelbullar (Cinnamon Buns)",
        "recipe": {
            "ingredients": [
                "500g all-purpose flour",
                "75g sugar",
                "1 tsp ground cinnamon",
                "1/2 tsp salt",
                "75g butter, melted",
                "200ml milk, warmed",
                "25g fresh yeast or 1 packet active dry yeast",
                "1 egg",
                "For filling: 75g butter, softened, 50g sugar, 1 tbsp ground cinnamon",
                "1 egg for brushing",
                "Pearl sugar for sprinkling"
            ],
            "instructions": [
                "Step 1: Dissolve yeast in warm milk. Mix flour, sugar, cinnamon, and salt in a bowl.",
                "Step 2: Add melted butter, egg, and yeast mixture. Knead into a smooth dough and let rise for 1 hour.",
                "Step 3: Roll out the dough into a rectangle and spread with softened butter, sugar, and cinnamon.",
                "Step 4: Roll up the dough tightly and slice into pieces. Place on a baking sheet.",
                "Step 5: Let rise for another 30 minutes. Brush with beaten egg and sprinkle with pearl sugar.",
                "Step 6: Bake at 225°C (435°F) for 8-10 minutes until golden brown."
            ]
        },
        "origin": "Sweden",
        "history": "Kanelbullar, or Swedish cinnamon buns, are a beloved Swedish pastry enjoyed with coffee or tea. They are often made for special occasions and are a popular part of Swedish fika culture."
    },
    {
        "country": "Sweden",
        "dish": "Sill (Pickled Herring)",
        "recipe": {
            "ingredients": [
                "4-6 pickled herring fillets",
                "1 onion, thinly sliced",
                "1/2 cup white vinegar",
                "1/2 cup water",
                "1/2 cup sugar",
                "1 tsp whole black peppercorns",
                "1 tsp mustard seeds",
                "1 bay leaf",
                "Fresh dill for garnish"
            ],
            "instructions": [
                "Step 1: Mix vinegar, water, sugar, peppercorns, mustard seeds, and bay leaf in a saucepan. Bring to a boil and let cool.",
                "Step 2: Place herring fillets and onions in a jar.",
                "Step 3: Pour the cooled pickling liquid over the herring and onions.",
                "Step 4: Seal the jar and refrigerate for at least 3 days before serving.",
                "Step 5: Garnish with fresh dill before serving."
            ]
        },
        "origin": "Sweden",
        "history": "Sill, or pickled herring, is a traditional Swedish dish commonly served during holidays and special occasions. It is often enjoyed as part of the Swedish smorgasbord, or buffet."
    },
    {
        "country": "Sweden",
        "dish": "Raggmunk (Potato Pancakes)",
        "recipe": {
            "ingredients": [
                "500g potatoes, peeled and grated",
                "1 onion, grated",
                "1 egg",
                "2 tbsp all-purpose flour",
                "Salt and black pepper to taste",
                "Butter for frying",
                "Lingonberry sauce for serving"
            ],
            "instructions": [
                "Step 1: In a bowl, mix grated potatoes, onion, egg, flour, salt, and pepper.",
                "Step 2: Heat butter in a frying pan over medium heat.",
                "Step 3: Spoon the potato mixture into the pan, flattening into pancakes.",
                "Step 4: Fry until golden brown and crispy on both sides, about 3-4 minutes per side.",
                "Step 5: Serve hot with lingonberry sauce."
            ]
        },
        "origin": "Sweden",
        "history": "Raggmunk are crispy potato pancakes, a traditional Swedish dish often enjoyed with lingonberry sauce and sour cream. They are a comforting and hearty part of Swedish cuisine."
    },
    {
        "country": "Sweden",
        "dish": "Janssons Frestelse (Jansson's Temptation)",
        "recipe": {
            "ingredients": [
                "500g potatoes, peeled and thinly sliced",
                "1 onion, finely chopped",
                "100g anchovy fillets, chopped",
                "300ml heavy cream",
                "2 tbsp butter",
                "Salt and black pepper to taste",
                "Breadcrumbs for topping"
            ],
            "instructions": [
                "Step 1: Preheat oven to 200°C (390°F).",
                "Step 2: In a greased baking dish, layer potatoes, onions, and anchovies.",
                "Step 3: Pour cream over the layers and season with salt and pepper.",
                "Step 4: Dot with butter and sprinkle breadcrumbs on top.",
                "Step 5: Bake for 45-50 minutes until potatoes are tender and top is golden brown."
            ]
        },
        "origin": "Sweden",
        "history": "Janssons Frestelse is a classic Swedish casserole made with potatoes, anchovies, and cream. It is a popular dish during Christmas and other festive occasions."
    },
    {
        "country": "Sweden",
        "dish": "Kåldolmar (Stuffed Cabbage Rolls)",
        "recipe": {
            "ingredients": [
                "1 large cabbage",
                "500g ground beef",
                "250g ground pork",
                "1 onion, finely chopped",
                "1 egg",
                "100g rice, cooked",
                "Salt and black pepper to taste",
                "Butter for frying",
                "1 cup beef broth",
                "1 cup tomato sauce"
            ],
            "instructions": [
                "Step 1: Boil cabbage in salted water until leaves are pliable. Drain and let cool.",
                "Step 2: In a bowl, mix ground beef, ground pork, onion, egg, cooked rice, salt, and pepper.",
                "Step 3: Place a spoonful of filling on each cabbage leaf and roll up, tucking in the sides.",
                "Step 4: Heat butter in a pan and brown the cabbage rolls on all sides.",
                "Step 5: Place rolls in a baking dish, pour beef broth and tomato sauce over them.",
                "Step 6: Cover and bake at 180°C (350°F) for 1 hour."
            ]
        },
        "origin": "Sweden",
        "history": "Kåldolmar are Swedish stuffed cabbage rolls, traditionally made with a mixture of ground meats and rice, and baked in a savory sauce. They are often enjoyed as a hearty main dish."
    },
    {
        "country": "Sweden",
        "dish": "Prinsesstårta (Princess Cake)",
        "recipe": {
            "ingredients": [
                "For the sponge cake:",
                "4 eggs",
                "200g granulated sugar",
                "200g all-purpose flour",
                "2 tsp baking powder",
                "For the filling:",
                "200g raspberry jam",
                "500ml heavy cream",
                "2 tbsp powdered sugar",
                "For the frosting:",
                "500g marzipan",
                "Green food coloring",
                "Powdered sugar for dusting"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F). Grease and line a cake pan.",
                "Step 2: Beat eggs and sugar until thick and pale. Fold in flour and baking powder.",
                "Step 3: Pour batter into the prepared pan and bake for 25-30 minutes. Let cool.",
                "Step 4: Split the cake horizontally and spread raspberry jam on the bottom layer.",
                "Step 5: Whip heavy cream with powdered sugar and spread over the jam layer.",
                "Step 6: Place the top layer of cake on top and cover with marzipan, colored green.",
                "Step 7: Dust with powdered sugar and decorate as desired."
            ]
        },
        "origin": "Sweden",
        "history": "Prinsesstårta, or Princess Cake, is a classic Swedish dessert made with sponge cake, raspberry jam, whipped cream, and marzipan. It is a popular choice for celebrations and special occasions."
    },
    {
        "country": "Sweden",
        "dish": "Silltårta (Herring Cake)",
        "recipe": {
            "ingredients": [
                "200g pickled herring, chopped",
                "200g sour cream",
                "100g mayonnaise",
                "1/2 cup finely chopped red onion",
                "2 tbsp capers",
                "1 tbsp chopped fresh dill",
                "Salt and black pepper to taste",
                "Sliced rye bread for serving"
            ],
            "instructions": [
                "Step 1: In a bowl, mix sour cream, mayonnaise, onion, capers, dill, salt, and pepper.",
                "Step 2: Stir in the chopped pickled herring.",
                "Step 3: Chill in the refrigerator for at least 1 hour before serving.",
                "Step 4: Serve on sliced rye bread."
            ]
        },
        "origin": "Sweden",
        "history": "Silltårta is a traditional Swedish herring cake made with pickled herring and a creamy sauce. It is often served as a part of the Swedish smorgasbord or during special occasions."
    },
    {
        "country": "Sweden",
        "dish": "Rödbetssallad (Beetroot Salad)",
        "recipe": {
            "ingredients": [
                "500g cooked beetroots, peeled and diced",
                "200g cooked potatoes, diced",
                "1/2 cup finely chopped onion",
                "1/2 cup mayonnaise",
                "1/2 cup sour cream",
                "Salt and black pepper to taste",
                "Chopped fresh dill for garnish"
            ],
            "instructions": [
                "Step 1: In a large bowl, combine diced beetroots, potatoes, and onion.",
                "Step 2: Mix mayonnaise and sour cream in a separate bowl and fold into the beetroot mixture.",
                "Step 3: Season with salt and pepper.",
                "Step 4: Garnish with chopped fresh dill before serving."
            ]
        },
        "origin": "Sweden",
        "history": "Rödbetssallad, or beetroot salad, is a popular Swedish dish made with beetroots, potatoes, and a creamy dressing. It is commonly served as a side dish during festive meals and celebrations."
    },
    {
        "country": "Hungary",
        "dish": "Gulyás (Goulash)",
        "recipe": {
            "ingredients": [
                "500g beef chuck, cut into cubes",
                "2 tbsp vegetable oil",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp sweet paprika",
                "1 tsp caraway seeds",
                "1 bell pepper, chopped",
                "2 tomatoes, chopped",
                "3 medium potatoes, peeled and diced",
                "1 liter beef broth",
                "Salt and black pepper to taste",
                "Chopped fresh parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium heat. Add onions and garlic and sauté until softened.",
                "Step 2: Add beef cubes and brown on all sides.",
                "Step 3: Stir in paprika and caraway seeds, then add bell pepper and tomatoes. Cook for 5 minutes.",
                "Step 4: Pour in beef broth and bring to a boil. Reduce heat and simmer for 1 hour.",
                "Step 5: Add potatoes and cook until tender, about 20 minutes.",
                "Step 6: Season with salt and pepper. Garnish with chopped parsley before serving."
            ]
        },
        "origin": "Hungary",
        "history": "Gulyás, or goulash, is a traditional Hungarian stew made with beef, paprika, and vegetables. It has a rich history as a staple dish in Hungarian cuisine and is enjoyed across Central Europe."
    },
    {
        "country": "Hungary",
        "dish": "Pörkölt (Hungarian Stew)",
        "recipe": {
            "ingredients": [
                "500g pork shoulder, cut into cubes",
                "2 tbsp vegetable oil",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp sweet paprika",
                "1 bell pepper, chopped",
                "2 tomatoes, chopped",
                "1 cup beef broth",
                "Salt and black pepper to taste",
                "Chopped fresh parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium heat. Add onions and garlic and sauté until softened.",
                "Step 2: Add pork cubes and brown on all sides.",
                "Step 3: Stir in paprika, bell pepper, and tomatoes. Cook for 5 minutes.",
                "Step 4: Pour in beef broth and bring to a boil. Reduce heat and simmer for 1 hour.",
                "Step 5: Season with salt and pepper. Garnish with chopped parsley before serving."
            ]
        },
        "origin": "Hungary",
        "history": "Pörkölt is a rich and flavorful Hungarian stew made with pork and paprika. It is often served with dumplings or potatoes and is a beloved dish in Hungarian homes."
    },
    {
        "country": "Hungary",
        "dish": "Lángos",
        "recipe": {
            "ingredients": [
                "500g all-purpose flour",
                "10g active dry yeast",
                "250ml warm water",
                "1 tsp sugar",
                "1 tsp salt",
                "2 tbsp vegetable oil",
                "2 cloves garlic, minced",
                "Sour cream and grated cheese for topping"
            ],
            "instructions": [
                "Step 1: Dissolve yeast and sugar in warm water. Let sit for 5 minutes until foamy.",
                "Step 2: In a bowl, mix flour and salt. Add yeast mixture and oil. Knead until smooth.",
                "Step 3: Cover and let rise in a warm place for 1 hour.",
                "Step 4: Divide dough into balls and flatten into discs. Fry in hot oil until golden brown.",
                "Step 5: Rub with minced garlic and top with sour cream and grated cheese."
            ]
        },
        "origin": "Hungary",
        "history": "Lángos is a popular Hungarian street food, a deep-fried flatbread typically enjoyed with garlic, sour cream, and cheese. It is a staple at fairs and markets in Hungary."
    },
    {
        "country": "Hungary",
        "dish": "Töltött Káposzta (Stuffed Cabbage Rolls)",
        "recipe": {
            "ingredients": [
                "1 large cabbage",
                "500g ground pork",
                "100g rice, cooked",
                "1 onion, finely chopped",
                "1 egg",
                "2 tbsp paprika",
                "Salt and black pepper to taste",
                "500ml tomato sauce",
                "1 cup beef broth"
            ],
            "instructions": [
                "Step 1: Boil cabbage in salted water until leaves are pliable. Drain and let cool.",
                "Step 2: In a bowl, mix ground pork, cooked rice, onion, egg, paprika, salt, and pepper.",
                "Step 3: Place a spoonful of filling on each cabbage leaf and roll up, tucking in the sides.",
                "Step 4: Arrange rolls in a baking dish. Pour tomato sauce and beef broth over them.",
                "Step 5: Cover and bake at 180°C (350°F) for 1.5 hours."
            ]
        },
        "origin": "Hungary",
        "history": "Töltött Káposzta, or stuffed cabbage rolls, is a traditional Hungarian dish made with cabbage leaves filled with a pork and rice mixture. It is a hearty and comforting dish often enjoyed during holidays and family gatherings."
    },
    {
        "country": "Hungary",
        "dish": "Halászlé (Fisherman’s Soup)",
        "recipe": {
            "ingredients": [
                "500g freshwater fish (such as carp), cleaned and cut into pieces",
                "2 tbsp vegetable oil",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp sweet paprika",
                "1 bell pepper, chopped",
                "2 tomatoes, chopped",
                "1 liter fish stock",
                "Salt and black pepper to taste",
                "Chopped fresh parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium heat. Add onions and garlic and sauté until softened.",
                "Step 2: Stir in paprika, bell pepper, and tomatoes. Cook for 5 minutes.",
                "Step 3: Add fish pieces and pour in fish stock. Bring to a boil.",
                "Step 4: Reduce heat and simmer for 30 minutes.",
                "Step 5: Season with salt and pepper. Garnish with chopped parsley before serving."
            ]
        },
        "origin": "Hungary",
        "history": "Halászlé, or Fisherman’s Soup, is a traditional Hungarian soup made with freshwater fish and paprika. It is a popular dish in Hungary, especially in regions with a strong fishing tradition."
    },
    {
        "country": "Hungary",
        "dish": "Pálinka (Hungarian Fruit Brandy)",
        "recipe": {
            "ingredients": [
                "2 kg ripe fruit (such as plums, apricots, or pears)",
                "500g sugar",
                "1 packet of yeast",
                "Water (as needed)"
            ],
            "instructions": [
                "Step 1: Wash and chop the fruit. Place in a large fermentation vessel.",
                "Step 2: Dissolve sugar in a small amount of water and add to the fruit.",
                "Step 3: Sprinkle yeast over the fruit and mix well.",
                "Step 4: Cover and let ferment in a warm place for 2-3 weeks, stirring occasionally.",
                "Step 5: Strain the liquid and distill to obtain pálinka. Age for several months for best flavor."
            ]
        },
        "origin": "Hungary",
        "history": "Pálinka is a traditional Hungarian fruit brandy made from fermented fruit. It is a cherished part of Hungarian culture and is often enjoyed as a digestif or during special occasions."
    },
    {
        "country": "Hungary",
        "dish": "Lecso (Hungarian Vegetable Stew)",
        "recipe": {
            "ingredients": [
                "3 bell peppers, chopped",
                "2 onions, chopped",
                "2 tomatoes, chopped",
                "2 cloves garlic, minced",
                "2 tbsp sweet paprika",
                "500g sausages, sliced",
                "2 tbsp vegetable oil",
                "Salt and black pepper to taste",
                "Chopped fresh parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium heat. Add onions and garlic and sauté until softened.",
                "Step 2: Stir in paprika, bell peppers, and tomatoes. Cook for 10 minutes.",
                "Step 3: Add sausages and cook until heated through.",
                "Step 4: Season with salt and pepper. Garnish with chopped parsley before serving."
            ]
        },
        "origin": "Hungary",
        "history": "Lecso is a hearty Hungarian vegetable stew made with bell peppers, tomatoes, and sausages. It is a versatile dish that can be served on its own or as a side dish."
    },
    {
        "country": "Hungary",
        "dish": "Dobos Torte (Dobos Cake)",
        "recipe": {
            "ingredients": [
                "For the cake layers:",
                "6 eggs",
                "150g granulated sugar",
                "150g all-purpose flour",
                "1 tsp baking powder",
                "For the filling and frosting:",
                "200g butter, softened",
                "200g granulated sugar",
                "200g dark chocolate, melted",
                "1 tsp vanilla extract",
                "For the topping:",
                "100g dark chocolate, melted",
                "Caramelized sugar slices"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F). Grease and line 6 cake pans.",
                "Step 2: Beat eggs and sugar until thick and pale. Fold in flour and baking powder.",
                "Step 3: Divide batter evenly among the pans and bake for 10-12 minutes. Let cool.",
                "Step 4: For the filling, beat butter, sugar, chocolate, and vanilla until smooth.",
                "Step 5: Spread filling between layers of cake.",
                "Step 6: Frost the top and sides with remaining filling and chill.",
                "Step 7: Decorate with melted chocolate and caramelized sugar slices."
            ]
        },
        "origin": "Hungary",
        "history": "Dobos Torte is a classic Hungarian cake known for its layers of sponge cake and rich chocolate buttercream. It is named after Hungarian pastry chef József C. Dobos, who created the cake in the 19th century."
    },
    {
        "country": "Hungary",
        "dish": "Jókai Bableves (Jókai Bean Soup)",
        "recipe": {
            "ingredients": [
                "200g dried beans, soaked overnight",
                "300g smoked pork ribs",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp sweet paprika",
                "2 bell peppers, chopped",
                "2 tomatoes, chopped",
                "1 liter beef broth",
                "Salt and black pepper to taste",
                "Chopped fresh parsley for garnish"
            ],
            "instructions": [
                "Step 1: In a large pot, cook soaked beans until tender. Drain and set aside.",
                "Step 2: In the same pot, cook smoked pork ribs until browned. Remove and set aside.",
                "Step 3: Add onions and garlic to the pot and sauté until softened.",
                "Step 4: Stir in paprika, bell peppers, and tomatoes. Cook for 5 minutes.",
                "Step 5: Add beans, pork ribs, and beef broth. Bring to a boil, then simmer for 1 hour.",
                "Step 6: Season with salt and pepper. Garnish with chopped parsley before serving."
            ]
        },
        "origin": "Hungary",
        "history": "Jókai Bableves is a hearty Hungarian bean soup named after the famous Hungarian author Mór Jókai. It features beans, smoked pork, and paprika, making it a comforting and flavorful dish."
    },
    {
        "country": "Hungary",
        "dish": "Kürtőskalács (Chimney Cake)",
        "recipe": {
            "ingredients": [
                "500g all-purpose flour",
                "75g sugar",
                "1 packet active dry yeast",
                "250ml warm milk",
                "100g butter, melted",
                "1 egg",
                "1/2 tsp salt",
                "Cinnamon sugar for coating"
            ],
            "instructions": [
                "Step 1: Dissolve yeast in warm milk and let sit for 5 minutes.",
                "Step 2: In a bowl, mix flour, sugar, and salt. Add yeast mixture, melted butter, and egg. Knead until smooth.",
                "Step 3: Cover and let rise in a warm place for 1 hour.",
                "Step 4: Roll out dough and cut into strips. Wrap strips around cylindrical baking molds.",
                "Step 5: Bake at 200°C (390°F) for 15-20 minutes until golden brown.",
                "Step 6: Brush with melted butter and coat with cinnamon sugar."
            ]
        },
        "origin": "Hungary",
        "history": "Kürtőskalács, or chimney cake, is a traditional Hungarian sweet pastry cooked on a rotating spit. It is crispy on the outside and soft on the inside, often enjoyed at fairs and markets."
    },
    {
        "country": "Poland",
        "dish": "Pierogi (Dumplings)",
        "recipe": {
            "ingredients": [
                "For the dough:",
                "500g all-purpose flour",
                "1 egg",
                "200ml sour cream",
                "1/2 tsp salt",
                "For the filling:",
                "300g potatoes, peeled and diced",
                "200g cheese (such as farmer's cheese or ricotta), crumbled",
                "1 onion, finely chopped",
                "2 tbsp vegetable oil",
                "Salt and black pepper to taste",
                "Butter for frying"
            ],
            "instructions": [
                "Step 1: For the dough, mix flour and salt in a bowl. Make a well in the center and add egg and sour cream. Knead until smooth. Cover and let rest for 30 minutes.",
                "Step 2: For the filling, cook potatoes in boiling water until tender. Drain and mash.",
                "Step 3: Heat oil in a pan, sauté onions until golden. Mix with mashed potatoes, cheese, salt, and pepper.",
                "Step 4: Roll out the dough and cut into circles. Place a spoonful of filling in the center of each circle. Fold and seal edges.",
                "Step 5: Boil pierogi in salted water until they float to the surface. Fry in butter until golden brown."
            ]
        },
        "origin": "Poland",
        "history": "Pierogi are traditional Polish dumplings that can be filled with a variety of ingredients. They are a beloved dish in Polish cuisine, often served during holidays and special occasions."
    },
    {
        "country": "Poland",
        "dish": "Bigos (Hunter's Stew)",
        "recipe": {
            "ingredients": [
                "500g sauerkraut, drained",
                "300g fresh cabbage, chopped",
                "300g pork shoulder, cut into cubes",
                "200g kielbasa (Polish sausage), sliced",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp vegetable oil",
                "1 cup beef broth",
                "2 tbsp tomato paste",
                "1 tbsp sweet paprika",
                "1 bay leaf",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium heat. Add onions and garlic and sauté until softened.",
                "Step 2: Add pork cubes and brown on all sides.",
                "Step 3: Stir in sauerkraut, fresh cabbage, kielbasa, beef broth, tomato paste, paprika, bay leaf, salt, and pepper.",
                "Step 4: Bring to a boil, then reduce heat and simmer for 1.5 hours, stirring occasionally.",
                "Step 5: Adjust seasoning as needed and serve hot."
            ]
        },
        "origin": "Poland",
        "history": "Bigos, or Hunter's Stew, is a hearty Polish dish made with sauerkraut, cabbage, and a variety of meats. It is often enjoyed during the colder months and is a staple in Polish cuisine."
    },
    {
        "country": "Poland",
        "dish": "Żurek (Sour Rye Soup)",
        "recipe": {
            "ingredients": [
                "500ml sour rye soup starter (żur)",
                "1 liter beef or vegetable broth",
                "200g kielbasa (Polish sausage), sliced",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp vegetable oil",
                "2 bay leaves",
                "1 tsp dried marjoram",
                "Salt and black pepper to taste",
                "Hard-boiled eggs for garnish"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium heat. Add onions and garlic and sauté until softened.",
                "Step 2: Add kielbasa and cook until browned.",
                "Step 3: Pour in broth and bring to a boil. Add bay leaves and marjoram.",
                "Step 4: Stir in sour rye soup starter and simmer for 30 minutes.",
                "Step 5: Season with salt and pepper. Serve with sliced hard-boiled eggs."
            ]
        },
        "origin": "Poland",
        "history": "Żurek is a traditional Polish soup made from sour rye flour and often served with sausage and hard-boiled eggs. It is a popular dish during Easter and other festive occasions."
    },
    {
        "country": "Poland",
        "dish": "Gołąbki (Stuffed Cabbage Rolls)",
        "recipe": {
            "ingredients": [
                "1 large cabbage",
                "500g ground beef",
                "100g rice, cooked",
                "1 onion, finely chopped",
                "1 egg",
                "2 tbsp tomato paste",
                "1 tsp dried thyme",
                "Salt and black pepper to taste",
                "500ml tomato sauce"
            ],
            "instructions": [
                "Step 1: Boil cabbage in salted water until leaves are pliable. Drain and let cool.",
                "Step 2: In a bowl, mix ground beef, cooked rice, onion, egg, tomato paste, thyme, salt, and pepper.",
                "Step 3: Place a spoonful of filling on each cabbage leaf and roll up, tucking in the sides.",
                "Step 4: Arrange rolls in a baking dish. Pour tomato sauce over them.",
                "Step 5: Cover and bake at 180°C (350°F) for 1.5 hours."
            ]
        },
        "origin": "Poland",
        "history": "Gołąbki, or stuffed cabbage rolls, are a classic Polish dish made with cabbage leaves filled with a meat and rice mixture. They are a comforting and traditional meal often served during family gatherings."
    },
    {
        "country": "Poland",
        "dish": "Placki Ziemniaczane (Potato Pancakes)",
        "recipe": {
            "ingredients": [
                "500g potatoes, peeled and grated",
                "1 onion, grated",
                "1 egg",
                "2 tbsp all-purpose flour",
                "Salt and black pepper to taste",
                "Vegetable oil for frying",
                "Sour cream and applesauce for serving"
            ],
            "instructions": [
                "Step 1: Place grated potatoes in a clean cloth and squeeze out excess moisture.",
                "Step 2: In a bowl, mix potatoes, onion, egg, flour, salt, and pepper.",
                "Step 3: Heat oil in a frying pan over medium heat.",
                "Step 4: Drop spoonfuls of batter into the pan and flatten with a spatula. Fry until golden brown on both sides.",
                "Step 5: Drain on paper towels and serve with sour cream and applesauce."
            ]
        },
        "origin": "Poland",
        "history": "Placki Ziemniaczane, or potato pancakes, are a popular Polish dish made from grated potatoes and onions. They are often served with sour cream or applesauce and are a beloved comfort food in Polish cuisine."
    },
    {
        "country": "Poland",
        "dish": "Kopytka (Potato Dumplings)",
        "recipe": {
            "ingredients": [
                "500g potatoes, peeled and cubed",
                "1 egg",
                "200g all-purpose flour",
                "Salt to taste",
                "Butter for frying",
                "Chopped fresh parsley for garnish"
            ],
            "instructions": [
                "Step 1: Boil potatoes in salted water until tender. Drain and mash.",
                "Step 2: Mix mashed potatoes with egg, flour, and salt to form a dough.",
                "Step 3: Roll dough into a log and cut into small pieces.",
                "Step 4: Cook dumplings in boiling salted water until they float to the surface.",
                "Step 5: Fry in butter until golden brown and garnish with chopped parsley."
            ]
        },
        "origin": "Poland",
        "history": "Kopytka, or potato dumplings, are a traditional Polish dish made from mashed potatoes and flour. They are often served with meat dishes or in a creamy sauce."
    },
    {
        "country": "Poland",
        "dish": "Barszcz (Beet Soup)",
        "recipe": {
            "ingredients": [
                "500g beets, peeled and grated",
                "1 liter beef or vegetable broth",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp vegetable oil",
                "1 tbsp vinegar",
                "1 tsp sugar",
                "Salt and black pepper to taste",
                "Sour cream for serving"
            ],
            "instructions": [
                "Step 1: Heat oil in a pot over medium heat. Add onions and garlic and sauté until softened.",
                "Step 2: Add grated beets and cook for 5 minutes.",
                "Step 3: Pour in broth and bring to a boil. Reduce heat and simmer for 30 minutes.",
                "Step 4: Stir in vinegar, sugar, salt, and pepper.",
                "Step 5: Serve hot with a dollop of sour cream."
            ]
        },
        "origin": "Poland",
        "history": "Barszcz is a traditional Polish beet soup known for its vibrant color and tangy flavor. It is a staple in Polish cuisine and is often served with sour cream and sometimes accompanied by pierogi."
    },
    {
        "country": "Poland",
        "dish": "Żurek (Sour Rye Soup)",
        "recipe": {
            "ingredients": [
                "500ml sour rye starter (żur)",
                "1 liter vegetable broth",
                "200g kielbasa (Polish sausage), sliced",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp vegetable oil",
                "2 bay leaves",
                "1 tsp dried marjoram",
                "Salt and black pepper to taste",
                "Hard-boiled eggs for garnish"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium heat. Add onions and garlic and sauté until softened.",
                "Step 2: Add kielbasa and cook until browned.",
                "Step 3: Pour in broth and bring to a boil. Add bay leaves and marjoram.",
                "Step 4: Stir in sour rye starter and simmer for 30 minutes.",
                "Step 5: Season with salt and pepper. Serve with sliced hard-boiled eggs."
            ]
        },
        "origin": "Poland",
        "history": "Żurek is a traditional Polish soup made from sour rye flour and often served with sausage and hard-boiled eggs. It is a popular dish during Easter and other festive occasions."
    },
    {
        "country": "Poland",
        "dish": "Sernik (Cheesecake)",
        "recipe": {
            "ingredients": [
                "For the crust:",
                "200g digestive biscuits, crushed",
                "100g butter, melted",
                "For the filling:",
                "500g cream cheese",
                "200g granulated sugar",
                "4 eggs",
                "200ml sour cream",
                "1 tsp vanilla extract",
                "1 tbsp all-purpose flour"
            ],
            "instructions": [
                "Step 1: Preheat oven to 175°C (350°F). Mix crushed biscuits with melted butter and press into the bottom of a springform pan.",
                "Step 2: Beat cream cheese with sugar until smooth. Add eggs one at a time, beating well after each addition.",
                "Step 3: Mix in sour cream, vanilla extract, and flour until smooth.",
                "Step 4: Pour filling over the crust and bake for 50-60 minutes.",
                "Step 5: Let cool completely before removing from the pan. Chill before serving."
            ]
        },
        "origin": "Poland",
        "history": "Sernik, or Polish cheesecake, is a popular dessert made with cream cheese and often enjoyed during holidays and special occasions. It has a rich and creamy texture, and can be flavored with various ingredients."
    },
    {
        "country": "Poland",
        "dish": "Kielbasa (Polish Sausage)",
        "recipe": {
            "ingredients": [
                "1 kg pork shoulder, ground",
                "200g beef, ground",
                "5 cloves garlic, minced",
                "2 tbsp sweet paprika",
                "1 tsp black pepper",
                "1 tsp salt",
                "1/2 tsp ground caraway seeds",
                "Sausage casings (optional)"
            ],
            "instructions": [
                "Step 1: In a large bowl, mix ground pork and beef with garlic, paprika, pepper, salt, and caraway seeds.",
                "Step 2: Stuff sausage casings with the meat mixture, if using. Twist into links and tie ends.",
                "Step 3: Smoke or cook sausages according to your preference, either in a smoker or by simmering in water."
            ]
        },
        "origin": "Poland",
        "history": "Kielbasa is a traditional Polish sausage that comes in many varieties. It is a staple in Polish cuisine and can be enjoyed grilled, smoked, or in soups and stews."
    },
    {
        "country": "Poland",
        "dish": "Mizeria (Cucumber Salad)",
        "recipe": {
            "ingredients": [
                "4 cucumbers, sliced",
                "1 cup sour cream",
                "1 tbsp white vinegar",
                "1 tsp sugar",
                "1 tbsp fresh dill, chopped",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Place cucumber slices in a bowl and sprinkle with salt. Let sit for 15 minutes, then drain.",
                "Step 2: In a separate bowl, mix sour cream, vinegar, sugar, dill, salt, and pepper.",
                "Step 3: Toss cucumbers with the sour cream mixture and serve chilled."
            ]
        },
        "origin": "Poland",
        "history": "Mizeria is a refreshing Polish cucumber salad made with sour cream and fresh dill. It is often served as a side dish or accompaniment to meat dishes."
    },
    {
        "country": "Belgium",
        "dish": "Moules-Frites (Mussels with Fries)",
        "recipe": {
            "ingredients": [
                "For the mussels:",
                "1 kg mussels, cleaned and debearded",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "1 stalk celery, chopped",
                "1 cup white wine",
                "1 cup fish or vegetable broth",
                "2 tbsp butter",
                "1 tbsp fresh parsley, chopped",
                "Salt and black pepper to taste",
                "For the fries:",
                "4 large potatoes, peeled and cut into fries",
                "Vegetable oil for frying",
                "Salt to taste"
            ],
            "instructions": [
                "Step 1: For the fries, heat oil in a deep fryer or large pot to 180°C (350°F). Fry potatoes in batches until golden and crispy. Drain on paper towels and season with salt.",
                "Step 2: For the mussels, melt butter in a large pot over medium heat. Add onion, garlic, and celery and cook until softened.",
                "Step 3: Add white wine and broth to the pot and bring to a boil.",
                "Step 4: Add mussels, cover, and cook for 5-7 minutes, or until mussels have opened.",
                "Step 5: Discard any mussels that do not open. Stir in parsley and season with salt and pepper.",
                "Step 6: Serve mussels with fries on the side."
            ]
        },
        "origin": "Belgium",
        "history": "Moules-Frites is a quintessential Belgian dish consisting of steamed mussels served with fries. It is popular throughout Belgium and is often enjoyed in bistros and brasseries."
    },
    {
        "country": "Belgium",
        "dish": "Carbonnade Flamande (Flemish Beef Stew)",
        "recipe": {
            "ingredients": [
                "1 kg beef stew meat, cut into cubes",
                "2 large onions, chopped",
                "2 cloves garlic, minced",
                "2 tbsp vegetable oil",
                "2 tbsp flour",
                "2 cups beef broth",
                "1 cup Belgian beer (such as Dubbel or Tripel)",
                "2 tbsp brown sugar",
                "2 tbsp Dijon mustard",
                "2 bay leaves",
                "1 tsp dried thyme",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium-high heat. Brown beef cubes on all sides. Remove and set aside.",
                "Step 2: Add onions and garlic to the pot and cook until softened.",
                "Step 3: Stir in flour and cook for 2 minutes.",
                "Step 4: Add beef broth, beer, brown sugar, mustard, bay leaves, and thyme. Bring to a boil.",
                "Step 5: Return beef to the pot, reduce heat, cover, and simmer for 2-3 hours, or until beef is tender.",
                "Step 6: Season with salt and pepper before serving."
            ]
        },
        "origin": "Belgium",
        "history": "Carbonnade Flamande is a traditional Flemish beef stew made with Belgian beer. It is a rich and hearty dish, often served with fries or bread."
    },
    {
        "country": "Belgium",
        "dish": "Stoofvlees (Belgian Beef Stew)",
        "recipe": {
            "ingredients": [
                "1 kg beef stew meat, cut into cubes",
                "2 tbsp vegetable oil",
                "3 large onions, chopped",
                "2 cloves garlic, minced",
                "2 tbsp tomato paste",
                "2 cups beef broth",
                "1 cup dark beer",
                "2 tbsp brown sugar",
                "2 tbsp apple cider vinegar",
                "1 tbsp dried thyme",
                "2 bay leaves",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium-high heat. Brown beef cubes on all sides. Remove and set aside.",
                "Step 2: Add onions and garlic to the pot and cook until softened.",
                "Step 3: Stir in tomato paste and cook for 2 minutes.",
                "Step 4: Add beef broth, beer, brown sugar, vinegar, thyme, and bay leaves. Bring to a boil.",
                "Step 5: Return beef to the pot, reduce heat, cover, and simmer for 2-3 hours, or until beef is tender.",
                "Step 6: Season with salt and pepper before serving."
            ]
        },
        "origin": "Belgium",
        "history": "Stoofvlees, or Belgian beef stew, is a classic dish known for its rich flavor from dark beer and slow cooking. It is a beloved comfort food in Belgian cuisine."
    },
    {
        "country": "Belgium",
        "dish": "Waffles",
        "recipe": {
            "ingredients": [
                "250g all-purpose flour",
                "2 tbsp granulated sugar",
                "1 tbsp baking powder",
                "1/2 tsp salt",
                "2 large eggs",
                "200ml milk",
                "100g butter, melted",
                "1 tsp vanilla extract"
            ],
            "instructions": [
                "Step 1: Preheat your waffle iron according to manufacturer's instructions.",
                "Step 2: In a bowl, mix flour, sugar, baking powder, and salt.",
                "Step 3: In another bowl, whisk eggs, milk, melted butter, and vanilla extract.",
                "Step 4: Add wet ingredients to dry ingredients and mix until just combined.",
                "Step 5: Pour batter into preheated waffle iron and cook according to manufacturer's instructions until golden brown."
            ]
        },
        "origin": "Belgium",
        "history": "Belgian waffles are known for their light, airy texture and deep pockets. They are enjoyed with a variety of toppings, such as fresh fruit, whipped cream, or syrup."
    },
    {
        "country": "Belgium",
        "dish": "Moules à la Crème (Mussels in Cream)",
        "recipe": {
            "ingredients": [
                "1 kg mussels, cleaned and debearded",
                "1 large onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp butter",
                "1 cup white wine",
                "1 cup heavy cream",
                "1 tbsp fresh parsley, chopped",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: Melt butter in a large pot over medium heat. Add onion and garlic and cook until softened.",
                "Step 2: Add white wine and bring to a boil.",
                "Step 3: Add mussels, cover, and cook for 5-7 minutes, or until mussels have opened.",
                "Step 4: Discard any mussels that do not open. Stir in cream and parsley.",
                "Step 5: Season with salt and pepper. Serve hot."
            ]
        },
        "origin": "Belgium",
        "history": "Moules à la Crème is a creamy version of the classic mussel dish, highlighting the richness of Belgian cuisine. It is often served with crusty bread."
    },
    {
        "country": "Belgium",
        "dish": "Endives au Gratin (Belgian Endive Gratin)",
        "recipe": {
            "ingredients": [
                "6 endives, trimmed and halved",
                "200g ham, diced",
                "1 cup grated Gruyère cheese",
                "2 tbsp butter",
                "2 tbsp all-purpose flour",
                "1 cup milk",
                "Salt and black pepper to taste",
                "1/2 tsp nutmeg"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F).",
                "Step 2: Cook endives in boiling salted water for 5 minutes. Drain and wrap each in a slice of ham.",
                "Step 3: In a saucepan, melt butter over medium heat. Stir in flour and cook for 2 minutes.",
                "Step 4: Gradually add milk, whisking continuously until smooth. Cook until sauce thickens.",
                "Step 5: Stir in cheese, salt, pepper, and nutmeg.",
                "Step 6: Place wrapped endives in a baking dish, pour sauce over them, and bake for 20-25 minutes until bubbly and golden."
            ]
        },
        "origin": "Belgium",
        "history": "Endives au Gratin is a classic Belgian dish featuring endives wrapped in ham and topped with a creamy cheese sauce. It is a comforting and flavorful dish often enjoyed in Belgian homes."
    },
    {
        "country": "Belgium",
        "dish": "Tarte Tatin",
        "recipe": {
            "ingredients": [
                "6-8 apples, peeled, cored, and halved",
                "150g granulated sugar",
                "100g butter",
                "1 sheet puff pastry",
                "1 tsp vanilla extract",
                "1/2 tsp ground cinnamon"
            ],
            "instructions": [
                "Step 1: Preheat oven to 200°C (400°F).",
                "Step 2: Melt butter and sugar in a skillet over medium heat until caramelized.",
                "Step 3: Arrange apple halves in the caramel and cook for 10 minutes.",
                "Step 4: Remove from heat and place puff pastry over apples, tucking edges down the sides of the skillet.",
                "Step 5: Bake for 25-30 minutes until pastry is golden brown.",
                "Step 6: Let cool slightly before inverting onto a plate."
            ]
        },
        "origin": "Belgium",
        "history": "Tarte Tatin is a caramelized upside-down apple tart that is popular in Belgian dessert menus. Its rich caramel flavor and flaky pastry make it a delightful treat."
    },
    {
        "country": "Belgium",
        "dish": "Speculoos (Spiced Cookies)",
        "recipe": {
            "ingredients": [
                "250g all-purpose flour",
                "100g brown sugar",
                "125g butter, softened",
                "1 egg",
                "1 tsp ground cinnamon",
                "1/2 tsp ground nutmeg",
                "1/4 tsp ground cloves",
                "1/4 tsp baking soda",
                "1/4 tsp salt"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F).",
                "Step 2: Cream together butter and sugar until light and fluffy.",
                "Step 3: Beat in egg and spices.",
                "Step 4: Gradually add flour, baking soda, and salt, mixing until combined.",
                "Step 5: Roll out dough on a floured surface and cut into shapes.",
                "Step 6: Bake for 10-12 minutes until edges are golden. Cool on wire racks."
            ]
        },
        "origin": "Belgium",
        "history": "Speculoos are traditional Belgian spiced cookies, often enjoyed with coffee or tea. They are characterized by their aromatic spices and crisp texture."
    },
    {
        "country": "Belgium",
        "dish": "Waterzooi (Belgian Stew)",
        "recipe": {
            "ingredients": [
                "1 kg chicken, cut into pieces",
                "2 large carrots, sliced",
                "1 leek, chopped",
                "1 onion, chopped",
                "2 cloves garlic, minced",
                "2 tbsp butter",
                "1 liter chicken broth",
                "1 cup heavy cream",
                "1 tbsp fresh parsley, chopped",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: In a large pot, melt butter over medium heat. Add onions, garlic, carrots, and leek and cook until softened.",
                "Step 2: Add chicken pieces and cook until browned.",
                "Step 3: Pour in chicken broth and bring to a boil. Reduce heat and simmer for 30 minutes.",
                "Step 4: Stir in cream and cook for another 10 minutes.",
                "Step 5: Season with salt and pepper. Garnish with parsley before serving."
            ]
        },
        "origin": "Belgium",
        "history": "Waterzooi is a traditional Belgian stew that originated in Ghent. It is typically made with chicken or fish, vegetables, and a creamy broth, and is a comforting classic in Belgian cuisine."
    },
    {
        "country": "Belgium",
        "dish": "Belgian Endive Salad",
        "recipe": {
            "ingredients": [
                "4 Belgian endives, chopped",
                "1 apple, diced",
                "100g walnuts, chopped",
                "100g blue cheese, crumbled",
                "2 tbsp olive oil",
                "1 tbsp balsamic vinegar",
                "Salt and black pepper to taste"
            ],
            "instructions": [
                "Step 1: In a large bowl, combine endives, apple, walnuts, and blue cheese.",
                "Step 2: In a small bowl, whisk together olive oil, balsamic vinegar, salt, and pepper.",
                "Step 3: Drizzle dressing over salad and toss gently to coat."
            ]
        },
        "origin": "Belgium",
        "history": "Belgian Endive Salad is a refreshing salad that highlights the unique flavor of Belgian endives. It is often paired with apples and blue cheese for a delightful mix of flavors."
    },
    {
        "country": "Austria",
        "dish": "Wiener Schnitzel",
        "recipe": {
            "ingredients": [
                "4 veal cutlets, pounded thin",
                "1 cup all-purpose flour",
                "2 large eggs, beaten",
                "1 cup breadcrumbs",
                "Salt and black pepper to taste",
                "Vegetable oil for frying",
                "Lemon wedges for serving"
            ],
            "instructions": [
                "Step 1: Season veal cutlets with salt and pepper.",
                "Step 2: Dredge each cutlet in flour, then dip in beaten eggs, and coat with breadcrumbs.",
                "Step 3: Heat oil in a large skillet over medium heat. Fry cutlets until golden brown and crispy, about 3-4 minutes per side.",
                "Step 4: Drain on paper towels. Serve with lemon wedges."
            ]
        },
        "origin": "Austria",
        "history": "Wiener Schnitzel is a traditional Austrian dish made from breaded and fried veal cutlets. It is a classic of Viennese cuisine and is often served with a lemon wedge and a side of potato salad or cucumber salad."
    },
    {
        "country": "Austria",
        "dish": "Sachertorte",
        "recipe": {
            "ingredients": [
                "For the cake:",
                "150g dark chocolate, chopped",
                "150g butter, softened",
                "150g granulated sugar",
                "6 large eggs, separated",
                "150g all-purpose flour",
                "1 tsp vanilla extract",
                "Apricot jam for filling",
                "For the glaze:",
                "200g dark chocolate, chopped",
                "200ml heavy cream"
            ],
            "instructions": [
                "Step 1: Preheat oven to 180°C (350°F). Grease and line a 9-inch round cake pan.",
                "Step 2: Melt chocolate over a double boiler and let cool slightly.",
                "Step 3: Cream butter and sugar until light and fluffy. Beat in egg yolks one at a time, then stir in melted chocolate and vanilla.",
                "Step 4: Fold in flour until just combined.",
                "Step 5: In a separate bowl, beat egg whites until stiff peaks form. Gently fold into the batter.",
                "Step 6: Pour batter into the prepared pan and bake for 25-30 minutes. Cool completely.",
                "Step 7: Spread apricot jam over the top of the cake.",
                "Step 8: For the glaze, heat cream until simmering. Pour over chopped chocolate and stir until smooth. Let cool slightly, then pour over the jam-covered cake."
            ]
        },
        "origin": "Austria",
        "history": "Sachertorte is a rich, chocolate cake with a layer of apricot jam and a smooth chocolate glaze. It was first created in Vienna by Franz Sacher in 1832 and has since become a symbol of Austrian culinary tradition."
    },
    {
        "country": "Austria",
        "dish": "Apfelstrudel (Apple Strudel)",
        "recipe": {
            "ingredients": [
                "For the filling:",
                "6 large apples, peeled, cored, and thinly sliced",
                "100g granulated sugar",
                "1 tsp ground cinnamon",
                "50g raisins",
                "50g chopped walnuts",
                "1 tbsp lemon juice",
                "For the dough:",
                "250g all-purpose flour",
                "1/4 tsp salt",
                "1 large egg",
                "100ml warm water",
                "2 tbsp vegetable oil",
                "Butter for brushing"
            ],
            "instructions": [
                "Step 1: For the filling, mix apples, sugar, cinnamon, raisins, walnuts, and lemon juice in a bowl.",
                "Step 2: For the dough, combine flour and salt. In a separate bowl, mix egg, water, and oil. Gradually add to the flour and knead until smooth. Let rest for 30 minutes.",
                "Step 3: Roll out dough on a floured surface until very thin. Brush with melted butter.",
                "Step 4: Spread apple filling evenly over the dough. Roll up tightly and place on a baking sheet lined with parchment paper.",
                "Step 5: Brush with melted butter and bake at 180°C (350°F) for 35-40 minutes until golden brown."
            ]
        },
        "origin": "Austria",
        "history": "Apfelstrudel is a traditional Austrian pastry made with thin layers of dough and a spiced apple filling. It is often enjoyed with powdered sugar and a dollop of whipped cream or vanilla sauce."
    },
    {
        "country": "Austria",
        "dish": "Kaiserschmarrn",
        "recipe": {
            "ingredients": [
                "4 large eggs",
                "250ml milk",
                "200g all-purpose flour",
                "2 tbsp granulated sugar",
                "1/4 tsp salt",
                "2 tbsp butter",
                "Powdered sugar for dusting",
                "Fruit compote or jam for serving"
            ],
            "instructions": [
                "Step 1: In a bowl, whisk eggs and milk together. Add flour, sugar, and salt, and mix until smooth.",
                "Step 2: Heat butter in a large skillet over medium heat. Pour in batter and cook until the edges are set and the bottom is golden brown.",
                "Step 3: Using a spatula, tear the pancake into pieces and flip to cook the other side.",
                "Step 4: Dust with powdered sugar and serve with fruit compote or jam."
            ]
        },
        "origin": "Austria",
        "history": "Kaiserschmarrn is a fluffy, shredded pancake that is traditionally served as a dessert or sweet main course. It is named after Emperor Franz Joseph I of Austria and is a favorite in Austrian and Bavarian cuisine."
    },
    {
        "country": "Austria",
        "dish": "Goulash",
        "recipe": {
            "ingredients": [
                "1 kg beef stew meat, cut into cubes",
                "2 large onions, chopped",
                "2 cloves garlic, minced",
                "2 tbsp vegetable oil",
                "2 tbsp sweet paprika",
                "1 tsp caraway seeds",
                "2 cups beef broth",
                "1 cup diced tomatoes",
                "Salt and black pepper to taste",
                "Chopped fresh parsley for garnish"
            ],
            "instructions": [
                "Step 1: Heat oil in a large pot over medium heat. Brown beef cubes on all sides and remove from pot.",
                "Step 2: Add onions and garlic to the pot and cook until softened.",
                "Step 3: Stir in paprika and caraway seeds.",
                "Step 4: Return beef to the pot and add beef broth and tomatoes. Bring to a boil.",
                "Step 5: Reduce heat and simmer for 1.5-2 hours, or until beef is tender.",
                "Step 6: Season with salt and pepper. Garnish with parsley before serving."
            ]
        },
        "origin": "Austria",
        "history": "Goulash is a hearty stew with origins in Hungary, but it is also a beloved dish in Austria. Austrian goulash is typically made with beef and flavored with paprika and caraway seeds."
    },
    {
        "country": "Austria",
        "dish": "Tafelspitz",
        "recipe": {
            "ingredients": [
                "1.5 kg beef brisket",
                "2 large carrots, chopped",
                "1 large onion, chopped",
                "2 stalks celery, chopped",
                "2 cloves garlic, minced",
                "2 bay leaves",
                "1 tsp dried thyme",
                "1 liter beef broth",
                "Salt and black pepper to taste",
                "Horseradish and apple sauce for serving"
            ],
            "instructions": [
                "Step 1: Place beef brisket in a large pot and cover with beef broth.",
                "Step 2: Add carrots, onion, celery, garlic, bay leaves, and thyme.",
                "Step 3: Bring to a boil, then reduce heat and simmer for 2-3 hours, or until meat is tender.",
                "Step 4: Remove beef from the pot and let rest before slicing.",
                "Step 5: Serve with horseradish and apple sauce."
            ]
        },
        "origin": "Austria",
        "history": "Tafelspitz is a traditional Austrian dish consisting of boiled beef served with various accompaniments. It is considered a classic dish of Viennese cuisine and is often enjoyed with horseradish and apple sauce."
    },
    {
        "country": "Austria",
        "dish": "Wiener Backhendl",
        "recipe": {
            "ingredients": [
                "4 chicken thighs, skinless and boneless",
                "1 cup all-purpose flour",
                "2 large eggs, beaten",
                "1 cup breadcrumbs",
                "Salt and black pepper to taste",
                "Vegetable oil for frying",
                "Lemon wedges for serving"
            ],
            "instructions": [
                "Step 1: Season chicken with salt and pepper.",
                "Step 2: Dredge each piece in flour, then dip in beaten eggs, and coat with breadcrumbs.",
                "Step 3: Heat oil in a large skillet over medium heat. Fry chicken until golden brown and crispy, about 6-8 minutes per side.",
                "Step 4: Drain on paper towels. Serve with lemon wedges."
            ]
        },
        "origin": "Austria",
        "history": "Wiener Backhendl is a traditional Austrian dish of fried chicken, often served with a lemon wedge. It is a popular choice in Austrian pubs and restaurants."
    },
    {
        "country": "Austria",
        "dish": "Kaiserschmarrn",
        "recipe": {
            "ingredients": [
                "4 large eggs",
                "250ml milk",
                "200g all-purpose flour",
                "2 tbsp granulated sugar",
                "1/4 tsp salt",
                "2 tbsp butter",
                "Powdered sugar for dusting",
                "Fruit compote or jam for serving"
            ],
            "instructions": [
                "Step 1: In a bowl, whisk eggs and milk together. Add flour, sugar, and salt, and mix until smooth.",
                "Step 2: Heat butter in a large skillet over medium heat. Pour in batter and cook until the edges are set and the bottom is golden brown.",
                "Step 3: Using a spatula, tear the pancake into pieces and flip to cook the other side.",
                "Step 4: Dust with powdered sugar and serve with fruit compote or jam."
            ]
        },
        "origin": "Austria",
        "history": "Kaiserschmarrn is a fluffy, shredded pancake that is traditionally served as a dessert or sweet main course. It is named after Emperor Franz Joseph I of Austria and is a favorite in Austrian and Bavarian cuisine."
    },
    {
        "country": "Austria",
        "dish": "Buchteln (Austrian Sweet Rolls)",
        "recipe": {
            "ingredients": [
                "500g all-purpose flour",
                "75g granulated sugar",
                "1 packet (7g) dry yeast",
                "1/2 tsp salt",
                "250ml milk, warmed",
                "75g butter, melted",
                "2 large eggs",
                "1/2 cup fruit jam (e.g., apricot or raspberry)",
                "Powdered sugar for dusting"
            ],
            "instructions": [
                "Step 1: In a bowl, mix flour, sugar, yeast, and salt.",
                "Step 2: Add milk, melted butter, and eggs. Knead until smooth and elastic. Let rise in a warm place for 1 hour.",
                "Step 3: Roll out dough and cut into squares. Place a spoonful of jam in the center of each square and fold the corners over.",
                "Step 4: Place rolls in a greased baking dish and let rise for another 30 minutes.",
                "Step 5: Bake at 180°C (350°F) for 25-30 minutes until golden brown. Dust with powdered sugar before serving."
            ]
        },
        "origin": "Austria",
        "history": "Buchteln are soft, sweet rolls filled with fruit jam, a traditional Austrian treat often enjoyed for breakfast or dessert."
    }
]
#
def get_dishes():
    return jsonify(Dishes)
#
@app.route('/dishes/<country>', methods=['GET'])
def get_dish_by_country(country):
    dishes_by_country = [d for d in Dishes if d["country"].lower() == country.lower()]
    if dishes_by_country:
        return jsonify(dishes_by_country)
    return jsonify({"message": "Dish not found"}), 404@app.route('/dishes', methods=['GET'])
#
if __name__ == '__main__':
    app.run(debug=True)
#
