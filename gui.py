import eel
from random import randint
import jinja2 as jinja2

eel.init("web")

# Start the index.html file
eel.start(
    'templates/index.html',
    jinja_templates='templates'
)