import collections

room_numbers = {
    'CSC101': '3004',
    'CSC102': '4501',
    'CSC103': '6755',
    'NET110': '1244',
    'COM241': '1411'
}

instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

meeting_times = {
    'CSC101': ('Monday', '8:00 a.m.'),
    'CSC102': ('Tuesday', '9:00 a.m.'),
    'CSC103': ('Wednesday', '10:00 a.m.'),
    'NET110': ('Thursday', '11:00 a.m.'),
    'COM241': ('Friday', '1:00 p.m.')
}

# Function to display course information
def display_course_info(course_number):
    if course_number in room_numbers:
        room = room_numbers[course_number]
        instructor = instructors[course_number]
        meeting_day, meeting_time = meeting_times[course_number]
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_day} at {meeting_time}")
    else:
        print("Course not found.")

# Function to check if a course conflicts with the existing schedule
def is_conflict(course_number, schedule):
    meeting_day, _ = meeting_times[course_number]
    return course_number in schedule or meeting_day in schedule.values()

# Main program
print("Welcome to the Class Advisor!")
print("I'm here to help you build your class schedule.")

schedule = {}

while True:
    course_number = input("Enter a course number to add (or 'q' to quit): ")
    if course_number == 'q':
        break
    
    if course_number not in room_numbers:
        print("Course not found. Please enter a valid course number.")
    elif is_conflict(course_number, schedule):
        print("This course conflicts with your existing schedule. Please choose another course.")
    else:
        display_course_info(course_number)
        confirm = input("Do you want to add this course to your schedule? (y/n): ")
        if confirm.lower() == 'y':
            schedule[course_number] = meeting_times[course_number][0]
            print("Course added to your schedule.")
    
    print()  # Add a blank line for readability

print("Here is your weekly schedule:")
sorted_schedule = collections.OrderedDict(sorted(schedule.items(), key=lambda x: list(meeting_times.values()).index(meeting_times[x[0]])))

for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    print(f"\n{day}:")
    for course, meeting_day in sorted_schedule.items():
        if meeting_day == day:
            _, meeting_time = meeting_times[course]
            print(f"  {course} - {meeting_time}")

print("\nThank you for using the Class Advisor. Have a great semester!")
