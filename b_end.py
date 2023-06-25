import requests

APIkey="09f35bd7b0901b8d078345e6e014531b"
def get_data(place,days):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data['list']
    nr_values=8*days      # update for every 3 hours a day thats y its 8*days
    filtered_data=filtered_data[:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Seoul",days=2))