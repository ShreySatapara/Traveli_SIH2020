DEFAULT_LOCATION = 'gandhinagar'
def _get_city(request):
    """
    Get's the user location from the query, defaulting to San Francisco if none provided

    Args:
        request (Request): contains info about the conversation up to this point (e.g. domain,
          intent, entities, etc)

    Returns:
        string: resolved location entity
    """
    city_entity = next((e for e in request.entities if e['type'] == 'city'), None)

    if city_entity:
        return city_entity['text']
    else:
        # Default to San Francisco
        return DEFAULT_LOCATION

