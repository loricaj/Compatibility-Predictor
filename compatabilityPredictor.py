import json

#read json file 
f = open('data.json')
data = json.load(f)

#variables to store the team's stats
sumTeamInt = 0
sumTeamStr = 0
sumTeamEnd = 0
sumTeamSFT = 0

#iterate through team array to get value then sum of attributes
for teamMember in data['team']:
    sumTeamInt += teamMember['attributes']['intelligence']
    sumTeamStr += teamMember['attributes']['strength']
    sumTeamEnd += teamMember['attributes']['endurance']
    sumTeamSFT += teamMember['attributes']['spicyFoodTolerance']

#compute for team average of each attribute
numTeamMembers = len(data['team'])

avgTeamInt = sumTeamInt/numTeamMembers
avgTeamStr = sumTeamStr/numTeamMembers
avgTeamEnd = sumTeamEnd/numTeamMembers
avgTeamSFT = sumTeamSFT/numTeamMembers

#iterate through array to calculate applicant compatability scores and store in object
calculatedScores = {
    "scoredApplications": []
}

for applicant in data['applicants']:

    score = 0
    
    if (applicant['attributes']['intelligence'] > avgTeamInt or 
        abs(applicant['attributes']['intelligence'] - avgTeamInt) < 2):
        score += 0.6
        
    if (applicant['attributes']['strength'] > avgTeamStr or
        abs(applicant['attributes']['strength'] - avgTeamStr) < 2):
        score += 0.1
        
    if (applicant['attributes']['endurance'] > avgTeamEnd or
        abs(applicant['attributes']['endurance'] - avgTeamEnd) < 2):
        score += 0.2
        
    if (applicant['attributes']['spicyFoodTolerance'] > avgTeamSFT or
        abs(applicant['attributes']['spicyFoodTolerance'] - avgTeamSFT) < 2):
        score += 0.1
    
    
    calculatedScores['scoredApplications'].append( {"name": applicant['name'], "score": round(score, 2)} )


print(json.dumps(calculatedScores, indent=3))
