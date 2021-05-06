import json
import lang

language = lang.languages

with open('lang.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(language, indent=4))
