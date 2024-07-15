class DataProcessingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process request data here
        response = self.get_response(request)
        # Process response data here
        return response
