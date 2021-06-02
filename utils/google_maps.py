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

    def _reverse_geocode(self, lat, lng, language=None):
        """

        :param lat:
        :param lng:
        :param language:
        :return:
        """
        list_reverse_geocode = self._google_geocode.reverse_geocode((lat, lng), language=language)
        return list_reverse_geocode

    def _return_reverse_geocode_info(self, lat, lng, language=None):
        """

        :param lat:
        :param lng:
        :param language:
        :return:
        """
        list_reverse_geocode = self._reverse_geocode(lat, lng, language=language)
        if list_reverse_geocode:
            city = ''
            pincode = ''
            route = ''
            neighborhood = ''
            sublocality = ''
            administrative_area_level_1 = ''
            country = ''
            street_number = ''

            formatted_address = list_reverse_geocode[0]['formatted_address']
            for address_info in list_reverse_geocode[0]['address_components']:
                if 'locality' in address_info['types']:
                    city = address_info['long_name']
                elif 'postal_code' in address_info['types']:
                    pincode = address_info['long_name']
                elif 'route' in address_info['types']:
                    route = address_info['long_name']
                elif 'neighborhood' in address_info['types']:
                    neighborhood = address_info['long_name']
                elif 'sublocality' in address_info['types']:
                    sublocality = address_info['long_name']
                elif 'administrative_area_level_1' in address_info['types']:
                    administrative_area_level_1 = address_info['long_name']
                elif 'country' in address_info['types']:
                    country = address_info['long_name']
                elif 'street_number' in address_info['types']:
                    street_number = address_info['long_name']

                return {'city': city, 'pincode': pincode, 'route': route, 'neighborhood': neighborhood,
                        'sublocality': sublocality, 'administrative_area_level_1': administrative_area_level_1,
                        'country': country, 'formatted_address': formatted_address, 'street_number': street_number}

        else:
            return None

