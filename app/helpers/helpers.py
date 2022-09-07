from geopy.distance import geodesic


def lost_communication_helper(lost) -> dict:
    return {
        "id": str(lost["_id"]),
        "nome": lost["nome"],
        "email": lost["email"],
        "CPF": str(lost["CPF"]),
        "latitude": lost["latitude"],
        "longitude": lost["longitude"],
        "lavoura": lost["lavoura"],
        "data_colheita": lost["data_colheita"],
        "evento": lost["evento"],
    }


def get_distance(lost_latitude, lost_longitute, lost_data_latitude, lost_data_longitude):
    coords_old_data = (lost_latitude, lost_longitute)
    coords_new_data = (lost_data_latitude, lost_data_longitude)
    distance = geodesic(coords_old_data, coords_new_data).km
    print(distance)
    return distance
