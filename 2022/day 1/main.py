import pandas

calories_per_elves = []

with open('elves.txt') as f:
    calories_individual = 0
    #line = f.readline() # this skipped the 1st line in elves.txt bc I use for loop after: https://stackoverflow.com/a/26506797
    for line in f:
        if line == "\n":
            calories_per_elves.append(calories_individual)
            calories_individual = 0
        else:
            calories_individual += int(line.strip())

df = pandas.DataFrame(calories_per_elves, columns=["Calories"])
#df.index.name = "Elf index" #https://stackoverflow.com/a/37968994
#df.index += 1 #starting index at 1

# most_calories = df[df['Calories']==df['Calories'].max()]
# print(most_calories)
print(f"The Elf with the most calories is carrying {df['Calories'].max()} calories.\n")

top_3 = df.nlargest(3, 'Calories')
top_3_sum = top_3.sum().values[0]
print(f"The top 3 Elves are carrying a total of {top_3_sum} calories.")
