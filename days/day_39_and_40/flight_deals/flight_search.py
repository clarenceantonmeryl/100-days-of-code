from flight_data import FlightData
import requests

TEQUILA_API_KEY = 'hPWludzk1sTECutW_FGVG6Dgos8NJijF'
TEQUILA_API_URL = "https://tequila-api.kiwi.com"
TEQULA_IATA_URL = f"{TEQUILA_API_URL}/locations/query"
TEQUILA_SEARCH_URL = f"{TEQUILA_API_URL}/v2/search"
TEQUILA_API_HEADER = {
    "apikey": TEQUILA_API_KEY
}



class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_iata_code(self, city):
        params = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=TEQULA_IATA_URL, params=params, headers=TEQUILA_API_HEADER)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def flight_search(
            self,
            origin_city_code,
            destination_city_code,
            from_time,
            to_time):

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=TEQUILA_SEARCH_URL, params=query, headers=TEQUILA_API_HEADER)
        print(response.url)
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print("No flights available")
            return None
        else:
            travel_route = data["route"][0]
            return_route = data["route"][1]
            price = data["price"]
            origin_city = travel_route["cityFrom"]
            origin_airport = travel_route["flyFrom"]
            destination_city = travel_route["cityTo"]
            destination_airport = travel_route["flyTo"]
            travel_date = travel_route["local_departure"]
            return_date = return_route["local_arrival"]
            flightdata = FlightData(
                price=price,
                origin_city=origin_city,
                origin_airport=origin_airport,
                destination_city=destination_city,
                destination_airport=destination_airport,
                travel_date=travel_date,
                return_date=return_date
            )
            return flightdata
