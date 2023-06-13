import requests

APIkey="09f35bd7b0901b8d078345e6e014531b"
def get_data(place,days,kind=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*days
    filtered_data=filtered_data[:nr_values]
    if kind=="temperature":
        filtered_data=[dict["main"]["temp"] for dict in filtered_data]
    if kind=="sky":
        filtered_data=[dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="Seoul",days=1,kind="sky"))