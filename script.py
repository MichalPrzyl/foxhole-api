import requests
import random
from datetime import datetime

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

def format_timestamp(ms):
    return datetime.fromtimestamp(ms / 1000).strftime('%Y-%m-%d %H:%M:%S')

def main():
    war = get_war_status()
    print("🪖 Wojna ID:", war["warId"])
    print("🔹 Wojna nr:", war["warNumber"])
    print("📆 Start wojny:", format_timestamp(war["conquestStartTime"]))
    print("🏆 Zwycięzca:", war["winner"])
    print("📊 Towns do zwycięstwa:", war["requiredVictoryTowns"])

    maps = get_maps()
    print(f"\n🌍 Liczba map: {len(maps)}")
    #
    random_map = random.choice(maps)
    print("🎯 Losowa mapa:", random_map)

    dynamic = get_map_dynamic_data(random_map)

    print("\n📌 Obiekty na mapie:")
    for item in dynamic["mapItems"]:
        print(f" - Frakcja: {item['teamId']}, Typ: {item['iconType']}, Koordynaty: ({item['x']}, {item['y']})")


    # print(f"dynamic: {dynamic}")
if __name__ == "__main__":
    main()

