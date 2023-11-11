CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    image VARCHAR(255),
    prep_time INTEGER NOT NULL,
    cook_time INTEGER NOT NULL,
    servings INTEGER NOT NULL,
    description TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
);

INSERT INTO recipes (id, title, image, prep_time, cook_time, servings, description, ingredients, instructions)
VALUES
(1, 'Pike Place Chowder', 'https://example.com/pike-place-chowder.jpg', 30, 45, 6, 'A rich and creamy seafood chowder inspired by the famous Pike Place Chowder in Seattle.', '1 lb mixed seafood, 4 cups vegetable broth, 1 cup heavy cream, 1/2 cup diced onions, 1/2 cup diced celery, 1/2 cup diced carrots, 1/2 cup diced potatoes, 1/4 cup butter, 1/4 cup all-purpose flour, salt and pepper to taste', '1. In a large pot, melt butter over medium heat. Add onions, celery, carrots, and potatoes. Cook until softened, about 5 minutes. 2. Stir in flour and cook for another 2 minutes. Gradually add vegetable broth, stirring constantly. 3. Add mixed seafood and bring to a simmer. Cook for 20 minutes. 4. Stir in heavy cream, salt, and pepper. Simmer for another 10 minutes. Serve hot.');

INSERT INTO recipes (id, title, image, prep_time, cook_time, servings, description, ingredients, instructions)
VALUES
(2, 'Action''s Dungeness Crab Cakes', 'https://example.com/actions-dungeness-crab-cakes.jpg', 20, 20, 4, 'These Dungeness crab cakes, man, they''re out of this world! I found them at a spot in Seattle, and they were so good I had to share the recipe.', '1 lb Dungeness crab meat, 1/2 cup panko breadcrumbs, 1/4 cup mayonnaise, 1 large egg, 2 tbsp chopped fresh parsley, 1 tbsp Dijon mustard, 1 tbsp Worcestershire sauce, 1 tsp Old Bay seasoning, 1/4 tsp salt, 1/8 tsp black pepper, 2 tbsp vegetable oil', '1. In a large bowl, mix together crab meat, panko breadcrumbs, mayonnaise, egg, parsley, Dijon mustard, Worcestershire sauce, Old Bay seasoning, salt, and black pepper. 2. Shape the mixture into 8 equal-sized patties. 3. Heat vegetable oil in a large skillet over medium heat. 4. Cook the crab cakes for 4-5 minutes per side until they are golden brown and crispy. 5. Serve with your favorite dipping sauce and enjoy!');

INSERT INTO recipes (id, title, image, prep_time, cook_time, servings, description, ingredients, instructions)
VALUES
(3, 'Action''s Dungeness Crab Cakes', 'https://example.com/actions-dungeness-crab-cakes.jpg', 20, 20, 4, 'These Dungeness crab cakes, man, they''re out of this world! I found them at a spot in Seattle, and they were so good I had to share the recipe.', '1 lb Dungeness crab meat, 1/2 cup panko breadcrumbs, 1/4 cup mayonnaise, 1 large egg, 2 tbsp chopped fresh parsley, 1 tbsp Dijon mustard, 1 tbsp Worcestershire sauce, 1 tsp Old Bay seasoning, 1/4 tsp salt, 1/8 tsp black pepper, 2 tbsp vegetable oil', '1. In a large bowl, mix together crab meat, panko breadcrumbs, mayonnaise, egg, parsley, Dijon mustard, Worcestershire sauce, Old Bay seasoning, salt, and black pepper. 2. Shape the mixture into 8 equal-sized patties. 3. Heat vegetable oil in a large skillet over medium heat. 4. Cook the crab cakes for 4-5 minutes per side until they are golden brown and crispy. 5. Serve with your favorite dipping sauce and enjoy!');
