# tools.py

import base64

def convert_base64_to_file(base64_string, output_filepath):
    binary_data = base64.b64decode(base64_string)
    with open(output_filepath, 'wb') as file:
        file.write(binary_data)


