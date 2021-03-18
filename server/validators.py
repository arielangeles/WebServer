""" App validators. """

def validate_key_parse(data):
    """
    Validate key is a numerical value string and parse it.

    :param dict data: Data to be validated
    """
    validated_data = {int(key): str(value) for key, value
                      in data.items() if key.isdigit()}

    return validated_data if len(validated_data) == len(data) else None