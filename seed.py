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
        "name": "Chris Bumstead",
        "photo": "images/chrisbumstead.jpg",
        "description": "4x Classic Physique Olympia. Modern era icon.",
        "likes": 0,
        "nationality": "Canadian",
        "era": "2020s"
    },
    {
        "name": "Phil Heath",
        "photo": "images/philheath.jpg",
        "description": "7x Mr. Olympia. Exceptional symmetry and conditioning.",
        "likes": 0,
        "nationality": "American",
        "era": "2010s"
    },
    {
        "name": "Dorian Yates",
        "photo": "images/dorianyates.jpg",
        "description": "6x Mr. Olympia. Pioneer of the mass monster era.",
        "likes": 0,
        "nationality": "British",
        "era": "1990s"
    },
    {
        "name": "Jay Cutler",
        "photo": "images/jaycutler.jpg",
        "description": "4x Mr. Olympia. Known for incredible size and work ethic.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s"
    },
    {
        "name": "Lee Haney",
        "photo": "images/leehaney.jpg",
        "description": "8x Mr. Olympia. First to win 8 consecutive titles.",
        "likes": 0,
        "nationality": "American",
        "era": "1980s"
    },
    {
        "name": "Frank Zane",
        "photo": "images/frankzane.jpg",
        "description": "3x Mr. Olympia. Known for aesthetic and symmetry over mass.",
        "likes": 0,
        "nationality": "American",
        "era": "1970s"
    },
    {
        "name": "Kai Greene",
        "photo": "images/kaigreene.jpg",
        "description": "3x Arnold Classic champion. Known for his artistic approach to bodybuilding.",
        "likes": 0,
        "nationality": "American",
        "era": "2010s"
    },
    {
        "name": "Lou Ferrigno",
        "photo": "images/louferrigno.jpg",
        "description": "2x IFBB Mr. Universe. Known for his role as The Incredible Hulk.",
        "likes": 0,
        "nationality": "American",
        "era": "1970s"
    },
    {
        "name": "Mike Mentzer",
        "photo": "images/mikementzer.jpg",
        "description": "Mr. Universe 1978. Pioneer of the Heavy Duty training philosophy.",
        "likes": 0,
        "nationality": "American",
        "era": "1970s"
    },
    {
        "name": "Franco Columbu",
        "photo": "images/francocolumbu.jpg",
        "description": "2x Mr. Olympia and Arnold's closest training partner.",
        "likes": 0,
        "nationality": "Italian",
        "era": "1970s"
    },
    {
        "name": "Sergio Oliva",
        "photo": "images/sergiooliva.jpg",
        "description": "3x Mr. Olympia. The only man to beat Arnold at the Olympia.",
        "likes": 0,
        "nationality": "Cuban",
        "era": "1960s"
    },
    {
        "name": "Big Ramy",
        "photo": "images/bigramy.jpg",
        "description": "2x Mr. Olympia. One of the biggest physiques in bodybuilding history.",
        "likes": 0,
        "nationality": "Egyptian",
        "era": "2020s"
    },
    {
        "name": "Flex Wheeler",
        "photo": "images/flexwheeler.jpg",
        "description": "4x Arnold Classic champion. Called the most genetically gifted ever.",
        "likes": 0,
        "nationality": "American",
        "era": "1990s"
    },
    {
        "name": "Dexter Jackson",
        "photo": "images/dexterjackson.jpg",
        "description": "Mr. Olympia 2008. Longest competitive career in bodybuilding history.",
        "likes": 0,
        "nationality": "American",
        "era": "2000s"
    },
    {
        "name": "Larry Wheels",
        "photo": "images/larrywheels.jpg",
        "description": "World record powerlifter and bodybuilder. One of the most followed athletes online.",
        "likes": 0,
        "nationality": "American",
        "era": "2020s"
    },
    {
        "name": "Nick Walker",
        "photo": "images/nickwalker.jpg",
        "description": "Arnold Classic 2021 champion. One of the most exciting young athletes in the sport.",
        "likes": 0,
        "nationality": "American",
        "era": "2020s"
    },
    {
        "name": "Derek Lunsford",
        "photo": "images/dereklunsford.jpg",
        "description": "Mr. Olympia 2023. Dominant force in modern bodybuilding.",
        "likes": 0,
        "nationality": "American",
        "era": "2020s"
    },
    {
        "name": "Hadi Choopan",
        "photo": "images/hadichoopan.jpg",
        "description": "Mr. Olympia 2022. Known as The Persian Wolf for his conditioning.",
        "likes": 0,
        "nationality": "Iranian",
        "era": "2020s"
    }
]

collection.drop()
collection.insert_many(athletes)      
collection.create_index([("name", "text")])
