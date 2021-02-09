def is_service_enabled(services, type):
    for service in services:
        if service["type"] == type:
            if service["enabled"]:
                return True
    return False

def get_param(params, type):
    for param in params:
        if param[type]:
            return param[type]
    return None

def decode(js, type):
    cameras = js["cameras"]
    history = []
    for camera in cameras:
        if is_service_enabled(camera["services"], type):
            history.append(camera)
    return history

def decode_history(js):
    return decode(js, "HISTORY")

def decode_live(js):
    return decode(js, "LIVE")   

def decode_alert(js):
    cameras = js["cameras"]
    alarms = js["alarms"]
    movements = []
    for alarm in alarms:
        if alarm["type"] == "MOVIMENT" and alarm["enabled"]:
            id = get_param(alarm["parameters"],"cameraId")
            if id:
                movements.append(id)
    result = []
    for camera in cameras:
        if camera["id"] in movements:
            result.append(camera)
    return result

def decode_moviment(js):
    cameras = js["cameras"]
    alarms = js["alarms"]
    movements = []
    for alarm in alarms:
        if alarm["type"] == "MOVIMENT" and alarm["enabled"]:
            id = get_param(alarm["parameters"],"cameraId")
            if id:
                movements.append(id)
    result = []
    for camera in cameras:
        if camera["id"] in movements:
            result.append(camera)
    return result

def decode_tag(js):
    return js["monitoringTag"]
        
        