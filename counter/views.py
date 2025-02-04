"""from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'MDZNHL7tNMcsMivMo8E4kg==DuFv8uDS8BWOeoXU'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
"""

"""

# Import necessary libraries
import requests
from django.shortcuts import render

# Define your view
def home(request):
    # Handle POST request to fetch nutrition data
    if request.method == 'POST':
        query = request.POST['query']  # Get the query from form
        api_url = 'https://api.nal.usda.gov/fdc/v1/foods/search'
        api_key = 'YOUR_API_KEY'  # Replace with your USDA API key
        params = {'api_key': api_key, 'query': query}
        api_request = requests.get(api_url, params=params)
        
        # Check if request was successful
        if api_request.status_code == 200:
            try:
                api_data = api_request.json()
                # Extract relevant data from the API response
                if api_data.get('foods'):
                    food_item = api_data['foods'][0]
                    nutrients = food_item.get('foodNutrients', [])
                    serving_size = food_item.get('servingSize', '')
                    return render(request, 'home.html', {
                        'food_item': food_item,
                        'nutrients': nutrients,
                        'serving_size': serving_size
                    })
                else:
                    error_message = "Food not found in USDA database."
                    return render(request, 'home.html', {'error_message': error_message})
            except Exception as e:
                # Handle any exceptions or errors
                error_message = f"Error fetching data: {str(e)}"
                return render(request, 'home.html', {'error_message': error_message})
        else:
            # Handle API request errors
            error_message = f"API request failed with status code: {api_request.status_code}"
            return render(request, 'home.html', {'error_message': error_message})
    
    # Render initial GET request to display form
    return render(request, 'home.html')

    
    """

"""

from django.shortcuts import render
import random

# Dictionary to store generated nutritional data for each food item
generated_data = {}

# Function to generate random nutritional data for a food item
def generate_random_nutrition_data():
    return {
        'calories': random.randint(100, 500),
        'carbohydrates_total_g': round(random.uniform(0, 100), 2),
        'cholesterol_mg': random.randint(0, 100),
        'fat_saturated_g': round(random.uniform(0, 20), 2),
        'fat_total_g': round(random.uniform(0, 30), 2),
        'fiber_g': round(random.uniform(0, 10), 2),
        'potassium_mg': random.randint(0, 500),
        'protein_g': round(random.uniform(0, 50), 2),
        'sodium_mg': random.randint(0, 1000),
        'sugar_g': round(random.uniform(0, 50), 2)
    }

# View function to handle requests
def home(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        
        # Check if we already have generated data for this query
        if query in generated_data:
            # Use existing generated data for this query
            random_data = generated_data[query]
        else:
            # Generate random nutritional data for the queried food item
            random_data = generate_random_nutrition_data()
            # Store generated data in dictionary for future use
            generated_data[query] = random_data

        # Add the queried food item name to the random data
        random_data['name'] = query

        return render(request, 'home.html', {'api': [random_data]})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})

        
        """

from django.shortcuts import render
import random

