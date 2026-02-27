class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code before view
        print("Before view")

        response = self.get_response(request)

        # Code after view
        print("After view")

        return response