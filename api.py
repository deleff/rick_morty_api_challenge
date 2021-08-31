import flask
import urllib.request, json


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# 1. Query "Rick and Morty" API and look for All characters
with urllib.request.urlopen("https://rickandmortyapi.com/api/character") as url:
  data = json.loads(url.read().decode())


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return '{Status: UP}'


@app.route('/', methods=['GET'])
def home():
#    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1. Query "Rick and Morty" API and look for All characters that meets the following conditions:
# a. Species is "Human"
# b. Status is "Alive"
# c. Origin is "Earth (C-137)"
    characters = []

    for each in data['results']:
      if each['status'] == 'Alive' and each['species'] == 'Human' and each['origin']['name'] == 'Earth (C-137)':
        character = {'name': each['name'], 'location': each['location']['name'], 'image': each['image']}
        characters.append(character)

    living_earthers = json.dumps(characters)
    return living_earthers

app.run(debug=True, host='0.0.0.0')
