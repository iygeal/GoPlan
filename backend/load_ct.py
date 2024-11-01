#!/usr/bin/env python3
"""
Script to add 20 cities to each state in Nigeria to the cities table.
"""

from app.db import db
from app.models.city import City
from app.models.state import State
from app import create_app

# List of 20 cities per state
cities_per_state = {
        'Abia': ['Aba', 'Umuahia', 'Arochukwu', 'Ohafia', 'Isuikwuato', 'Uzuakoli', 'Bende', 'Abiriba', 'Akwete', 'Umunneochi',
                 'Ugwunagbo', 'Okpuala Ngwa', 'Ubani Ibeku', 'Azumini', 'Igbere', 'Nkporo', 'Umukabia',
                 'Osisioma', 'Ohafia-Ifigh', 'Mkporo'],

        'Adamawa': ['Yola', 'Mubi', 'Numan', 'Jimeta', 'Ganye', 'Gombi', 'Guyuk', 'Lamurde', 'Madagali', 'Maiha', 'Michika',
                    'Mayo-Belwa', 'Shelleng', 'Song', 'Toungo', 'Fufore', 'Demsa', 'Hong', 'Jada', 'Yola South'],

        'Akwa Ibom': ['Uyo', 'Eket', 'Ikot Ekpene', 'Oron', 'Ibeno', 'Ikot Abasi', 'Itu', 'Abak', 'Etinan', 'James Town',
                      'Oron', 'Nwaniba', 'Ekpene Ukpa', 'Onna', 'Nsit Ubium', 'Ukana', 'Okobo', 'Enwang', 'Okopedi', 'Essien Udim'],
        
        'Anambra': ['Awka', 'Onitsha', 'Nnewi', 'Ogbunike', 'Agulu', 'Ojoto', 'Igbo-Ukwu', 'Ekwulobia', 'Umunze', 'Aguata',
               'Nri', 'Orumba', 'Ozubulu', 'Oraifite', 'Ihiala', 'Okija', 'Atani', 'Aguluezechukwu', 'Umunya', 'Anaku'],
        
        'Bauchi': ['Bauchi', 'Yankari', 'Alkaleri', 'Tafawa Balewa', 'Dass', 'Gwana', 'Ningi', 'Misau', 'Azare', 'Bulkachuwa',
               'Kafin Madaki', 'Disina', 'Gombe Abba', 'Kirfi', 'Tambari', 'Toro', 'Zadawa', 'Burgel', 'Katagum', 'Giade'],
        
        'Bayelsa': ['Yenagoa', 'Brass', 'Nembe', 'Ogbia', 'Akassa', 'Oloibiri', 'Twon-Brass', 'Amassoma', 'Kaiama', 'Oporoma',
                    'Ekeremor', 'Sagbama', 'Peretorugbene', 'Agge', 'Korokorosei', 'Okpoama', 'Brass Island', 'Akipelai', 'Bassambiri',
                    'Okolobiri'],

        'Benue': ['Makurdi', 'Gboko', 'Otukpo', 'Katsina-Ala', 'Vandeikya', 'Oju', 'Igumale', 'Zakibiam', 'Adikpo', 'Buruku',
                  'Ushongo', 'Yandev', 'Ugbokolo', 'Aliade', 'Lessel', 'Ihugh', 'Sankera', 'Wannune', 'Naka', 'Ugba'],

        'Borno': ['Maiduguri', 'Bama', 'Biu', 'Gwoza', 'Dikwa', 'Kukawa', 'Monguno', 'Rann', 'Gamboru', 'Baga',
                  'Damboa', 'Benisheik', 'Askira', 'Konduga', 'Ngala', 'Gubio', 'Damasak', 'Abadam', 'Mallam Fatori', 'Pulka'],

        'Cross River': ['Calabar', 'Ugep', 'Ikom', 'Ogoja', 'Obudu', 'Akamkpa', 'Odukpani', 'Akpabuyo', 'Biase', 'Yakurr',
                        'Obanliku', 'Boki', 'Etung', 'Obubra', 'Yala', 'Bekwarra', 'Bakassi', 'Abi', 'Akpap', 'Itigidi'],

        'Delta': ['Warri', 'Asaba', 'Sapele', 'Ughelli', 'Agbor', 'Burutu', 'Oleh', 'Ozoro', 'Abraka', 'Ibusa',
                  'Ogwashi-Uku', 'Oghara', 'Patani', 'Issele-Uku', 'Kwale', 'Orerokpe', 'Bomadi', 'Ashaka', 'Obiaruku',
                  'Akwukwu-Igbo'],

        'Ebonyi': ['Abakaliki', 'Afikpo', 'Unwana', 'Onueke', 'Ishiagu', 'Uburu', 'Ezza', 'Effium', 'Ikwo', 'Ivo',
                   'Ohaozara', 'Ishielu', 'Ezzamgbo', 'Okposi', 'Amasiri', 'Nguzu Edda', 'Iboko', 'Izzi', 'Ukawu', 'Ohaukwu'],

        'Edo': ['Benin City', 'Auchi', 'Ekpoma', 'Uromi', 'Igarra', 'Ubiaja', 'Irrua', 'Sabongida-Ora', 'Igueben', 'Abudu',
               'Ewu', 'Fugar', 'Ibillo', 'Okpella', 'Usen', 'Iguobazuwa', 'Afuze', 'Uzebba', 'Ehor', 'Owan'],

        'Ekiti': ['Ado Ekiti', 'Ikere', 'Ikole', 'Oye', 'Ijero', 'Emure', 'Ise', 'Efon', 'Omuo', 'Ilawe',
                  'Aramoko', 'Igede', 'Ido', 'Ode', 'Iyin', 'Otun', 'Ifaki', 'Ayedun', 'Ipoti', 'Igbara-Odo'],

        'Enugu': ['Enugu', 'Nsukka', 'Oji River', 'Awgu', 'Udi', 'Agbani', 'Enugu Ezike', 'Ohodo', 'Obollo Afor', 'Aguobu-Owa',
                  'Eha Amufu', 'Eke', 'Amuri', 'Orba', 'Ugwuoba', 'Ibagwa', 'Ogrute', 'Ikem', 'Nkwo Nike', 'Akpugo'],

        'Gombe': ['Gombe', 'Billiri', 'Kaltungo', 'Bajoga', 'Kumo', 'Dukku', 'Nafada', 'Akko', 'Dadiya', 'Deba',
                  'Balanga', 'Tumu', 'Mallam Sidi', 'Shongom', 'Yamatu', 'Filiya', 'Gwandum', 'Lapan', 'Talasse', 'Tula'],

        'Imo': ['Owerri', 'Orlu', 'Okigwe', 'Mbaise', 'Oguta', 'Nkwerre', 'Mbano', 'Obowo', 'Orodo', 'Isinweke',
                'Awo-Idemili', 'Mgbidi', 'Amaigbo', 'Urualla', 'Umundugba', 'Ihiagwa', 'Emekuku', 'Ezinihitte', 'Amaraku', 'Umuna'],

        'Jigawa': ['Dutse', 'Hadejia', 'Gumel', 'Kazaure', 'Ringim', 'Babura', 'Birniwa', 'Gagarawa', 'Maigatari',
                   'Kafin Hausa', 'Kiyawa', 'Auyo', 'Jahun', 'Miga', 'Birnin Kudu', 'Guri', 'Kaugama', 'Mallam Madori',
                   'Sule Tankarkar', 'Taura'],

        'Kaduna': ['Kaduna', 'Zaria', 'Kafanchan', 'Kagoro', 'Birnin Gwari', 'Giwa', 'Ikara', 'Kachia', 'Kauru', 'Lere',
                   'Makarfi', 'Sabon Gari', 'Sanga', 'Soba', 'Zonkwa', 'Anchau', 'Hunkuyi', 'Kagarko', 'Kubau', 'Pambegua'],

        'Kano': ['Kano', 'Dambatta', 'Gwarzo', 'Karaye', 'Rano', 'Wudil', 'Bichi', 'Tarauni', 'Ungogo', 'Gezawa',
                 'Minjibir', 'Fagge', 'Gwale', 'Kumbotso', 'Nasarawa', 'Rimin Gado', 'Sumaila', 'Tudun Wada', 'Tsanyawa', 'Kunchi'],

        'Katsina': ['Katsina', 'Funtua', 'Daura', 'Malumfashi', 'Jibia', 'Kankia', 'Mani', 'Musawa', 'Dutsin-Ma', 'Zango',
                    'Bakori', 'Batagarawa', 'Baure', 'Bindawa', 'Charanchi', 'Dan Musa', 'Dandume', 'Danja', 'Ingawa', 'Kaita'],

        'Kebbi': ['Birnin Kebbi', 'Argungu', 'Yauri', 'Zuru', 'Koko', 'Jega', 'Gwandu', 'Bagudo', 'Maiyama', 'Bunza',
                  'Aleiro', 'Augie', 'Kalgo', 'Sakaba', 'Shanga', 'Suru', 'Danko', 'Fakai', 'Ngaski', 'Wasagu'],

        'Kogi': ['Lokoja', 'Okene', 'Idah', 'Kabba', 'Ankpa', 'Anyigba', 'Egbe', 'Isanlu', 'Ogaminana', 'Okehi',
                 'Ajaokuta', 'Dekina', 'Koton Karfe', 'Ogori', 'Olamaboro', 'Yagba', 'Mopa', 'Iyara', 'Okpo', 'Oguma'],

        'Kwara': ['Ilorin', 'Offa', 'Omu-Aran', 'Jebba', 'Patigi', 'Share', 'Erin-Ile', 'Lafiagi', 'Afon', 'Bode Saadu',
                  'Ajasse Ipo', 'Oke Onigbin', 'Iloffa', 'Igbaja', 'Kaiama', 'Ilesha Baruba', 'Okuta', 'Babanloma', 'Iponrin', 'Oro'],

        'Lagos': ['Lagos', 'Lagos Island', 'Ikeja', 'Lekki', 'Surulere', 'Apapa', 'Badagry', 'Ikorodu', 'Epe', 'Mushin', 'Oshodi',
                  'Agege', 'Ikoyi', 'Victoria Island', 'Ajah', 'Festac Town', 'Amuwo Odofin', 'Alimosho', 'Ajegunle',
                  'Eti-Osa', 'Ijede'],

        'Nasarawa': ['Nasarawa', 'Lafia', 'Keffi', 'Akwanga', 'Nasarawa', 'Wamba', 'Doma', 'Keana', 'Awe', 'Toto', 'Garaku',
                     'Karu', 'Kokona', 'Obi', 'Nasarawa Egon', 'Mararaba', 'New Karu', 'Masaka', 'Uke', 'Gitata', 'Gadabuke'],

        'Niger': ['Minna', 'Bida', 'Suleja', 'Kontagora', 'Lapai', 'New Bussa', 'Agaie', 'Kagara', 'Kutigi', 'Mokwa',
                 'Rijau', 'Zungeru', 'Wushishi', 'Agwara', 'Badeggi', 'Tegina', 'Madalla', 'Mashegu', 'Tafa', 'Gurara'],

        'Ogun': ['Abeokuta', 'Sagamu', 'Ijebu Ode', 'Ilaro', 'Ota', 'Ifo', 'Iperu', 'Ayetoro', 'Owode', 'Ago-Iwoye',
                 'Igbesa', 'Ijebu-Igbo', 'Ado-Odo', 'Imeko', 'Ibafo', 'Odogbolu', 'Omu', 'Ipokia', 'Imasayi', 'Ibese'],

        'Ondo': ['Akure', 'Owo', 'Ondo', 'Ikare', 'Ore', 'Okitipupa', 'Idanre', 'Ile-Oluji', 'Oka-Akoko', 'Igbokoda',
                 'Ifon', 'Ilara-Mokin', 'Igbara-Oke', 'Odigbo', 'Akungba', 'Ode-Irele', 'Igbotako', 'Ode-Aye', 'Ijare', 'Ugbo'],

        'Osun': ['Osogbo', 'Ile-Ife', 'Ilesa', 'Ede', 'Iwo', 'Ejigbo', 'Ikirun', 'Ikire', 'Ila Orangun', 'Ijebu-Jesa',
                 'Ipetu-Ijesa', 'Gbongan', 'Okuku', 'Ilobu', 'Inisa', 'Ife North', 'Ifetedo', 'Igbajo', 'Otan Ayegbaju', 'Ibokun'],

        'Oyo': ['Ibadan', 'Ogbomosho', 'Oyo', 'Iseyin', 'Saki', 'Eruwa', 'Igbo-Ora', 'Kishi', 'Igboho', 'Okeho',
                'Lalupon', 'Otu', 'Iganna', 'Jobele', 'Awe', 'Ilora', 'Ajaawa', 'Iresaadu', 'Ago-Amodu', 'Ipapo'],

        'Plateau': ['Jos', 'Pankshin', 'Shendam', 'Langtang', 'Barkin Ladi', 'Mangu', 'Bokkos', 'Wase', 'Kanke', 'Dengi',
                    'Bassa', 'Riyom', 'Kwal', 'Vom', 'Kafanchan', 'Kwalla', 'Kanam', 'Amper', 'Angware', 'Kurgwi'],

        'Rivers': ['Port Harcourt', 'Bonny', 'Degema', 'Bori', 'Omoku', 'Opobo', 'Buguma', 'Ahoada', 'Eleme', 'Okrika',
                   'Oyigbo', 'Abonnema', 'Isiokpo', 'Igwuruta', 'Rumuokoro', 'Ebubu', 'Ndoni', 'Nchia', 'Rumuola', 'Emohua'],

        'Sokoto': ['Sokoto', 'Gwadabawa', 'Wurno', 'Rabah', 'Binji', 'Goronyo', 'Gada', 'Illela', 'Isa', 'Sabon Birni',
                   'Bodinga', 'Dange', 'Kebbe', 'Kware', 'Shagari', 'Silame', 'Tambuwal', 'Tangaza', 'Tureta', 'Wamako'],

        'Taraba': ['Jalingo', 'Wukari', 'Bali', 'Gembu', 'Takum', 'Ibi', 'Baissa', 'Lau', 'Karim Lamido', 'Mutum Biyu',
                   'Zing', 'Gassol', 'Sardauna', 'Serti', 'Gashaka', 'Kurmi', 'Yorro', 'Donga', 'Garbabi', 'Suntai'],

        'Yobe': ['Damaturu', 'Potiskum', 'Gashua', 'Geidam', 'Nguru', 'Buni Yadi', 'Dapchi', 'Kanamma', 'Yusufari', 'Machina',
                 'Bursari', 'Daya', 'Fika', 'Gulani', 'Jakusko', 'Karasuwa', 'Nangere', 'Ngalda', 'Tarmuwa', 'Yunusari'],

        'Zamfara': ['Gusau', 'Kaura Namoda', 'Talata Mafara', 'Anka', 'Gummi', 'Bukkuyum', 'Nasarawa', 'Maradun', 'Bungudu',
                    'Tsafe', 'Shinkafi', 'Maru', 'Bakura', 'Birnin Magaji', 'Zurmi', 'Chafe', 'Dan Sadau', 'Moriki',
                    'Kwatarkwashi', 'Gurbin Bore']
        }

# Initialize Flask app
app = create_app()

with app.app_context():
    for state_name, city_names in cities_per_state.items():
        # Retrieve the state from the database
        state = State.query.filter_by(name=state_name).first()
        if state:
            for city_name in city_names:
                # Create a new City object and set its state_id
                city = City(name=city_name, state_id=state.id)
                db.session.add(city)
            print(f"Added cities for {state_name}")
        else:
            print(f"State {state_name} not found in the database.")

    # Commit all changes to the database
    db.session.commit()
    print("All cities added successfully.")


# Initialize Flask app
app = create_app()

with app.app_context():
    for state_name, city_names in cities_per_state.items():
        # Retrieve the state from the database
        state = State.query.filter_by(name=state_name).first()
        if state:
            for city_name in city_names:
                # Create a new City object and set its state_id
                city = City(name=city_name, state_id=state.id)
                db.session.add(city)
            print(f"Added cities for {state_name}")
        else:
            print(f"State {state_name} not found in the database.")

    # Commit all changes to the database
    db.session.commit()
    print("All cities added successfully.")