def home(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        
        # Dictionary to map food items to more realistic calorie values
        food_calories = {
            'fish': 200,
            'chicken': 250,
            'crab': 150,
            'potatoes': 100,
            'beef': 300,
            'pork': 280,
            'rice': 130,
            'pasta': 180,
            'pizza': 280,
            'burger': 350,
            'salmon': 220,
            'shrimp': 120,
            'avocado': 160,
            'banana': 90,
            'apple': 50,
            'orange': 60,
            'spinach': 10,
            'broccoli': 45,
            'carrot': 30,
            'milk': 42,
            'yogurt': 60,
            'cheese': 110,
            'egg': 70,
            'bread': 80,
            'cereal': 150,
            'oatmeal': 150,
            'peanut butter': 180,
            'almonds': 160,
            'walnuts': 185,
            'dark chocolate': 600,
            'popcorn': 110,
            'ice cream': 250,
            'coconut': 354,
    'dates': 282,
    'figs': 74,
    'grapes': 69,
    'kiwi': 42,
    'mango': 60,
    'banana': 89,
    'peach': 39,
    'avocado': 160,
    'pomegranate': 83,
    'papaya': 43,
    'lychee': 66,
    'blackberry': 43,
    'plum': 30,
    'pineapple': 50,
    'blueberry': 57,
    'strawberry': 32,
    'orange': 47,
    'apple': 52,
    'watermelon': 30,
    'pear': 57,
    'grapefruit': 42,
    'lemon': 29,
    'lime': 30,
    'apricot': 48,
    'nectarine': 44,
    'cherry': 50,
    'melon': 34,
    'cranberry': 46,
    'raspberry': 52,
    'elderberry': 73,
    'guava': 68,
    'dragon fruit': 60,
    'kiwifruit': 61,
    'passion fruit': 97,
    'persimmon': 70,
    'tangerine': 53,
    'kiwano': 44,
    'pomelo': 38,
    'quince': 57,
    'plantain': 122,
    'star fruit': 31,
    'mulberry': 43,
    'cantaloupe': 34,
    'honeydew melon': 36,
    'jackfruit': 95,
    'lychee': 66,
    'mangosteen': 73,
    'rambutan': 68,
    'sapodilla': 83,
    'soursop': 66,
    'longan': 60,
    'ackee': 151,
    'breadfruit': 103,
    'custard apple': 101,
    'durian': 147,
    'feijoa': 55,
    'kumquat': 71,
    'loquat': 47,
    'mamey sapote': 149,
    'pawpaw': 57,
    'surinam cherry': 50,
    'ugli fruit': 45,
    'white currant': 56,
    'salmonberry': 52,
    'cloudberries': 43,
    'cloudberry': 43,
    'goji berry': 82,
    'huckleberry': 52,
    'juniper berry': 37,
    'lulo': 57,
    'medlar': 54,
    'nance': 44,
    'red currant': 56,
    'white currant': 56,
    'tomato': 18 ,
    'tomato': 18 ,
    'fish': 200,
'chicken': 250,
'crab': 150,
'beef': 300,
'pork': 280,
'salmon': 220,
'shrimp': 120,
'lamb': 290,
'turkey': 189,
'duck': 337,
'goat': 143,
'venison': 158,
'rabbit': 173,
'squid': 158,
'oyster': 68,
'lobster': 89,
'quail': 110,
'pheasant': 178,
'frog legs': 73,
'buffalo': 153,
'ham': 145,
'veal': 110,
'horse meat': 180,
'kangaroo': 98,
'emu': 112,
'snake': 89,
'turtle': 89,
'wild boar': 125,
'elk': 110,
'crayfish': 82,
'alligator': 232,
'octopus': 82,
'scallops': 88,
'perch': 96,
'catfish': 105,
'mahi mahi': 137,
'tilapia': 96,
'halibut': 116,
'anchovy': 131,
'cod': 82,
'whitefish': 153,
'swordfish': 182,
'mackerel': 205,
'bluefish': 158,
'bass': 124,
'haddock': 116,
'tuna': 184,
'carp': 127,
'sardine': 208,
'steak': 250,
'ribs': 361,
'spareribs': 259,
'beef jerky': 410,
'corned beef': 251,
'pepperoni': 494,
'pastrami': 133,
'salami': 336,
'bologna': 250,
'hot dog': 296,
'bratwurst': 297,
'sausage': 301,
'chorizo': 455,
'blood sausage': 379,
'ham hock': 210,
'tripe': 80,
'pate': 323,
'foie gras': 462,
'trotters': 250,
'poultry': 166,
'frankfurter': 297,
'wurstel': 301,
'andouille sausage': 301,
'kielbasa': 297,
'smoked sausage': 250,
'cured sausage': 250,
'beef tongue': 252,
'beef heart': 130,
'turkey breast': 189,
'turkey leg': 169,
'turkey wing': 173,
'goose': 240,
'squab': 155,
'partridge': 173,
'grouse': 150,
'black pudding': 379,
'white pudding': 354,
'haggis': 250,
'tripe': 80,
'caviar': 264,
'steak tartare': 192,
'head cheese': 157,
'faggots': 250,
'beef wellington': 234,
'tournedos rossini': 311,
'peppered steak': 181,
'steak diane': 243,
'pepper steak': 256,
'philly cheese steak': 302,
'beef stew': 169,
'beef pot pie': 180,
'meatloaf': 219,
'beef bourguignon': 185,
'beef stroganoff': 160,
'beef brisket': 195,
'beef ribs': 361,
'beef soup': 60,
'sirloin steak': 148,
'fillet steak': 125,
'ribeye steak': 369,
'tenderloin steak': 274,
't-bone steak': 250,
'porterhouse steak': 250,
'flank steak': 290,
'skirt steak': 220,
'flat iron steak': 175,
'minute steak': 200,
'chicken breast': 165,
'chicken thigh': 209,
'chicken drumstick': 165,
'chicken wing': 203,
'chicken liver': 119,
'chicken gizzard': 94,
'chicken nuggets': 270,
'fried chicken': 265,
'roast chicken': 190,
'chicken pot pie': 185,
'chicken soup': 31,
'chicken stew': 125,
'chicken casserole': 150,
'chicken kiev': 290,
'chicken curry': 196,
'chicken tikka masala': 176,
'chicken biryani': 193,
'chicken fried rice': 210,
'chicken stir fry': 160,
'chicken noodle soup': 31,
'chicken wings': 203,
'chicken sandwich': 223,
'chicken salad': 220,
'chicken pizza': 280,
'chicken drumsticks': 165,
'chicken leg': 209,
'chicken stew': 125,
'chicken stock': 30,
'chicken stir-fry': 159,
'chicken and rice': 130,
'chicken thighs': 209,
'chicken alfredo': 196,
'chicken marsala': 185,
'chicken parmesan': 211,
'chicken fajitas': 150,
'chicken enchiladas': 264,
'chicken quesadillas': 275,
'chicken tacos': 208,
'chicken tortilla soup': 45,
'chicken nachos': 292,
'chicken burrito': 148,
'chicken chimichanga': 255,
'chicken salad sandwich': 186,
'chicken Caesar salad': 136,
'chicken wrap': 179,
'chicken burger': 250,
'chicken nugget': 270,
'chicken cutlet': 222,
'chicken thigh': 209,
'chicken legs': 209,
'chicken breast fillet': 165,
'chicken drumstick': 165,
'chicken wings': 203,
'chicken liver': 119,
'chicken gizzard': 94,
'chicken wings': 203,
'chicken feet': 199,
'chicken heart': 153,
'chicken skin': 479,
'chicken thighs': 209,
'chicken back': 100,
'chicken carcass': 100,
'chicken head': 120,
'chicken tail': 140,
'chicken neck': 160,
'chicken feet': 250,
'chicken kidneys': 180,
'chicken liver': 190,
'chicken liver': 175,
'chicken heart': 250,
    'spinach': 23,
    'broccoli': 34,
    'carrot': 41,
    'bell pepper': 31,
    'tomato': 18,
    'cucumber': 15,
    'lettuce': 15,
    'celery': 16,
    'zucchini': 17,
    'cauliflower': 25,
    'cabbage': 25,
    'onion': 40,
    'garlic': 149,
    'green beans': 31,
    'sweet potato': 86,
    'asparagus': 20,
    'brussels sprouts': 43,
    'kale': 50,
    'mushrooms': 22,
    'radish': 16,
    'beetroot': 43,
    'turnip': 28,
    'artichoke': 47,
    'leek': 61,
    'pumpkin': 26,
    'butternut squash': 45,
    'radicchio': 23,
    'fennel': 31,
    'chili pepper': 40,
    'okra': 33,
    'parsnip': 75,
    'rhubarb': 21,
    'watercress': 11,
    'eggplant': 25,
    'collard greens': 33,
    'dandelion greens': 45,
    'bok choy': 13,
    'kohlrabi': 27,
    'chard': 19,
    'turnip greens': 32,
    'mustard greens': 27,
    'jicama': 38,
    'snow peas': 42,
    'daikon': 18,
    'arugula': 25,
    'endive': 17,
    'chives': 30,
    'bamboo shoots': 27,
    'lotus root': 74,
    'horseradish': 48,
    'sun-dried tomatoes': 258,
    'water chestnut': 97,
    'corn': 86,
    'potato': 77,
    'yam': 118,
    'rutabaga': 38,
    'taro': 112,
    'plantain': 122,
    'cassava': 160,
    'celery root': 42,
    'jerusalem artichoke': 73,
    'chayote': 19,
    'acorn squash': 40,
    'spaghetti squash': 31,
    'bamboo shoots': 27,
    'lotus root': 74,
    'horseradish': 48,
    'wasabi': 109,
    'chili pepper': 40,
    'nopal': 16,
    'bell pepper': 31,
    'lemon grass': 99,
    'corn': 86,
    'acorn squash': 40,
    'radish': 16,
    'carrot': 41,
    'parsnip': 75,
    'broccoli': 34,
    'cauliflower': 25,
    'asparagus': 20,
    'cabbage': 25,
    'artichoke': 47,
    'arugula': 25,
    'beet': 43,
    'beetroot': 43,
    'bok choy': 13,
    'brussels sprout': 43,
    'carrot': 41,
    'cauliflower': 25,
    'celeriac': 42,
    'celery': 16,
    'chayote': 19,
    'collard green': 33,
    'corn': 86,
    'cucumber': 15,
    'daikon': 18,
    'endive': 17,
    'fennel': 31,
    'garlic': 149,
    'green bean': 31,
    'jicama': 38,
    'kale': 50,
    'kohlrabi': 27,
    'leek': 61,
    'lettuce': 15,
    'mushroom': 22,
    'okra': 33,
    'olive': 115,
    'onion': 40,
    'parsnip': 75,
    'pea': 81,
    'pepper': 31,
    'pumpkin': 26,
    'radicchio': 23,
    'radish': 16,
    'rhubarb': 21,
    'scallion': 32,
    'shallot': 72,
    'snow pea': 42,
    'spinach': 23,
    'squash': 40,
    'sweet potato': 86,
    'taro': 112,
    'tomatillo': 32,
    'tomato': 18,
    'turnip': 28,
    'water chestnut': 97,
    'watercress': 11,
    'zucchini': 17,
    'celery': 16,
    'jerusalem artichoke': 73,
    'chickpea': 164,
    'lentil': 116,
    'black-eyed pea': 138,
    'edamame': 122,
    'green bean': 31,
    'kidney bean': 127,
    'lima bean': 113,
    'mung bean': 105,
    'navy bean': 142,
    'pinto bean': 143,
    'soybean': 446,
    'pea': 81,
    'peanut': 567,
    'almond': 576,
    'cashew': 553,
    'coconut': 354,
    'hazelnut': 628,
    'macadamia nut': 718,
    'peanut': 567,
    'pecan': 691,
    'pine nut': 673,
    'pistachio': 562,
    'walnut': 654,
    'acorn squash': 40,
    'artichoke': 47,
    'asparagus': 20,
    'bamboo shoots': 27,
    'beetroot': 43,
    'bell pepper': 31,
    'bok choy': 13,
    'broccoli': 34,
    'brussels sprouts': 43,
    'cabbage': 25,
    'carrot': 41,
    'cauliflower': 25,
    'celery': 16,
    'chayote': 19,
    'collard greens': 33,
    'corn': 86,
    'cucumber': 15,
    'eggplant': 25,
    'fennel': 31,
    'garlic': 149,
    'green beans': 31,
    'jicama': 38,
    'kale': 50,
    'kohlrabi': 27,
    'leek': 61,
    'lettuce': 15,
    'mushrooms': 22,
    'okra': 33,
    'onion': 40,
    'parsnip': 75,
    'peas': 81,
    'potato': 77,
    'pumpkin': 26,
    'radish': 16,
    'spinach': 23,
    'sweet potato': 86,
    'tomato': 18,
    'turnip': 28,
    'water chestnut': 97,
    'watercress': 11,
    'yam': 118,
    'zucchini': 17,
    'burger': 250,
    'pizza': 280,
    'french fries': 312,
    'hot dog': 280,
    'fried chicken': 280,
    'fried fish': 200,
    'fried shrimp': 220,
    'chicken nuggets': 290,
    'onion rings': 350,
    'taco': 217,
    'burrito': 163,
    'quesadilla': 200,
    'nachos': 320,
    'cheeseburger': 300,
    'milkshake': 150,
    'soda': 41,
    'ice cream': 207,
    'donut': 452,
    'pancake': 227,
    'waffle': 291,
    'macaroni and cheese': 330,
    'fried rice': 186,
    'spring rolls': 222,
    'egg roll': 250,
    'chow mein': 250,
    'pad thai': 357,
    'sushi': 129,
    'ramen': 98,
    'fried calamari': 200,
    'mozzarella sticks': 300,
    'chicken wings': 290,
    'hot wings': 290,
    'chili cheese fries': 296,
    'loaded potato skins': 260,
    'buffalo wings': 290,
    'chicken sandwich': 250,
    'sub sandwich': 245,
    'BLT sandwich': 250,
    'grilled cheese sandwich': 250,
    'club sandwich': 255,
    'gyro': 280,
    'kebab': 237,
    'taco salad': 271,
    'cheese fries': 312,
    'queso dip': 416,
    'nachos supreme': 320,
    'chicken quesadilla': 200,
    'churros': 415,
    'corn dog': 250,
    'cornbread': 270,
    'sloppy joe': 220,
    'chicken tenders': 300,
    'garlic bread': 250,
    'BBQ ribs': 316,
    'BBQ pulled pork sandwich': 270,
    'meatball sub': 287,
    'chicken parmigiana': 320,
    'lasagna': 150,
    'spaghetti and meatballs': 200,
    'calzone': 220,
    'enchiladas': 140,
    'chicken fajitas': 130,
    'beef tacos': 170,
    'beef burritos': 200,
    'beef enchiladas': 170,
    'beef fajitas': 150,
    'chicken tacos': 160,
    'chicken burritos': 190,
    'chicken enchiladas': 150,
    'chicken chimichangas': 320,
    'pulled pork tacos': 140,
    'pulled pork burritos': 170,
    'pulled pork enchiladas': 140,
    'pulled pork fajitas': 120,
    'shredded beef tacos': 160,
    'shredded beef burritos': 190,
    'shredded beef enchiladas': 160,
    'shredded beef fajitas': 140,
    'apple pie': 250,
'bacon': 407,
'bagel': 250,
'baguette': 250,
'banana bread': 326,
'barbecue chicken': 200,
'bean burger': 160,
'beef burger': 250,
'beef taco': 217,
'beef teriyaki': 200,
'beef wrap': 300,
'blueberry muffin': 426,
'bread': 250,
'bread roll': 250,
'breadsticks': 300,
'breakfast burrito': 200,
'breakfast sandwich': 250,
'bruschetta': 267,
'buffalo wings': 290,
'burrito': 250,
'buttermilk biscuit': 291,
'cake': 235,
'calamari': 200,
'candy': 394,
'caramel popcorn': 494,
'cheese bread': 250,
'cheeseburger': 292,
'cheesecake': 321,
'cheesy fries': 265,
'cherry pie': 400,
'chicken and waffles': 450,
'chicken nuggets': 290,
'chicken quesadilla': 220,
'chicken salad': 220,
'chicken sandwich': 252,
'chicken strips': 290,
'chicken taco': 220,
'chicken wings': 286,
'chili cheese fries': 260,
'chimichanga': 200,
'chocolate bar': 546,
'chocolate cake': 367,
'churros': 327,
'cinnamon roll': 318,
'club sandwich': 250,
'coconut shrimp': 350,
'coffee cake': 350,
'cookie': 450,
'corn dog': 250,
'cornbread': 440,
'crab cake': 210,
'crepe': 220,
'croissant': 406,
'donut': 452,
'dumplings': 300,
'egg roll': 250,
'egg sandwich': 250,
'enchilada': 200,
'french fries': 312,
'fried chicken': 295,
'fried rice': 160,
'frozen yogurt': 159,
'fruit salad': 100,
'garlic bread': 330,
'garlic knots': 255,
'granola bar': 400,
'grilled cheese': 400,
'gyro': 254,
'ham sandwich': 250,
'hash browns': 326,
'hot dog': 245,
'ice cream': 207,
'jelly donut': 320,
'kebab': 260,
'key lime pie': 300,
'lasagna': 150,
'lemon bars': 400,
'lobster roll': 170,
'macaroni and cheese': 200,
'meatball sub': 250,
'milkshake': 180,
'mini pizza': 400,
'mozzarella sticks': 250,
'nachos': 300,
'onion rings': 403,
'pad thai': 250,
'pancake': 200,
'panini': 250,
'pasta salad': 200,
'pepperoni pizza': 300,
'philly cheesesteak': 270,
'pita bread': 275,
'popcorn': 400,
'potato chips': 536,
'potato salad': 143,
'pretzel': 338,
'pulled pork sandwich': 241,
'quesadilla': 225,
'ramen': 110,
'red velvet cake': 360,
'reuben sandwich': 200,
'rice pudding': 130,
'roast beef sandwich': 220,
'salami sandwich': 220,
'salmon burger': 180,
'sandwich': 270,
'scones': 300,
'shawarma': 254,
'shrimp tempura': 200,
'sliders': 250,
'smoothie': 54,
'spaghetti': 131,
'spring rolls': 155,
'steak': 250,
'strawberry shortcake': 250,
'sushi': 129,
'taco': 300,
'tater tots': 400,
'tiramisu': 250,
'tortilla chips': 500,
'tuna sandwich': 250,
'turkey burger': 250,
'waffle': 291,
'wrap': 250,
'yogurt parfait': 120,
'zucchini fries': 250,
'coffee': 2,
    'tea': 2,
    'orange juice': 110,
    'apple juice': 115,
    'milk': 150,
    'almond milk': 30,
    'coconut water': 45,
    'cola': 140,
    'lemonade': 99,
    'beer': 154,
    'wine': 125,
    'whiskey': 64,
    'vodka': 64,
    'gin': 73,
    'rum': 64,
    'tequila': 64,
    'soda': 140,
    'iced tea': 49,
    'hot chocolate': 192,
    'smoothie': 120,
    'energy drink': 110,
    'sparkling water': 0,
    'sports drink': 80,
    'fruit punch': 110,
    'chai latte': 120,
    'matcha latte': 138,
    'mojito': 217,
     'sprite': 140,
    'pepsi': 150,
    'coke': 140,
    'mountain dew': 170,
    'dr. pepper': 150,
    'fanta': 160,
    'root beer': 180,
    'iced tea': 50,
    'orange juice': 110,
    'apple juice': 120,
    'cranberry juice': 130,
    'milk (whole)': 150,
    'milk (skim)': 90,
    'coffee (black)': 2,
    'coffee (with cream and sugar)': 50,
    'tea (black, brewed)': 2,
    'tea (with milk and sugar)': 30,
    'cake (chocolate)': 350,
    'cake': 300,
    'cupcake (chocolate)': 250,
    'cupcake': 200,
    'brownie': 200,
    'ice cream': 140,
    'ice cream (chocolate, 1 scoop)': 150,
    'ice cream (strawberry, 1 scoop)': 130,
    'cheesecake': 350,
    'chocolate chip cookie': 150,
    'donut (glazed)': 250,
    'donut (chocolate frosted)': 300,
    'pie (apple)': 300,
    'pie (pumpkin)': 320,
    'pudding (chocolate)': 200,
    'pudding (vanilla)': 180,
    'frozen yogurt': 110,
    'macaron': 70,


            # Add more food items as needed
        }
        
        # Check if the query is in our predefined food list
        if query.lower() in food_calories:
            # Use predefined calorie value
            calories = food_calories[query.lower()]
        else:
            # Generate a random calorie value between 100 and 400
            calories = random.randint(100, 400)
        
        # Generating random nutritional data
        random_data = {
            'name': query,
            'calories': calories,
            'carbohydrates_total_g': round(random.uniform(0, 100), 2),
            'cholesterol_mg': random.randint(0, 100),
            'fat_saturated_g': round(random.uniform(0, 20), 2),
            'fat_total_g': round(random.uniform(0, 30), 2),
            'fiber_g': round(random.uniform(0, 10), 2),
            'potassium_mg': random.randint(0, 500),
            'protein_g': round(random.uniform(0, 50), 2),
            'sodium_mg': random.randint(0, 1000),
            'sugar_g': round(random.uniform(0, 50), 2)
        }
        
        return render(request, 'home.html', {'api': [random_data]})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
