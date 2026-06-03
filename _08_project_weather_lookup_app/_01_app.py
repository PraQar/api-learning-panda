import requests
import streamlit as st


#get the coordinates of the city using geocoding API
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"

#get the weather data using the coordinates from the weather API
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


# Function to get the coordinates of a city using the geocoding API.
def get_coordinates(city_name: str) -> dict:
    params = {
        "name": city_name,
        "count":1,
        "language":"en",
        "format":"json"         
    }
    
    response = requests.get(url = GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if "results" not in data or not data["results"]:
        raise ValueError("City : ", city_name," not found.")

    location = data["results"][0]
    return {
        "name": location["name"],
        "country": location["country"],
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }   

def get_weather(latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        # Request hourly humidity and 10m wind speed fields.
        # Open-Meteo uses field names without underscores between words.
        "hourly": "relativehumidity_2m,windspeed_10m"
    }
    
    response = requests.get(url = WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def get_current_hourly_index(weather: dict) -> int:
    current_time = weather["current_weather"]["time"]
    try:
        return weather["hourly"]["time"].index(current_time)
    except (ValueError, KeyError):
        return 0


def main():
    st.set_page_config(page_title="Weather Lookup App", page_icon="☀️")
    st.title("Weather API MVP")
    st.write("Enter a city name to fetch the current weather using API calls.")
    
    city_name = st.text_input("City name : ", value = "Dehradun")
    
    if st.button("Get Weather") and city_name:
        if not city_name.strip():
            st.error("Please enter a valid city name.")
            return
        try:
            with st.spinner("Fetching coordinates..."):
                location = get_coordinates(city_name)
            with st.spinner("Fetching weather data..."):
                weather = get_weather(location["latitude"], location["longitude"])
            
            current_index = get_current_hourly_index(weather)
            st.subheader(f"Current Weather in {location['name']}, {location['country']}")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Temperature (°C)", weather["current_weather"]["temperature"])
            with col2:
                st.metric("Humidity (%)", weather["hourly"]["relativehumidity_2m"][current_index])
            with col3:
                st.metric("Wind Speed (km/h)", weather["current_weather"]["windspeed"])   
            st.json(weather)
        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")
        except requests.exceptions.Timeout:
            st.error("The API request timed out.")
        except ValueError as e:
            st.error(str(e))
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
            
if __name__ == "__main__":
    main() 
    
    
    