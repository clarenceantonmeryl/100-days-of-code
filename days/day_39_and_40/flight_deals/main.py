from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

tomorrow = datetime.now() + timedelta(days=1)

six_months = tomorrow + timedelta(days=180)

# data_manager.init_destination()
print(data_manager.destination_data)


def get_mode():
    mode = input("Add user or search for flights? a or s: ").lower()
    if mode == "a":
        return True
    else:
        return False


def add_user():
    first_name = input("What is your first name: ")
    last_name = input("What is your last name: ")
    email = input("What is your email: ")

    data_manager.add_user(first_name=first_name, last_name=last_name, email=email)


def search_flights():
    for destination in data_manager.destination_data:
        print(destination)
        if destination['iataCode'] == "":
            city = destination["city"]
            print("Blank", city)
            iata_code = flight_search.get_iata_code(city)
            print(iata_code)
            data_manager.update_destination(id=destination['id'], iata_code=iata_code)
        else:
            flight_data: FlightData = flight_search.flight_search("LON", destination["iataCode"], tomorrow, six_months)
            if flight_data:
                if destination["lowestPrice"] > flight_data.price:
                    users = data_manager.get_users()
                    notification_manager.send_email(
                        users=users,
                        destination=destination["city"],
                        price=flight_data.price
                    )
                    # notification_manager.send_message(destination=destination["city"], price=flight_data.price)
                    print(f"send message new price: {flight_data.price} old price: {destination['lowestPrice']}")

                else:
                    print("don't send message")


if get_mode():
    add_user()
else:
    search_flights()