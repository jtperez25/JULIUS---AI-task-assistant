from datetime import datetime

event_list = []
DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def time_key(event):
    time_str = event["time"]
    formats = ["%I:%M %p", "%H:%M", "%I %p", "%H"]
    for fmt in formats:
        try:
            return datetime.strptime(time_str, fmt).time()
        except ValueError:
            continue
    return datetime.strptime("12:00", "%H:%M").time()
            
def main():
    print("\nHello! I'm JULIUS, your personal task and event assistant :]")
    print("I can help you manage your week's schedule.")
    print("\nHere are some commands you can use:")
    print("  - ADD EVENT: Add a new event to your schedule.")
    print("  - REMOVE EVENT: Remove an existing event from your schedule.")
    print("  - VIEW SCHEDULE: View all events scheduled for the week.")
    print("  - HELP: Show this message.")
    print("  - QUIT: Shut down JULIUS.")

    while True:
        command = input("\nHow can I assist you?\n").strip().lower()

        if "add" in command:
            print("\nGreat, let's add an event to your schedule!")
            title = input("Event title: ").title().strip()
            if not title:
                print("Title can't be empty.")
                continue
            else:
                day = input("On which day of the week? (e.g. 'Monday') ").strip().capitalize()
                if day not in DAYS_OF_WEEK:
                    print("Please enter a valid day of the week (e.g. 'Monday').")
                    continue 
                time = input("At what time? (e.g. '6:45 PM or 14:30') ").strip()
                if not time:
                    print("Time can't be empty.")   
                    continue
                priority = input("  Priority (high, medium, low) [default: medium]: ").strip().lower()
                if priority not in ["high", "medium", "low"]:
                    priority = "medium"  # default
                priority = priority.capitalize()  # make it nice: High, Medium, Low
                event = {
                    "title": title,
                    "day": day,
                    "time": time,
                    "priority": priority
                }
                event_list.append(event)
                print(f"  '{title}' added on {day} at {time} ({priority} priority)!\n")
                
        elif "remove" in command:
            if not event_list:
                print("\nYour schedule is currently empty. Add an event to get started!\n")
                continue
            print("\nHere are your current events:")
            for idx, event in enumerate(event_list, 1):
                print(f"  {idx}. {event['title']} on {event['day']} at {event['time']}")
            try:
                to_remove = int(input("Enter the number of the event you want to remove: "))
                if 1 <= to_remove <= len(event_list):
                    removed_event = event_list.pop(to_remove - 1)
                    print(f"{removed_event['title']} has been removed from your schedule.\n")
                else:
                    print("Invalid number. Please try again.\n")
            except ValueError:
                print("Please enter a valid number.\n")

        elif "view" in command or "schedule" in command or "events" in command or "tasks" in command:
            if not event_list:
                print("\nYour schedule is currently empty. Add an event to get started!\n")
                continue
            print('\n' + "=" *70)
            print(" THIS WEEKS SCHEDULE".center(70))
            print("=" *70) 

            for day in DAYS_OF_WEEK:
                events_this_day = [e for e in event_list if e["day"] == day]

                print(f"\n{day.upper()}")
                if not events_this_day:
                    print("     No events scheduled.")
                    continue

                events_this_day.sort(key=time_key)

                for idx, event in enumerate(events_this_day, 1):
                    print(f"    {event['time']}: {event['title']} ({event['priority']} priority)")

            print("\n" + "="*70 + "\n")

        elif 'quit' in command or 'exit' in command or 'shutdown' in command or 'bye' in command:
            print("\nGoodbye! Have A Blessed Day!\n")
            break

        elif "help" in command:
            print("\nI can help you manage your week's schedule with the following commands:")
            print("  - ADD EVENT: Add a new event to your schedule.")
            print("  - REMOVE EVENT: Remove an existing event from your schedule.")
            print("  - VIEW SCHEDULE: View all events scheduled for the week.")
            print("  - HELP: Show this message.")
            print("  - QUIT: Shut down JULIUS.\n")

        else:
            print("\nI'm sorry, I didn't understand that. Type 'help' for commands.\n")

if __name__ == "__main__":
    main()