class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Added participant. Total participants: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

# Demonstration script
if __name__ == "__main__":
    # Creating Event objects
    event1 = Event("Python Workshop", "2024-08-15")
    event2 = Event("Data Science Seminar", "2024-09-20")

    # Displaying initial participant count
    print(f"{event1.name} on {event1.date}: Participants: {event1.get_participant_count()}")
    print(f"{event2.name} on {event2.date}: Participants: {event2.get_participant_count()}")

    # Adding participants
    event1.add_participant()
    event1.add_participant()
    event2.add_participant()

    # Displaying updated participant count
    print(f"{event1.name} on {event1.date}: Participants: {event1.get_participant_count()}")
    print(f"{event2.name} on {event2.date}: Participants: {event2.get_participant_count()}")
