def lost_communication_helper(lost) -> dict:
    return {
        "id": str(lost["_id"]),
        "nome": lost["nome"],
        "email": lost["email"],
        "CPF": int(lost["CPF"]),
        "latitude": lost["latitude"],
        "longitude": lost["longitude"],
        "lavoura": lost["lavoura"],
        "data_colheita": lost["data_colheita"],
        "evento": lost["evento"],
    }
