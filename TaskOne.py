import json


def calculate_weighted_score(json_data):
    total_sum = 0.0

    for item in json_data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        total_sum += score * weight

    return round(total_sum, 3)


# Пример использования
if __name__ == "__main__":
    # путь к JSON-файлу
    with open('input.json', 'r') as file:
        data = json.load(file)
        result = calculate_weighted_score(data)
        print(f"{result}")