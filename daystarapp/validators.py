

import re

def validate_ugandan_national_id(national_id):
    regex = r'^[A-Z]{2}\d{6}[0-9A-Z]{3}\d[A-Z]$'
    return bool(re.match(regex, national_id))
