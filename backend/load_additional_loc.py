#!/usr/bin/env python3
"""
Script to load additional locations not covered in the main Attractions table.
"""

from app.db import db
from app import create_app
from app.models.city import City
from app.models.state import State
from app.models.attraction import Attraction
from app.models.location import Location  # This is the model for the additional locations

# Define additional locations data that were not included in Attractions
additional_locations = {
        "Abia": ["Arochukwu Cave", "Azumini Blue River", "National War Museum", "Ojukwu Bunker", "Ngodo Cave"],
        "Adamawa": ["Mandara Mountains", "Koma Hills", "Sukur Cultural Landscape", "Gashaka-Gumti National Park",
                    "Lamurde Hot Spring"],
        "Akwa Ibom": ["Ibeno Beach", "Amalgamation House", "Oron Museum", "Ibom Plaza", "Godswill Akpabio Stadium"],
        "Anambra": ["Ogbunike Caves", "Agulu Lake", "Rojenny Tourist Village", "Owerre Ezukala Cave and Waterfall", "Onitsha Market"],
        "Bauchi": ["Yankari National Park", "Marshall Caves", "Wikki Warm Spring", "Sumu Wildlife Park", "Tunga Dutse"],
        "Bayelsa": ["Oxbow Lake", "Akassa Lighthouse", "Kaiama Monument", "Okpoama Beach", "Nembe City Walls"],
        "Benue": ["Ikwe Holiday Resort", "Montane Games Reserve", "Ikyogen Hills", "Dajo Pottery", "Kwagh-hir Puppet Theatre"],
        "Borno": ["Sambisa Forest", "Lake Alau", "Shehu of Borno Palace", "Rabeh’s Fort", "Kyarimi Park"],
        "Cross River": ["Obudu Mountain Resort", "Agbokim Waterfalls", "Drill Ranch", "Kwa Falls", "Mary Slessor House"],
        "Delta": ["Kwale Game Reserve", "Nana's Palace", "Red Mangrove Swamp", "Abraka Turf and Country Club", "Araya Bible Site"],
        "Ebonyi": ["Amanchara Waterfalls", "Afiukwu Beach", "Abakaliki Green Lake", "Ezeagu Tourist Complex", "Okposi Salt Lake"],
        "Edo": ["National Museum Benin", "Emotan Statue", "Benin Moat", "Okomu National Park", "Idia Renaissance"],
        "Ekiti": ["Ikogosi Warm Spring", "Arinta Waterfalls", "Fajuyi Memorial Park", "Olosunta Hills", "Ero Dam"],
        "Enugu": ["Awhum Waterfall", "Ezeagu Tourist Complex", "Ngwo Pine Forest", "Milken Hills", "National Museum of Unity"],
        "Gombe": ["Gombe Hills", "Tangale Hill", "Tula Battlefield", "Dadinkowa Dam", "Bima Hill"],
        "Imo": ["Oguta Lake", "Mbari Cultural Centre", "Amadioha Shrine", "Rolling Hills of Okigwe", "Ada Palm Plantation"],
        "Jigawa": ["Birnin Kudu Rock Paintings", "Dutse Rock", "Kazaure Emirate", "Hadejia Wetlands", "Baturiya Birds Sanctuary"],
        "Kaduna": ["Kajuru Castle", "Kamuku National Park", "Nok Village", "Kagoro Hills", "Lord Lugard Footbridge"],
        "Kano": ["Kofar Mata Dye Pits", "Gidan Makama Museum", "Dala Hill", "Emir's Palace", "Tiga Dam"],
        "Katsina": ["Gobarau Minaret", "Emir's Palace", "Kusugu Well", "Kusugu Shrine", "Daura Museum"],
        "Kebbi": ["Argungu Fishing Festival", "Gwandu Emirate", "Kanta Museum", "Zuru Hills", "Illo City Wall"],
        "Kogi": ["Mount Patti", "Confluence of River Niger and Benue", "Lord Lugard House", "Ogidi Hills", "Okene Pottery"],
        "Kwara": ["Esie Museum", "Owu Waterfalls", "Imoleboja Rock Shelter", "Shao Town", "Jebba"],
        "Lagos": ["Ikoyi Club", "Elegushi Beach", "National Theatre", "Third Mainland Bridge", "Iga Idunganran Palace"],
        "Nasarawa": ["Farin Ruwa Waterfalls", "Doma Dam", "Eggon Hills", "Akiri Salt Village", "Pepe Hills"],
        "Niger": ["Gurara Waterfalls", "Zuma Rock", "Kainji National Park", "Baro Empire Hill", "Shiroro Dam"],
        "Ogun": ["Olumo Rock", "Omo Forest Reserve", "Birikisu Sungbo Shrine", "June 12 Cultural Centre", "Olusegun Obasanjo Library"],
        "Ondo": ["Idanre Hills", "Ebomi Lake", "Owo Museum", "Oke Maria", "Ipale Hills"],
        "Osun": ["Osun-Osogbo Sacred Grove", "Ooni's Palace", "Obafemi Awolowo University", "Nike Art Gallery",
                 "Erin Ijesha Waterfall"],
        "Oyo": ["Mapo Hall", "University of Ibadan Zoo", "Ado-Awaye Suspended Lake", "Agodi Gardens",
                "Trans Wonderland Amusement Park"],
        "Plateau": ["Jos Wildlife Park", "Assop Falls", "Kurra Falls", "Shere Hills", "Rayfield Resort"],
        "Rivers": ["Isaac Boro Garden", "Port Harcourt Zoo", "Pleasure Park", "Bonny Island", "Finima Nature Park"],
        "Sokoto": ["Sokoto Museum", "Sultan's Palace", "Gidan Makama", "Kwiambana Forest", "Goronyo Dam"],
        "Taraba": ["Mambilla Plateau", "Gashaka-Gumti Park", "Bali Fishing Festival", "Kashimbila Dam", "Donga River Basin"],
        "Yobe": ["Dagona Waterfowl Sanctuary", "Bade Emirate", "Nguru Wetlands", "Tulo-Tulo Wellspring", "Mammy Market Potiskum"],
        "Zamfara": ["Kiyawa City Walls", "Kuyambana Game Reserve", "Emir's Palace Gusau", "Zamfara Forest Reserve", "Kanwa Dam"]
        }

# Initialize the Flask app
app = create_app()

with app.app_context():
    # Iterate through additional locations data
    for state_name, locations in additional_locations.items():
        # First get the state object
        state = State.query.filter_by(name=state_name).first()
        if not state:
            print(f"State '{state_name}' not found")
            continue

        # Get all cities for this state using state_id
        cities = City.query.filter_by(state_id=state.id).all()

        # Loop through each location in the state
        for city in cities:
            for location_name in locations:
                # Check if the location already exists in the Attractions table
                existing_attraction = Attraction.query.filter_by(
                    name=location_name,
                    city_id=city.id
                ).first()

                if not existing_attraction:
                    # If it doesn't exist, add it to the AdditionalLocation table
                    additional_location = Location(
                        name=location_name,
                        city_id=city.id,
                        state_id=city.state_id
                    )
                    db.session.add(additional_location)
                    print(f"Added additional location '{location_name}' in {city.name}, {state_name}.")

        # Commit after processing each state
        db.session.commit()
    print("All additional locations added successfully.")
