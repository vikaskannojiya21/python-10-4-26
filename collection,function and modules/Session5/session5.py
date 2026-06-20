team = {
    "CSK": {
        "captain": "Dhoni",
        "players": 18
    },
    "MI": {
        "captain": "Rohit",
        "players": 17
    }
}

# Add new team
team["GT"] = {
    "captain": "Hardik",
    "players": 16
}

# Print team names and captains
for name, data in team.items():
    print(name, "-", data["captain"])
