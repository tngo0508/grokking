from collections import defaultdict, deque
def find_recipes(recipes, ingredients, supplies):
    count = {recipe: 0 for recipe in recipes}
    graph = defaultdict(list)
    output = []
    for recipe, ingredient in zip(recipes, ingredients):
        for ingre in ingredient:
            graph[ingre].append(recipe)
        count[recipe] = len(set(ingredient))

    queue = deque(supplies)
    while queue:
        s = queue.popleft()
        for recipe in graph[s]:
            count[recipe] -= 1
            if count[recipe] == 0:
                output.append(recipe)
                queue.append(recipe)
                
    
    return output