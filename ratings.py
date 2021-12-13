"""Restaurant rating lister."""

# put your code here
def scoresProcess():
    s = open('scores.txt')
    scores = {}

    for line in s:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)

    return scores

def addRestaurant(scores):

    print("Please add a rating for your favorite restuarant!")
    restaurant = input("Restaurant name> ")
    rating = int(input("Rating> "))

    scores[restaurant] = rating

def sortedScores(scores):

    for restaurant, rating in sorted(scores.items()):
        print(restaurant + " is rated at " + str(rating) + ".")

scores = scoresProcess()
addRestaurant(scores)

sortedScores(scores)