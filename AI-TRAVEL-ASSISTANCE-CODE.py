import random
from datetime import datetime, timedelta

class TravelAssistant:
    def __init__(self):
        self.destinations = {
            "paris": {"country": "France", "best_season": "Spring/Fall", "budget": "$$-$$$"},
            "tokyo": {"country": "Japan", "best_season": "Spring/Fall", "budget": "$$$"},
            "bali": {"country": "Indonesia", "best_season": "Apr-Oct", "budget": "$-$$"},
            "new york": {"country": "USA", "best_season": "Spring/Fall", "budget": "$$$"},
            "rome": {"country": "Italy", "best_season": "Spring/Fall", "budget": "$$"},
            "dubai": {"country": "UAE", "best_season": "Nov-Mar", "budget": "$$$"},
            "bangkok": {"country": "Thailand", "best_season": "Nov-Feb", "budget": "$"},
        }
        
        self.attractions = {
            "paris": ["Eiffel Tower", "Louvre Museum", "Notre-Dame", "Arc de Triomphe"],
            "tokyo": ["Senso-ji Temple", "Tokyo Tower", "Shibuya Crossing", "Mount Fuji"],
            "bali": ["Ubud Monkey Forest", "Tanah Lot Temple", "Rice Terraces", "Beach Clubs"],
            "new york": ["Statue of Liberty", "Central Park", "Times Square", "Brooklyn Bridge"],
            "rome": ["Colosseum", "Vatican City", "Trevi Fountain", "Roman Forum"],
        }
        
    def greet(self):
        print("\n🌍 Welcome to AI Travel Assistant! 🌍")
        print("=" * 50)
        print("I can help you with:")
        print("1. Destination recommendations")
        print("2. Travel itinerary planning")
        print("3. Budget estimation")
        print("4. Packing list")
        print("5. Travel tips")
        print("=" * 50)
    
    def recommend_destination(self, budget, interests):
        print(f"\n✈️  Based on your {budget} budget and interest in {interests}...")
        
        recommendations = []
        for dest, info in self.destinations.items():
            if budget.lower() in info["budget"].lower():
                recommendations.append(dest)
        
        if recommendations:
            chosen = random.choice(recommendations)
            info = self.destinations[chosen]
            print(f"\n🎯 I recommend: {chosen.upper()}")
            print(f"   Country: {info['country']}")
            print(f"   Best time to visit: {info['best_season']}")
            print(f"   Budget level: {info['budget']}")
        else:
            print("Let me suggest some popular destinations:")
            for dest in list(self.destinations.keys())[:3]:
                print(f"  • {dest.upper()}")
    
    def create_itinerary(self, destination, days):
        destination = destination.lower()
        print(f"\n📅 {days}-Day Itinerary for {destination.upper()}")
        print("-" * 50)
        
        if destination in self.attractions:
            attractions = self.attractions[destination]
            for day in range(1, min(days + 1, len(attractions) + 1)):
                print(f"\nDay {day}:")
                if day <= len(attractions):
                    print(f"  Morning: Visit {attractions[day-1]}")
                    print(f"  Afternoon: Explore nearby area & lunch")
                    print(f"  Evening: Local cuisine & nightlife")
        else:
            print(f"Itinerary template for {destination}:")
            for day in range(1, days + 1):
                print(f"\nDay {day}: Explore main attractions and local culture")
    
    def estimate_budget(self, destination, days, travelers):
        base_costs = {
            "$": {"flight": 400, "hotel": 50, "food": 25, "activities": 30},
            "$$": {"flight": 600, "hotel": 100, "food": 50, "activities": 60},
            "$$$": {"flight": 1000, "hotel": 200, "food": 100, "activities": 100},
        }
        
        destination = destination.lower()
        if destination in self.destinations:
            budget_level = self.destinations[destination]["budget"].split("-")[0]
            costs = base_costs[budget_level]
        else:
            costs = base_costs["$$"]
        
        flight_cost = costs["flight"] * travelers
        accommodation = costs["hotel"] * days * travelers
        food = costs["food"] * days * travelers
        activities = costs["activities"] * days * travelers
        
        total = flight_cost + accommodation + food + activities
        
        print(f"\n💰 Budget Estimate for {destination.upper()}")
        print("-" * 50)
        print(f"Flights: ${flight_cost:,}")
        print(f"Accommodation ({days} nights): ${accommodation:,}")
        print(f"Food: ${food:,}")
        print(f"Activities: ${activities:,}")
        print("-" * 50)
        print(f"TOTAL ESTIMATE: ${total:,}")
        print(f"Per person: ${total//travelers:,}")
    
    def generate_packing_list(self, destination, season):
        essentials = ["Passport", "Travel insurance", "Phone charger", "Medications"]
        clothing = ["Comfortable walking shoes", "Underwear", "Socks"]
        
        if season.lower() in ["summer", "spring"]:
            clothing.extend(["T-shirts", "Shorts", "Sunglasses", "Sunscreen", "Hat"])
        else:
            clothing.extend(["Jacket", "Sweaters", "Long pants", "Scarf"])
        
        print(f"\n🎒 Packing List for {destination}")
        print("-" * 50)
        print("Essentials:")
        for item in essentials:
            print(f"  ☐ {item}")
        print("\nClothing:")
        for item in clothing:
            print(f"  ☐ {item}")
    
    def travel_tips(self, destination):
        tips = [
            "Book flights and hotels in advance for better prices",
            "Learn basic phrases in the local language",
            "Keep copies of important documents",
            "Research local customs and etiquette",
            "Get travel insurance",
            "Download offline maps",
            "Notify your bank about travel plans",
            "Pack light and leave room for souvenirs",
        ]
        
        print(f"\n💡 Travel Tips for {destination.upper()}")
        print("-" * 50)
        for i, tip in enumerate(tips[:5], 1):
            print(f"{i}. {tip}")

def main():
    assistant = TravelAssistant()
    assistant.greet()
    
    while True:
        print("\n" + "=" * 50)
        print("What would you like to do?")
        print("1. Get destination recommendation")
        print("2. Create itinerary")
        print("3. Estimate budget")
        print("4. Get packing list")
        print("5. Travel tips")
        print("6. Exit")
        
        choice = input("\nEnter choice (1-6): ")
        
        if choice == "1":
            budget = input("Your budget level (Low/Medium/High): ")
            interests = input("Your interests (beach/culture/adventure/city): ")
            assistant.recommend_destination(budget, interests)
        
        elif choice == "2":
            destination = input("Destination: ")
            days = int(input("Number of days: "))
            assistant.create_itinerary(destination, days)
        
        elif choice == "3":
            destination = input("Destination: ")
            days = int(input("Number of days: "))
            travelers = int(input("Number of travelers: "))
            assistant.estimate_budget(destination, days, travelers)
        
        elif choice == "4":
            destination = input("Destination: ")
            season = input("Season (Summer/Winter/Spring/Fall): ")
            assistant.generate_packing_list(destination, season)
        
        elif choice == "5":
            destination = input("Destination: ")
            assistant.travel_tips(destination)
        
        elif choice == "6":
            print("\n✈️  Safe travels! Goodbye! 🌍")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
