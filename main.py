
from datetime import date

sessions = []
daily_goal = 180

  
def add_session():
    print("\n--- Add Study Session ---")

    subject = input("Subject or skill: ").strip()
    topic = input("Topic studied: ").strip()

    if not subject or not topic:
        print("Subject and topic cannot be empty.")
        return

    try:
        minutes = int(input("Minutes studied: "))

        if minutes <= 0:
            print("Minutes must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid whole number.")
        return

    learned = input("What did you learn? ").strip()

    session = {
        "date": date.today().isoformat(),
        "subject": subject,
        "topic": topic,
        "minutes": minutes,
        "learned": learned
    }

    sessions.append(session)
    print("\nStudy session added successfully!")


def view_sessions():
    print("\n--- All Study Sessions ---")

    if not sessions:
        print("No sessions recorded yet.")
        return

    for number, session in enumerate(sessions, start=1):
        print(f"\nSession {number}")
        print(f"Date: {session['date']}")
        print(f"Subject: {session['subject']}")
        print(f"Topic: {session['topic']}")
        print(f"Duration: {session['minutes']} minutes")
        print(f"Learned: {session['learned']}")


def daily_summary():
    today = date.today().isoformat()

    today_sessions = [
        session for session in sessions
        if session["date"] == today
    ]

    total = sum(
        session["minutes"] for session in today_sessions
    )

    print("\n--- Today's Summary ---")
    print(f"Sessions completed: {len(today_sessions)}")
    print(f"Total study time: {total} minutes")
    print(f"Daily goal: {daily_goal} minutes")

    remaining = max(0, daily_goal - total)
    progress = min(100, total / daily_goal * 100)

    print(f"Progress: {progress:.1f}%")
    print(f"Time remaining to goal: {remaining} minutes")

    if total >= daily_goal:
        print("Congratulations! You reached your goal!")


def set_goal():
    global daily_goal

    try:
        goal = int(input("Enter your daily goal in minutes: "))

        if goal <= 0:
            print("Your goal must be greater than zero.")
            return

        daily_goal = goal
        print(f"Daily goal updated to {daily_goal} minutes.")

    except ValueError:
        print("Please enter a valid whole number.")


def main():
    while True:
        print("\n" + "=" * 32)
        print("STUDENT STUDY TRACKER")
        print("=" * 32)
        print("1. Add study session")
        print("2. View all sessions")
        print("3. View daily summary")
        print("4. Set daily goal")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_session()
        elif choice == "2":
            view_sessions()
        elif choice == "3":
            daily_summary()
        elif choice == "4":
            set_goal()
        elif choice == "5":
            print("Keep learning. See you next time!")
            break
        else:
            print("Invalid option. Choose from 1 to 5.")


if __name__ == "__main__":
    main()
