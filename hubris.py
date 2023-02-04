import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import defaultdict

# read in csv file of power rankings data
# file should be clean and have only the expected columns with no additional rows
df = pd.read_csv("S3_Power_Rankings.csv")

# team data for plotting later
# colors are very not final
teams = [
    {
        "name": "Baltimore Crabs",
        "primary color": "#593037",
        "secondary color": "#f7630c"
    },
    {
        "name": "Boston Flowers",
        "primary color": "#d791e3",
        "secondary color": "#393a17"
    },
    {
        "name": "Broken Ridge Jazz Hands",
        "primary color": "#6388ad",
        "secondary color": "#f3ca40"
    },
    {
        "name": "Seattle Garages",
        "primary color": "#2606d7",
        "secondary color": "#ff2423"
    },
    {
        "name": "Canada Moist Talkers",
        "primary color": "#ed1c24",
        "secondary color": "#e5f4f5"
    },
    {
        "name": "Charleston Shoe Thieves",
        "primary color": "#ffce0a",
        "secondary color": "#fcf2d0"
    },
    {
        "name": "LA Unlimited Tacos",
        "primary color": "#9822d3",
        "secondary color": "#facf33"
    },
    {
        "name": "Miami Dale",
        "primary color": "#bf00ff",
        "secondary color": "#33ffff"
    },
    {
        "name": "Dallas Steaks",
        "primary color": "#8c8d8f",
        "secondary color": "#FFFFFF"
    },
    {
        "name": "Hades Tigers",
        "primary color": "#5c1c1c",
        "secondary color": "#e85637"
    },
    {
        "name": "Mexico City Wild Wings",
        "primary color": "#693f26",
        "secondary color": "#ff4f00"
    },
    {
        "name": "Philly Pies",
        "primary color": "#008080",
        "secondary color": "#ec970b"
    },
    {
        "name": "Hawai'i Fridays",
        "primary color": "#3ee652",
        "secondary color": "#f8b93a"
    },
    {
        "name": "San Francisco Lovers",
        "primary color": "#f193b3",
        "secondary color": "#d2264a"
    },
    {
        "name": "Kansas City Breath Mints",
        "primary color": "#178f55",
        "secondary color": "#ff0011"
    },
    {
        "name": "Chicago Firefighters",
        "primary color": "#8c2a3e",
        "secondary color": "#ff960a"
    },
    {
        "name": "Yellowstone Magic",
        "primary color": "#fcb040",
        "secondary color": "#bf1e2e"
    },
    {
        "name": "New York Millennials",
        "primary color": "#f8d6d7",
        "secondary color": "#99cde3"
    },
    {
        "name": "Moab Hellmouth Sunbeams",
        "primary color": "#fffbab",
        "secondary color": "#e8c877"
    },
    {
        "name": "Tokyo Lift",
        "primary color": "#e536c8",
        "secondary color": "#faf0f9"
    },
    {
        "name": "Core Mechanics",
        "primary color": "#ff430a",
        "secondary color": "#858585"
    },
    {
        "name": "Atlantis Georgias",
        "primary color": "#00dbc2",
        "secondary color": "#5cffec"
    },
    {
        "name": "Ohio Worms",
        "primary color": "#5c4822",
        "secondary color": "#ba9c65"
    },
    {
        "name": "Houston Spies",
        "primary color": "#67556b",
        "secondary color": "#9e82a4"
    }
]

custom_palette = {
    "Baltimore Crabs": "#593037",
    "Boston Flowers": "#d791e3",
    "Broken Ridge Jazz Hands": "#6388ad",
    "Seattle Garages": "#2606d7",
    "Canada Moist Talkers": "#ed1c24",
    "Charleston Shoe Thieves": "#ffce0a",
    "LA Unlimited Tacos": "#9822d3",
    "Miami Dale": "#bf00ff",
    "Dallas Steaks": "#8c8d8f",
    "Hades Tigers": "#5c1c1c",
    "Mexico City Wild Wings": "#693f26",
    "Philly Pies": "#008080",
    "Hawai'i Fridays": "#3ee652",
    "San Francisco Lovers": "#f193b3",
    "Kansas City Breath Mints": "#178f55",
    "Chicago Firefighters": "#8c2a3e",
    "Yellowstone Magic": "#fcb040",
    "New York Millennials": "#f8d6d7",
    "Moab Hellmouth Sunbeams": "#fffbab",
    "Tokyo Lift": "#e536c8",
    "Core Mechanics": "#ff430a",
    "Atlantis Georgias": "#00dbc2",
    "Ohio Worms": "#5c4822",
    "Houston Spies": "#67556b"
}

df.drop([24, 25, 26, 27, 28, 29], inplace=True)
df.drop(columns=["Unnamed: 0", "Unnamed: 1"], inplace=True)
df.sort_values(by="Avg rank", inplace=True)
df.drop(columns=["S1 Rank", "S2 Rank", "S3 Rank", "Division", "Avg rank", "StDev", "Blurb Claimed", "Blurb Submitted"], inplace=True)

df["Name"] = df["Home"] + " " + df["Team"]

df.drop(columns=["Home", "Team"], inplace=True)

# df["Rankings"] = df.drop("Home", axis=1).apply(pd.to_numeric, axis=1).agg(list, axis=1);

temp = df.drop("Name", axis=1).apply(pd.to_numeric)
temp["Name"] = df["Name"]
melted = temp.melt(id_vars="Name")
melted = melted.rename(columns={"value": "Rankings"})

# Overall Plot
axis = sns.boxplot(data=melted, y="Rankings", x="Name", hue="Name", orient="v", palette=custom_palette, dodge=False, boxprops={"linewidth": 0.5}, medianprops={"linewidth": 0.8})
axis.tick_params(axis="x", labelrotation=30)
plt.xticks(ha="right")
plt.subplots_adjust(bottom=0.3, left=0.2)
axis.set(xlabel=None)
axis.get_legend().remove()
axis.invert_yaxis()
fig = axis.get_figure()
fig.set_figwidth(10)
fig.savefig("output/overall.png", transparent=False)

# reset plot in between runs
plt.clf()
plt.subplots_adjust(bottom=0.1, left=0.1)

# Individual Team Plots
for t in teams:
    name = t["name"]
    axis = sns.boxplot(x=melted[melted["Name"] == name]["Rankings"], color=t["primary color"], medianprops={"linewidth": 2, "color": t["secondary color"]})
    axis.grid(axis='x', linestyle=':')
    axis.set_axisbelow(True)
    axis.spines['top'].set_visible(False)
    axis.spines['left'].set_visible(False)
    axis.spines['right'].set_visible(False)
    axis.tick_params(left=False)
    axis.set(xlabel=None)

    fig = axis.get_figure()
    fig.savefig(f"output/{name}.png", transparent=False)
    plt.clf()
