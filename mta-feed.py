import requests
import pandas as pd
import gtfs_realtime_pb2

url = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace"

try:
    response = requests.get(url)
    response.raise_for_status()
    feed_content = response.content
    print("Successfully downloaded the GTFS feed.")

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(feed_content)

    # DATAFRAMES:
    trip_updates_data = []
    vehicle_positions_data = []
    alerts_data = []

    for entity in feed.entity:
        if entity.HasField('trip_update'):
            trip_update = entity.trip_update
            trip_id = trip_update.trip.trip_id
            for stop_time_update in trip_update.stop_time_update:
                trip_updates_data.append({
                    'trip_id': trip_id,
                    'stop_sequence': stop_time_update.stop_sequence,
                    'arrival_time': stop_time_update.arrival.time if stop_time_update.HasField('arrival') else None,
                    'departure_time': stop_time_update.departure.time if stop_time_update.HasField('departure') else None,
                    'stop_id': stop_time_update.stop_id
                })
        elif entity.HasField('vehicle'):
            vehicle = entity.vehicle
            vehicle_positions_data.append({
                'vehicle_id': vehicle.vehicle.id if vehicle.HasField('vehicle') else None,
                'trip_id': vehicle.trip.trip_id if vehicle.HasField('trip') else None,
                'latitude': vehicle.position.latitude if vehicle.HasField('position') else None,
                'longitude': vehicle.position.longitude if vehicle.HasField('position') else None,
                'bearing': vehicle.position.bearing if vehicle.HasField('position') else None,
                'speed': vehicle.position.speed if vehicle.HasField('position') else None,
                'timestamp': vehicle.timestamp
            })
        elif entity.HasField('alert'):
            alert = entity.alert
            alert_header_text = alert.header.text.translation[0].text if alert.header.HasField('text') and alert.header.text.translation else None
            alert_description_text = alert.description_text.translation[0].text if alert.description_text.HasField('text') and alert.description_text.translation else None
            alert_effect = alert.effect if alert.HasField('effect') else None
            alerts_data.append({
                'alert_header_text': alert_header_text,
                'alert_description_text': alert_description_text,
                'alert_effect': alert_effect
            })

    trip_updates_df = pd.DataFrame(trip_updates_data)
    vehicle_positions_df = pd.DataFrame(vehicle_positions_data)
    alerts_df = pd.DataFrame(alerts_data)

    print("\nTrip Updates DataFrame:")
    print(trip_updates_df)

    print("\nVehicle Positions DataFrame:")
    print(vehicle_positions_df)

    print("\nAlerts DataFrame:")
    print(alerts_df)

except requests.exceptions.RequestException as e:
    print(f"Error downloading the feed: {e}")
except Exception as e:
    print(f"An error occurred: {e}")



trip_updates_df.to_csv('data/trip_updates.csv')
vehicle_positions_df.to_csv('data/vehicle_pos.csv')
alerts_df.to_csv('data/alerts.csv')