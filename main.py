user_name = input("Welcome to GC mini golf! What is your name? ")
holes = input(f"Hi, {user_name}! Would you like to play 3 or 6 holes? ")

# Number of holes/prompt accordingly
if holes == "3":
    par_values = [3, 3, 3]
elif holes == "6":
    par_values = [3, 3, 3, 3, 3, 3]
else:
    print("Invalid input. Please enter 3 or 6 for the number of holes.")
    exit()
even_par = 0
total_score = 0

# Loop
for hole_num, par in enumerate(par_values, start=1):
    putts = int(input(f"How many putts for hole {hole_num}? "))
    total_score += putts - par

# Display score
if total_score == even_par:
    print(f"Good game, {user_name}! Your total par was: {total_score}.")
elif total_score <= even_par:
    print(f"Great game, {user_name}! Your total par was: {total_score}.")
elif total_score >= even_par:
    print(f"Nice try, {user_name}! Your total par was: +{total_score}.")




