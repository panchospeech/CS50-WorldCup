# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # Creates a variable with the name of the file prompted in argument line
    filename = sys.argv[1]
    # Opens the file and read it
    with open(filename) as f:
        reader = csv.DictReader(f)
        for team in reader:
            # copy the rating in the list team created an change the str to int
            team['rating'] = int(team['rating'])
            # store each team as a dictionary in a list of teams
            teams.append(team)

    counts = {}
    # Simulate N tournaments and keep track of win counts
    for i in range(N):
        winner = simulate_tournament(teams)
        if winner in counts:
            counts[winner] += 1
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")
        # keep track of win counts in the counts dictionary


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    # Starting from 0 where the maximum i value is 7 (lenght of teams - 1), increase i by 2 each time
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # Use simulate_round, which accepts a list of teams and returns a list of winners
    # Repeadtedly simulate rounds until one team is left
    while len(teams) > 1:
        teams = simulate_round(teams)
    # Return name of winning team
    return teams[0]['team']


if __name__ == "__main__":
    main()
