import pandas


df = pandas.read_csv('guide.csv', header=None) #adding header without replacing current header: https://stackoverflow.com/a/57579621

'''Splitting rows guide.csv into 2 columns'''
#https://www.geeksforgeeks.org/python-pandas-split-strings-into-two-list-columns-using-str-split/
splitting_column = df[0].str.split(" ", n=1, expand=True)
df["They"] = splitting_column[0]
df["Me"] = splitting_column[1]
df.drop(columns=0, inplace=True)

'''Switching their letters to Rock/Paper/Scissors'''
for index, row in df.iterrows():
    if row[0] == "A":
        df.loc[index, "They"] = "Rock".format(row[0])
    elif row[0] == "B":
        df.loc[index, "They"] = "Paper".format(row[0])
    elif row[0] == "C":
        df.loc[index, "They"] = "Scissors".format(row[0])

# '''PART 1'''
#'''Switching my letters to Rock/Paper/Scissors'''
#for index, row in df.iterrows():
    # if row[1] == "X":
    #     df.loc[index, "Me"] = "Rock".format(row[1])
    # elif row[1] == "Y":
    #     df.loc[index, "Me"] = "Paper".format(row[1])
    # elif row[1] == "Z":
    #     df.loc[index, "Me"] = "Scissors".format(row[1])

'''PART 2'''
'''Determining my shapes based on theirs'''
for index, row in df.iterrows():
    if row[1] == "X" and row[0] == "Rock" \
            or row[1] == "Y" and row[0] == "Scissors" \
            or row[1] == "Z" and row[0] == "Paper":
                df.loc[index, "Me"] = "Scissors".format(row[1])
    elif row[1] == "X" and row[0] == "Scissors" \
            or row[1] == "Y" and row[0] == "Paper" \
            or row[1] == "Z" and row[0] == "Rock":
                df.loc[index, "Me"] = "Paper".format(row[1])
    elif row[1] == "X" and row[0] == "Paper" \
            or row[1] == "Y" and row[0] == "Rock" \
            or row[1] == "Z" and row[0] == "Scissors":
                df.loc[index, "Me"] = "Rock".format(row[1])


'''Adding points columns to pandas Dataframe'''
#adding empty columns to a df: https://stackoverflow.com/a/43995812
headers_list = ["They", "Me", "shape-points", "outcome-points", "TOTAL-POINTS"]
df = df.reindex(columns=headers_list)

'''Counting points for my Rock/Paper/Scissor shape'''
for index, row in df.iterrows():
    if row[1] == "Rock":
        df.loc[index, "shape-points"] = "1".format(row[2])
    if row[1] == "Paper":
        df.loc[index, "shape-points"] = "2".format(row[2])
    if row[1] == "Scissors":
        df.loc[index, "shape-points"] = "3".format(row[2])

'''Counting points for the outcome'''
for index, row in df.iterrows():
    # a draw
    if row[1] == row[0]:
        df.loc[index, "outcome-points"] = "3".format(row[3])
    # my win
    elif row[1] == "Rock" and row[0] == "Scissors" \
            or row[1] == "Paper" and row[0] == "Rock" \
            or row[1] == "Scissors" and row[0] == "Paper":
        df.loc[index, "outcome-points"] = "6".format(row[3])
    # my loss
    elif row[1] == "Rock" and row[0] == "Paper" \
            or row[1] == "Paper" and row[0] == "Scissors" \
            or row[1] == "Scissors" and row[0] == "Rock":
        df.loc[index, "outcome-points"] = "0".format(row[3])

'''Counting total points per round'''
for index, row in df.iterrows():
    df.loc[index, "TOTAL-POINTS"] = f"{int(row[2])+int(row[3])}".format(row[4])

'''Counting total points - stat''' #https://www.geeksforgeeks.org/how-to-convert-string-to-integer-in-pandas-dataframe/
total = df['TOTAL-POINTS'].astype(int).sum()

if __name__ == '__main__':
    print(total)
