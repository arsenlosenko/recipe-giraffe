
class FoodApiClient(object):
    """
    Abstract class which represents Food API client
    """
    api_url = None

    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def search_recipes(self, *ingridients):
        raise NotImplementedError('method not yet implemented')

    @staticmethod
    def localize_ingredients(ingridients):
        raise NotImplementedError('method not yet implemented')

    @staticmethod
    def localize_response(response):
        raise NotImplementedError('method not yet implemented')
