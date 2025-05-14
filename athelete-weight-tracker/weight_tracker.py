import datetime

# Sample data structure: { "Name": [{"date": date, "weight": weight}, ...] }
athletes = {}

def add_athlete(name):
    if name not in athletes:
        athletes[name] = []
        print(f"Athlete '{name}' added.")
    else:
        print(f"Athlete '{name}' already exists.")

def log_weight(name, weight):
    if name in athletes:
        date = datetime.date.today().isoformat()
        athletes[name].append({"date": date, "weight": weight})
        print(f"Weight logged for {name}: {weight} kg on {date}")
    else:
        print("Athlete not found. Please add them first.")

def view_history(name):
    if name in athletes and athletes[name]:
        print(f"\nWeight History for {name}:")
        for record in athletes[name]:
            print(f" - {record['date']}: {record['weight']} kg")
    else:
        print("No records found.")

def check_weight(name, target_weight):
    if name in athletes and athletes[name]:
        latest = athletes[name][-1]['weight']
        print(f"{name}'s latest weight: {latest} kg")
        if latest > target_weight:
            print(f"⚠️ Over target by {latest - target_weight:.1f} kg")
        elif latest < target_weight:
            print(f"✅ Under target by {target_weight - latest:.1f} kg")
        else:
            print("🎯 At target weight!")
    else:
        print("No weight logged yet.")

def main():
    while True:
        print("\n--- Athlete Weight Tracker ---")
        print("1. Add Athlete")
        print("2. Log Weight")
        print("3. View Weight History")
        print("4. Check Target Weight")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            name = input("Enter athlete name: ").strip()
            add_athlete(name)

        elif choice == '2':
            name = input("Enter athlete name: ").strip()
            try:
                weight = float(input("Enter weight (kg): "))
                log_weight(name, weight)
            except ValueError:
                print("Invalid weight.")

        elif choice == '3':
            name = input("Enter athlete name: ").strip()
            view_history(name)

        elif choice == '4':
            name = input("Enter athlete name: ").strip()
            try:
                target = float(input("Enter target weight (kg): "))
                check_weight(name, target)
            except ValueError:
                print("Invalid weight.")

        elif choice == '5':
            print("Exiting code. Stay strong!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
