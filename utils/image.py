def get_image(activity_type: str) -> str:

    print("type: ", activity_type)
    base_path = "images/"
    image_map = {
        "Pedalada": "bike.png",
        "Corrida": "run.png",
        "Caminhada": "walk.png",
        "Natação": "swim.png",
        "Treinamento com peso": "weight-lifter.png",
        "Caiaque": "kayaking.png",
    }
    return f"{base_path}{image_map.get(activity_type, 'heat-wave.png')}"