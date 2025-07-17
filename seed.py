import pymongo

mongo_details = "mongodb://mongodb:27017"

client = pymongo.MongoClient(mongo_details)

db = client.ballers_db

collection = db.players

players_data = [
    {
        "name": "Lionel Messi",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Lionel_Messi_20180626.jpg",
        "current_team": "Inter Miami CF",
        "birth_year": 1987,
        "preferred_foot": "Left",
        "height": 170
    },
    {
        "name": "Cristiano Ronaldo",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8c/Cristiano_Ronaldo_2018.jpg",
        "current_team": "Al-Nassr FC",
        "birth_year": 1985,
        "preferred_foot": "Right",
        "height": 187
    },
    {
        "name": "Neymar Jr.",
        "image_url": "https://b.fssta.com/uploads/application/soccer/headshots/713.vresize.350.350.medium.34.png",
        "current_team": "Al Hilal SFC",
        "birth_year": 1992,
        "preferred_foot": "Right",
        "height": 175
    },
    {
        "name": "Kylian Mbappé",
        "image_url": "https://img.a.transfermarkt.technology/portrait/big/342229-1682683695.jpg?lm=1",
        "current_team": "Real Madrid C.F.",
        "birth_year": 1998,
        "preferred_foot": "Right",
        "height": 178
    },
    {
        "name": "Kevin De Bruyne",
        "image_url": "https://s.hs-data.com/bilder/spieler/gross/142263.jpg",
        "current_team": "Manchester City F.C.",
        "birth_year": 1991,
        "preferred_foot": "Right",
        "height": 181
    },
    {
        "name": "Peter Shalulile",
        "image_url": "https://www.idiskitimes.co.za/wp-content/uploads/2021/11/Peter-Shalulile-scaled-1.jpeg",
        "current_team": "Mamelodi Sundowns",
        "birth_year": 1993,
        "preferred_foot": "Right",
        "height": 174
    },
    {
        "name": "Kolo Touré",
        "image_url": "https://cdn.standardmedia.co.ke/images/saturday/yruxeuvodofgr541l575c5679899e9.jpg",
        "current_team": "Assistant Coach at Manchester City",
        "birth_year": 1981,
        "preferred_foot": "Right",
        "height": 178
    },
    {
        "name": "Zinedine Zidane",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Zinedine_Zidane_by_Tasnim_03.jpg",
        "current_team": "Investor at Rodez AF",
        "birth_year": 1972,
        "preferred_foot": "Right",
        "height": 185
    },
    {
        "name": "N'Golo Kanté",
        "image_url": "https://media.ouest-france.fr/v1/pictures/275a5d7924bc5117268b0caf0477f789-img-football-ngolo-kante.jpg?client_id=cmsfront&sign=3e5e9cbce952d1f84e644431b7c7602d8793ccb8caac549aafe2e7ca4e77b670",
        "current_team": "Al-Ittihad",
        "birth_year": 1991,
        "preferred_foot": "Right",
        "height": 168
    },
    {
        "name": "Ronaldo Nazario",
        "image_url": "https://pbs.twimg.com/media/FYW5DQ3XwAEtIJd?format=jpg&name=4096x4096",
        "current_team": "Retired",
        "birth_year": 1976,
        "preferred_foot": "Right",
        "height": 183
    }
]

collection.insert_many(players_data)

client.close()
