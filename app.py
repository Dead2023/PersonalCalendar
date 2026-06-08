from datetime import datetime

current_info = datetime.now()
def main():
    #TODO add a website to this for offline use
    
    events = []
    amount = int(input("Enter the amount of events: "))
    for i in range(amount):
        event = input("Enter the name of the homework:")
        day = input("Enter at what day the homework is due: ")
        month = input("Enter at what month the homework is due: ")
        year = input("Enter at what year the homework is due: ")
        submission = int(input("Which format is it sumbitted (Inclass = 0, Online = 1)"))
        date = day + "/" + month + "/" + year
        events.append([event, date,submission,i])

    for row in events:
        print(f"{row[0]} {row[1]}")
    return events
def calculate_order(events):
    # This seprates the events into overdue and not.
    if not events:
        print("No events to prioritize.")
        return
    overdue_events = []
    upcoming_events = []
    for event, date, submission, index in events:
        if datetime.strptime(date, "%d/%m/%Y")<current_info:
            overdue_events.append((event,date,submission,index))
        else:
            upcoming_events.append((event,date,submission,index))
    # priority calc. Prioritizes by due date but then when there is a tie breaker ap is used and even if that doesn't work then time submited will be used
    upcoming_events.sort(
        key=lambda x: (
            x[1], 
            not (x[0].split()[0] == "AP" if x[0].split() else False),
            x[2],
            x[3]
        )
    )

    for event, date,submission,index in upcoming_events:
        print(f"{event} {date} {submission} {index}")


if __name__ == "__main__":
    events = main()
    calculate_order(events)