from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["netflex"]
collection = db["athletes"]

athletes = [
    {
        "name": "Arnold Schwarzenegger",
        "photo": "images/arnold.jpg",
        "description": "7x Mr. Olympia. The face of bodybuilding worldwide.",
        "likes": 0,
        "nationality": "Austrian",
        "era": "1970s"
    },
    {
        "name": "Ronnie Coleman",
        "photo": "images/ronnie.jpg",
        "description": "8x Mr. Olympia. Known for his iconic lifts and unmatched mass.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s"
    },
    {
        "name": "Branch Warren",
        "photo": "images/branch_warren.jpg",
        "description": "2x Arnold Classic champion. Known for his gritty and intense training style.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s"
    },
    {
        "name": "Dexter Jackson",
        "photo": "images/dexter_jackson.jpg",
        "description": "Mr. Olympia 2008. Longest competitive career in bodybuilding history.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s"
    },
    {
        "name": "Dorian Yates",
        "photo": "images/dorian_yates.jpg",
        "description": "6x Mr. Olympia. Pioneer of the mass monster era.",
        "likes": 0,
        "nationality": "British",
        "era": "1990s"
    },
    {
        "name": "Flex Wheeler",
        "photo": "images/flex_wheeler.jpg",
        "description": "4x Arnold Classic champion. Called the most genetically gifted ever.",
        "likes": 0,
        "nationality": "American",
        "era": "1990s"
    },
    {
        "name": "Franco Columbu",
        "photo": "images/franco_columbu.jpg",
        "description": "2x Mr. Olympia and Arnold's closest training partner.",
        "likes": 0,
        "nationality": "Italian",
        "era": "1970s"
    },
    {
        "name": "Hidetada Yamagishi",
        "photo": "images/hidetada_yamagishi.jpg",
        "description": "Top IFBB Pro. First Japanese athlete to compete at Mr. Olympia.",
        "likes": 0,
        "nationality": "Japanese",
        "era": "2010s"
    },
    {
        "name": "Jay Cutler",
        "photo": "images/jay_cutler.webp",
        "description": "4x Mr. Olympia. Known for incredible size and work ethic.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s"
    },
    {
        "name": "Kai Greene",
        "photo": "images/kai_greene.webp",
        "description": "3x Arnold Classic champion. Known for his artistic approach to bodybuilding.",
        "likes": 0,
        "nationality": "American",
        "era": "2010s"
    },
    {
        "name": "Kevin Levrone",
        "photo": "images/kevin_levrone.jpg",
        "description": "4x Mr. Olympia runner-up. Known as the Maryland Muscle Machine.",
        "likes": 0,
        "nationality": "American",
        "era": "1990s"
    },
    {
        "name": "Lee Haney",
        "photo": "images/lee_haney.jpg",
        "description": "8x Mr. Olympia. First to win 8 consecutive titles.",
        "likes": 0,
        "nationality": "American",
        "era": "1980s"
    },
    {
        "name": "Lou Ferrigno",
        "photo": "images/lou_ferrigno.jpg",
        "description": "2x IFBB Mr. Universe. Known for his role as The Incredible Hulk.",
        "likes": 0,
        "nationality": "American",
        "era": "1970s"
    },
    {
        "name": "Phil Heath",
        "photo": "images/phil_heath.jpg",
        "description": "7x Mr. Olympia. Exceptional symmetry and conditioning.",
        "likes": 0,
        "nationality": "American",
        "era": "2010s"
    },
    {
        "name": "Rich Gaspari",
        "photo": "images/rich_gaspari.webp",
        "description": "3x Mr. Olympia runner-up. Pioneer of conditioning in bodybuilding.",
        "likes": 0,
        "nationality": "American",
        "era": "1980s"
    },
    {
        "name": "Sergio Oliva",
        "photo": "images/sergio_oliva.jpg",
        "description": "3x Mr. Olympia. The only man to beat Arnold at the Olympia.",
        "likes": 0,
        "nationality": "Cuban",
        "era": "1960s"
    },
    {
        "name": "Shawn Ray",
        "photo": "images/shawn_ray.jpg",
        "description": "Top Olympia competitor throughout the 1990s. Known for perfect conditioning.",
        "likes": 0,
        "nationality": "American",
        "era": "1990s"
    },
    {
        "name": "Shawn Rhoden",
        "photo": "images/shawn_rhoden.webp",
        "description": "Mr. Olympia 2018. Known for his incredible aesthetics and conditioning.",
        "likes": 0,
        "nationality": "American",
        "era": "2010s"
    },
    {
        "name": "Tom Platz",
        "photo": "images/tom_platz.jpg",
        "description": "Known as The Golden Eagle. Legendary for his incredible leg development.",
        "likes": 0,
        "nationality": "American",
        "era": "1980s"
    },
    {
        "name": "Chris Bumstead",
        "photo": "images/chris_bumstead.jpg",
        "description": "4x Classic Physique Olympia. Modern era icon.",
        "likes": 0,
        "nationality": "Canadian",
        "era": "2020s"
    }
]


collection.drop()
collection.insert_many(athletes)      
collection.create_index([("name", "text")])
