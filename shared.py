nationality_to_continent = {
    'Indian': 'Asia',
    'Chinese': 'Asia',
    'American': 'North America',
    'Canadian': 'North America',
    'British': 'Europe',
    'French': 'Europe',
    'Emirati': 'Asia',
    'Malaysian': 'Asia',
    'Lebanese': 'Asia',
    'Thai': 'Asia',
    'Macedonian': 'Europe',
    'Pakistani': 'Asia',
    'Iranian': 'Asia',
    'Japanese': 'Asia',
    'Hungarian': 'Europe',
    'Colombian': 'South America',
    'Argentinian': 'South America',
    'Slovak': 'South America',  # Note: Slovakia is actually in Europe
    'Turkish': 'Asia',
    'Ecuadorian': 'South America',
    'Chilean': 'South America',
    'Czech': 'Europe',
    'Peruvian': 'South America',
    'Filipino': 'Asia',
    'Mexican': 'North America',
    'Serbian': 'Europe',
    'Russian': 'Asia',
    'German': 'Europe',
    'Austrian': 'Europe',
    'Polish': 'Europe',
    'Danish': 'Europe',
    'Italian': 'Europe',
    'Australian': 'Oceania',
    'Portuguese': 'Europe',
    'Kazakh': 'Asia',
    'Greek': 'Europe',
    'Spanish': 'Europe',
    'Bulgarian': 'Europe',
    'New Zealander': 'Oceania',  # Also commonly "Kiwi"
    'Brazilian': 'South America',
    'Dutch': 'Europe',
    'Croatian': 'Europe',
    'Romanian': 'Europe',
    'Swiss': 'Europe',
    'Singaporean': 'Asia'
}

_question_filenames = {
    "OUS": "questions/OUS.json",
    "GGB": "questions/GreatestGoodBenchmark.json",
}

def get_questions(source):
    filename = _question_filenames[source]
    import json
    return json.load(open(filename, "r"))
