def get_image(activity_type: str) -> str:
    print("type: ", activity_type)
    base_path = "images/"
    image_map = {
        "Pedalada": "bike.png",
        "Corrida": "run.png",
        "Caminhada": "walk.png",
        "Natação": "swim.png",
        "Treinamento com peso": "weight-lifter.png",
        "Esporte aquático": "kayaking.png",
    }
    return f"{base_path}{image_map.get(activity_type, 'heat-wave.png')}"

def display_elevation(activity_type: str) -> bool:
    match activity_type:
        case "Pedalada":
            return True
        case "Corrida":
            return True
        case "Caminhada":
            return True
        case _:
            return False
    
    return False