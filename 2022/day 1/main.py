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


if __name__ == '__main__':
    top_1 = df['Calories'].max()
    print(f"The Elf with the most calories is carrying {top_1} calories.\n")

    top_3 = df.nlargest(3, 'Calories')
    top_3_sum = top_3.sum().values[0]
    print(f"The top 3 Elves are carrying a total of {top_3_sum} calories.")


#Naming the index column
#df.index.name = "Elf index" #https://stackoverflow.com/a/37968994

#starting index at 1
#df.index += 1

#Displaying the entire Series with the most calories
# most_calories = df[df['Calories']==df['Calories'].max()]



