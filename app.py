# Description: Main Streamlit application file for the Real-Time Emergency Response Dashboard.
import streamlit as st
from database import init_db, add_incident, get_all_incidents, clear_incidents
from cache import update_cache, get_cached_data
from sensors import fetch_weather_alerts

import folium
from streamlit_folium import st_folium

# Initialize the database
init_db()

st.set_page_config(page_title="Real-Time Emergency Response Dashboard", layout="wide")
st.title("Real-Time Emergency Response Dashboard")

# Create tabs for different views
tabs = st.tabs(["Dashboard", "Simulate Incident", "Map View"])

# ----- Dashboard Tab -----
with tabs[0]:
    st.header("Incident Dashboard")
    if st.button("Refresh Data (Clear History)", key="refresh_button"):
        clear_incidents()
        update_cache("incidents", [])
        st.success("All incident history cleared!")
    
    incidents = get_all_incidents()
    if incidents:
        data = []
        for inc in incidents:
            data.append({
                "ID": inc["id"],
                "Title": inc["title"],
                "Description": inc["description"],
                "Time": inc["incident_time"],
                "Latitude": inc["latitude"],
                "Longitude": inc["longitude"],
                "Status": inc["status"]
            })
        st.dataframe(data)
    else:
        st.info("No incidents recorded yet.")

# ----- Simulate Incident Tab -----
with tabs[1]:
    st.header("Simulate New Incident")
    
    st.subheader("Fetch Weather Alert")
    city = st.text_input("Enter city for weather alert (default: San Francisco)", "San Francisco", key="city_input")
    if st.button("Fetch Weather Alert", key="fetch_weather"):
        incident = fetch_weather_alerts(city)
        if incident:
            add_incident(
                title=incident["title"],
                description=incident["description"],
                incident_time=incident["incident_time"],
                latitude=incident["latitude"],
                longitude=incident["longitude"],
                status=incident["status"]
            )
            cached_incidents = get_cached_data("incidents") or []
            cached_incidents.insert(0, incident)
            update_cache("incidents", cached_incidents)
            st.success("Weather alert incident added!")
            st.json(incident)
        else:
            st.error("Failed to fetch weather data.")
    
    st.subheader("Cached Incident Data")
    cached_data = get_cached_data("incidents")
    if cached_data:
        st.json(cached_data)
    else:
        st.info("No cached incident data available.")

# ----- Map View Tab -----
with tabs[2]:
    st.header("Incident Map")
    incidents = get_all_incidents()
    if incidents:
        # Center the map on the most recent incident's coordinates.
        center_lat = incidents[0]["latitude"]
        center_lon = incidents[0]["longitude"]
        base_map = folium.Map(location=[center_lat, center_lon], zoom_start=12)
        for inc in incidents:
            folium.Marker(
                location=[inc["latitude"], inc["longitude"]],
                popup=f"{inc['title']} ({inc['incident_time']})",
                tooltip=inc["title"]
            ).add_to(base_map)
        st_folium(base_map, width=700, height=500)
    else:
        st.info("No incident data available to display on the map.")
