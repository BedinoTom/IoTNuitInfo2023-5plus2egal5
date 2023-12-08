from utils import request

def registry_device(token, type, name):
    resp = request.get_auth_request(token, "https://nuit-info-2023.apoorva64.com/api/devices?name="+name)
    if len(resp) > 0:
        return resp[0]['id']
    resp = request.post_auth_request(token, "https://nuit-info-2023.apoorva64.com/api/devices", {
        "type": type,
        "name": name
    })
    
    return resp["id"]

def push_data(token, id, temperature, humidity, day, position):
    request.post_auth_request(token, "https://nuit-info-2023.apoorva64.com/api/metrics", {
        "device_id": id,
        "lat": position[0],
        "lng": position[1],
        "temperature": temperature,
        "humidity": humidity,
        "day": True if day == 1 else False
    })
    