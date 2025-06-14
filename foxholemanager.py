import requests
import random
from datetime import datetime

BASE_URL = "https://war-service-live.foxholeservices.com/api"

class FoxholeManager:
    def get_war_status(self):
        res = requests.get(f"{BASE_URL}/worldconquest/war")
        res.raise_for_status()
        return res.json()

    def get_maps(self):
        res = requests.get(f"{BASE_URL}/worldconquest/maps")
        res.raise_for_status()
        return res.json()

    def get_map_dynamic_data(self, map_name):
        res = requests.get(f"{BASE_URL}/worldconquest/maps/{map_name}/dynamic/public")
        res.raise_for_status()
        return res.json()

    def format_timestamp(self, ms):
        return datetime.fromtimestamp(ms / 1000).strftime('%Y-%m-%d %H:%M:%S')

    def main(self):
        war = self.get_war_status()
        print("🪖 Wojna ID:", war["warId"])
        print("🔹 Wojna nr:", war["warNumber"])
        print("📆 Start wojny:", self.format_timestamp(war["conquestStartTime"]))
        print("🏆 Zwycięzca:", war["winner"])
        print("📊 Towns do zwycięstwa:", war["requiredVictoryTowns"])

        maps = self.get_maps()
        print(f"\n🌍 Liczba map: {len(maps)}")
        #
        random_map = random.choice(maps)
        print("🎯 Losowa mapa:", random_map)

        dynamic = self.get_map_dynamic_data(random_map)

        print("\n📌 Obiekty na mapie:")
        for item in dynamic["mapItems"]:
            print(f" - Frakcja: {item['teamId']}, Typ: {item['iconType']}, Koordynaty: ({item['x']}, {item['y']})")


    # print(f"dynamic: {dynamic}")
if __name__ == "__main__":
    # main()
    x = FoxholeManager()
    x.main()

