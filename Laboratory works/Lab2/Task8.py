def tournament():
    teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
    print("")
    for i, team1 in enumerate(teams, start=1):
        for j, team2 in enumerate(teams, start=1):
            if team1 != team2:
                print(f"- {team1} VS {team2}")
