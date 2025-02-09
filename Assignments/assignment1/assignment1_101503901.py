#Author: Soojeong Lim
#Assignment: #1

#b
gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5 # float
highest_reps = 25 # int
membership_active = True # boolean


#c
#data type of dictionary is Key-Value
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 35, 40),
    "Taylor": (40, 30, 25)
}

#d
workout_totals = {}
for friend, activities in workout_stats.items():
    total_minutes = sum(activities)
    workout_totals[f"{friend}_Total"] = total_minutes

#e
workout_stats.update(workout_totals)
workout_list = [
    list(workout_stats[friend]) for friend in ["Alex", "Jamie", "Taylor"]
]
#f
print("Yoga and Running minutes:")
for row in workout_list:
    print(row[:2])

print("Weightlifting minutes for the last two friends:")
for row in workout_list[-2:]:
    print(row[2])

#g
for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

#h
friend_name = input("Enter the name of the friend to check their workout record: ")

if f"{friend_name}_Total" in workout_stats:
    activities = workout_stats[friend_name]
    total_minutes = workout_stats[f"{friend_name}_Total"]
    print(f"Workout minutes for {friend_name}:")
    print(f"Yoga: {activities[0]} minutes, Running: {activities[1]} minutes, Weightlifting: {activities[2]} minutes")
    print(f"Total workout minutes: {total_minutes} minutes")
else:
    print(f"Friend {friend_name} not found in the records.")

#i
friends_totals = {friend: workout_stats[f"{friend}_Total"] for friend in ["Alex", "Jamie", "Taylor"]}

max_friend = max(friends_totals, key=friends_totals.get)
min_friend = min(friends_totals, key=friends_totals.get)

print(f"Friend with the highest total workout minutes: {max_friend} ({friends_totals[max_friend]} minutes)")
print(f"Friend with the lowest total workout minutes: {min_friend} ({friends_totals[min_friend]} minutes)")
