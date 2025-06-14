import requests
import random
import time

BASE_URL = "https://war-service-live.foxholeservices.com/api"

def get_war_status():
    res = requests.get(f"{BASE_URL}/worldconquest/war")
    res.raise_for_status()
    return res.json()

def get_maps():
    res = requests.get(f"{BASE_URL}/worldconquest/maps")
    res.raise_for_status()
    return res.json()

def get_map_dynamic_data(map_name):
    res = requests.get(f"{BASE_URL}/worldconquest/maps/{map_name}/dynamic/public")
    res.raise_for_status()
    return res.json()

def main():
    war = get_war_status()
    # print(f"war: {war}")
    # print("🔹 Wojna trwa:", war["warNumber"])
    # print("🔹 Dzień wojny:", war["dayOfWar"])
    # print("🔹 Zwycięska frakcja (do tej pory):", war.get("winner", "brak"))

    # maps = get_maps()
    # print(f"🔹 Liczba map: {len(maps)}")

    # random_map = random.choice(maps)
    # print("🔹 Losowa mapa:", random_map)

    # dynamic = get_map_dynamic_data(random_map)
    #
    # print("🔹 Przykładowe obiekty na mapie:")
    # for item in dynamic["mapItems"][:5]:  # tylko pierwsze 5
    #     print(f" - {item['teamId']} | {item['iconType']} | x={item['x']}, y={item['y']}")

if __name__ == "__main__":
    main()

