
from .parse_standard import *
# import textile
# import pypandoc
import json

def render_standard(standard_file):
    # return 
    with open(standard_file) as f:
        return f"<pre>{f.read()}</pre>"
  