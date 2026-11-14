
class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition


class NFLTeam:
    def __init__(self, teamName, playerList):
        self.teamName = teamName
        self.playerList = playerList


# The Players
player1 = Player("Joe Montana", "QB")
player2 = Player("Barry Sanders", "RB")
player3 = Player("Jerry Rice", "WR")
player4 = Player("Graham Gano", "K")

# Add players
playerList = [player1, player2, player3, player4]

# Create the football team
team = NFLTeam("Smashmouth Football", playerList)

# Display team name
print("Team:", team.teamName)

# Display all players
print("Players:")
for player in team.playerList:
    print(player.playerName, "-", player.playerPosition)

