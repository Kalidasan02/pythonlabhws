# tracker.py

def create_record(city, comment, date):
    """
    Returns a travel record as a dictionary.
    date format: dd-mm-yyyy
    """
    return {
        "city": city,
        "comment": comment,
        "date": date
    }
