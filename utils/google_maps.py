from googleplaces import GooglePlaces
import googlemaps


class GoogleMaps(object):
    def __init__(self, password):
        """

        :param password:
        """
        self._google_maps_key = password
        self._google_places = GooglePlaces(self._google_maps_key)
        self._google_geocode = googlemaps.Client(key=self._google_maps_key)

    def _text_search(self, query, language=None, location=None):
        """

        :param query:
        :param language:
        :param location:
        :return:
        """
        text_query_result = self._google_places.text_search(query=query, language=language, location=location)
        return text_query_result.places


