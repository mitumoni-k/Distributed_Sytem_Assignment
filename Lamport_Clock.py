class LamportClock:
    def __init__(self, process_id):
        self.process_id = process_id
        self.clock = 0

    def tick(self):
        """Increment the clock for an internal event."""
        self.clock += 1

    def send_event(self):
        """Simulate sending an event, returning the updated clock value."""
        self.tick()
        print(f"Process {self.process_id} sends event with clock = {self.clock}")
        return self.clock

    def receive_event(self, received_clock):
        """Update the clock upon receiving an event from another process."""
        self.clock = max(self.clock, received_clock) + 1
        print(f"Process {self.process_id} received event and updated clock = {self.clock}")

    def __str__(self):
        return f"Process {self.process_id} clock = {self.clock}"




def test_lamport_clock():
    
    process1 = LamportClock(process_id=1)
    process2 = LamportClock(process_id=2)
    process3 = LamportClock(process_id=3)

    print("\nInitial state:")
    print(process1)
    print(process2)
    print(process3)

    print("\nSequence of Events:")

    # Process 1 performs an internal event
    process1.tick()
    print(f"Process 1 internal event: {process1}")

    # Process 1 sends an event to Process 2
    timestamp1 = process1.send_event()

    # Process 2 receives the event from Process 1
    process2.receive_event(timestamp1)

    # Process 2 performs an internal event
    process2.tick()
    print(f"Process 2 internal event: {process2}")

    # Process 2 sends an event to Process 3
    timestamp2 = process2.send_event()

    # Process 3 receives the event from Process 2
    process3.receive_event(timestamp2)

    # Process 3 sends an event back to Process 1
    timestamp3 = process3.send_event()

    # Process 1 receives the event from Process 3
    process1.receive_event(timestamp3)

    print("\nFinal state:")
    print(process1)
    print(process2)
    print(process3)


test_lamport_clock()
