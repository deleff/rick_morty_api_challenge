# rick_morty_api_challenge
The challengest challenge for the rickest Rick

This is a simple Python app that queries the "Rick and Morty" API ('https://rickandmortyapi.com/documentation/#rest') for all the living humans from Earth (C-137).

By querying the app on port 5000, it will return a json comprised of their name, location, and an image link.

Querying port 5000/healthcheck will return a value of {Status: UP}

You can find the Python script, the Dockerfile that runs it, and a Helm template to deploy it in Kubernetes. 

## Requirements to run the script: 
Python3
Pip installing flask
Internet to get the values from the Rick and Morty API

## Suggestions to improve the code:
1. Cache the values from the API (possibly in a Redis server since the values are json). No need to constantly query an external endpoint.

2. Run a cronjob (weekly, after each new episode, or when the values are updated) to store the most up-to-date information

3. Add the ability to use parameters in the GET request (and alter the Python script to consume those parameters instead of hardcoding the type of character it will return). Also, this means that instead of the app running its query once and saving it, it will need to be able to run the query on demand. 

4. Add an autoscaler and the ability to deploy more than just one pod

5. Include a UI with Pickle Rick? Everybody loves Pickle Rick

6. Use a lighter-weight container. Ubuntu is way too large for a job like this

7. Don't run the container as root

## Basic CI process:
1. Create a new branch
2. Gated-check, must pass unit tests and helm linters before it can be merged
3. PR/required approval before merging
4. Automated deployment to staging environment 
5. QA testing, deplyment to canary, then C137 (AKA "Prod")
6. Victory nuggets dipped in that szechuan sauce, Morty!!!
