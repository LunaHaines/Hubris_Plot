import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import defaultdict

# read in csv file of power rankings data
# file should be clean and have only the expected columns with no additional rows
df = pd.read_csv("S3_Power_Rankings.csv")

# team data for plotting later
teams = [
    {
        "name": "Chicago Firefighters",
        "primary color": "#8c2a3e",
        "secondary color": "#ff960a"
    }
]

df.drop([24, 25, 26, 27, 28, 29], inplace=True)
df.drop(columns=["Unnamed: 0", "Unnamed: 1"], inplace=True)
df.drop(columns=["S1 Rank", "S2 Rank", "S3 Rank", "Division", "Avg rank", "StDev", "Blurb Claimed", "Blurb Submitted"], inplace=True)

df["Name"] = df["Home"] + " " + df["Team"]

df.drop(columns=["Home", "Team"], inplace=True)

# df["Rankings"] = df.drop("Home", axis=1).apply(pd.to_numeric, axis=1).agg(list, axis=1);

temp = df.drop("Name", axis=1).apply(pd.to_numeric)
temp["Name"] = df["Name"]
melted = temp.melt(id_vars="Name")
melted = melted.rename(columns={"value": "Rankings"})

# Overall Plot
# axis = sns.boxplot(data=melted, y="Rankings", x="Name", orient="v")
# axis.tick_params(axis="x", labelrotation=30)
# plt.xticks(ha="right")
# plt.subplots_adjust(bottom=0.3, left=0.2)

# Individual Plot
axis = sns.boxplot(x=melted[melted["Name"] == teams[0]["name"]]["Rankings"], color=teams[0]["primary color"], medianprops={"linewidth": 2, "color": teams[0]["secondary color"]})
axis.grid(axis='x', linestyle=':')
axis.set_axisbelow(True)
axis.spines['top'].set_visible(False)
axis.spines['left'].set_visible(False)
axis.spines['right'].set_visible(False)
axis.tick_params(left=False)

# Both
axis.set(xlabel=None)

fig = axis.get_figure()
fig.savefig('output/test.png', transparent=True)
plt.clf()
