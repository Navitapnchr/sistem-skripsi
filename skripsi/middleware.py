import logging

logger = logging.getLogger(__name__)

class SkripsiLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Mencatat aktivitas user yang mengakses API
        logger.info(f"Akses API: {request.method} {request.path}")
        
        response = self.get_response(request)
        return response