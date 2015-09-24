"""
What exactly I want to do:
Input: random public repo url => mine right now
Output: commits over time
Next: figure out how to get nested info from json ok
Next: stats at a given time
Next:  visualization
Next: pybrain?

Next:
Get information of a group, and plot visualization of their commits

Goal: use hackathon teams github information to analyze team collaboration.

"""

import requests

response = requests.get('https://api.github.com/repos/alinewm/kantare/stats/contributors')

# this is an ok response
assert response.status_code == 200

for contributor in response.json():
    # print specific contributor info, works kind of like a hash
    print '{} {}'.format(contributor['author']['login'], contributor['total'])

hourlyCommits = requests.get('https://api.github.com/repos/alinewm/kantare/stats/punch_card')

assert hourlyCommits.status_code == 200

for hour in hourlyCommits.json():
	print hour
