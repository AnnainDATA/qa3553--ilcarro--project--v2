import uuid
from faker import Faker
from models.car import Car

faker = Faker()
#----------------------------------------------------------------------------------------------------------
CITY_OPTIONS = ["Acre", "Afula", "Arad", "Ashdod", "Ashkelon", "Bat Yam", "Beersheba", "Beit Shemesh",
                "Bnei Brak", "Carmiel", "Dimona", "Eilat", "Givatayim", "Hadera", "Haifa", "Herzliya",
                "Holon", "Jerusalem", "Kfar Saba", "Kiryat Ata", "Kiryat Bialik", "Kiryat Gat",
                "Kiryat Motzkin", "Kiryat Ono", "Kiryat Shmona", "Kiryat Yam", "Lod", "Ma'alot-Tarshiha",
                "Migdal HaEmek", "Modi'in-Maccabim-Re'ut", "Nahariya", "Nazareth", "Nes Ziona",
                "Netanya", "Ofakim", "Or Yehuda", "Petah Tikva", "Ra'anana", "Ramat Gan", "Ramla",
                "Rehovot", "Rishon LeZion", "Rosh HaAyin", "Safed", "Sakhnin", "Sderot", "Tamra",
                "Tayibe", "Tel Aviv", "Tiberias", "Tira", "Umm al-Fahm", "Yavne", "Yeruham"]
#----------------------------------------------------------------------------------------------------------
CITY_OPTIONS_SWAGGER = ["Ashdod", "Ashkelon", "Bat Yam", "Beer Sheva", "Bnei Brak", "Dimona", "Eilat",
                        "Givatayim", "Hadera", "Haifa", "Herzliya", "Hod HaSharon", "Holon", "Jerusalem",
                        "Kfar Saba", "Modiin", "Nazareth", "Netanya", "Petah Tikva", "Qiryat Ata",
                        "Qiryat Bialik", "Qiryat Gat", "Qiryat Malakhi", "Qiryat Motzkin", "Qiryat Ono",
                        "Qiryat Shemona", "Qiryat Tivon", "Qiryat Yam", "Qiryat Ye'arim",
                        "Qiryat Yovel", "Raanana", "Ramat Gan", "Rehovot", "Rishon LeZion",
                        "Sderot", "Tel Aviv", "Tiberias"]
#----------------------------------------------------------------------------------------------------------
def find_matching_cities(city_options, city_options_swagger):
    result = []
    for city in city_options:
        if city in city_options_swagger:
            result.append(city)
    return result
matching_cities = find_matching_cities(CITY_OPTIONS,CITY_OPTIONS_SWAGGER)

# MATCHING_CITIES = ['Ashdod', 'Ashkelon', 'Bat Yam', 'Bnei Brak', 'Dimona', 'Eilat', 'Givatayim', 'Hadera',
#                    'Haifa', 'Herzliya', 'Holon', 'Jerusalem', 'Kfar Saba', 'Nazareth', 'Netanya', 'Petah Tikva',
#                    'Ramat Gan', 'Rehovot', 'Rishon LeZion', 'Sderot', 'Tel Aviv', 'Tiberias']
#----------------------------------------------------------------------------------------------------------
swagger_cities_only = list(set(CITY_OPTIONS_SWAGGER) - set(matching_cities))

# SWAGGER_CITIES_ONLY = ["Beer Sheva", "Hod HaSharon", "Modiin", "Qiryat Ata", "Qiryat Bialik",
#                        "Qiryat Gat", "Qiryat Malakhi", "Qiryat Motzkin", "Qiryat Ono",
#                        "Qiryat Shemona", "Qiryat Tivon", "Qiryat Yam", "Qiryat Ye'arim",
#                        "Qiryat Yovel","Raanana"]
#----------------------------------------------------------------------------------------------------------
FUEL_OPTIONS = ["Petrol","Diesel","Hybrid","Electric"]
MANUFACTURE_OPTIONS = ["Toyota", "Honda", "Ford", "BMW", "Mazda"]
MODEL_OPTIONS = ["Camry", "Civic", "Focus", "X5", "Premium"]
CAR_CLASS_OPTIONS = ["Economy","Comfort","Business","Premium"]
GEAR_OPTIONS = ["Automatic", "Manual"]
WHEELS_DRIVE_OPTIONS = ["FWD", "RWD", "AWD"]

def create_car(city = None, fuel = None, manufacture = None, model = None, year = None,
               seats=None, car_class = None, serial_number = None, price_per_day = None,
               gear = None, wheels_drive = None, photo_path=None):
    return Car(
        city=city if city is not None else faker.random_element(matching_cities),
        manufacture=manufacture if manufacture is not None else faker.random_element(MANUFACTURE_OPTIONS),
        model=model if model is not None else faker.random_element(MODEL_OPTIONS),
        year=year if year is not None else faker.random_int(min=2000, max=2026),
        fuel=fuel if fuel is not None else faker.random_element(FUEL_OPTIONS),
        seats=seats if seats is not None else faker.random_int(min=2, max=7),
        car_class=car_class if car_class is not None else faker.random_element(CAR_CLASS_OPTIONS),
        serial_number=serial_number if serial_number is not None else "MM" + uuid.uuid4().hex[:8].upper(),
        price_per_day=price_per_day if price_per_day is not None else faker.random_int(min=20, max=500),
        gear=gear if gear is not None else faker.random_element(GEAR_OPTIONS),
        wheels_drive=wheels_drive if wheels_drive is not None else faker.random_element(WHEELS_DRIVE_OPTIONS),
        photo_path=photo_path
    )


