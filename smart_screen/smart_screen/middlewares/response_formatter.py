from datetime import datetime
import json
import uuid

class ResponseAdditionInfoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        self.request_logger(request, response)
        response = self.render_response(response)
        return response

    def render_response(self, response):
        try:
            rs = json.loads(response.content)
        except:
            rs = None
        if response.status_code == 500:
            message = "Smart Screen is down"
        else:
            try:
                message = rs.get("message")
            except:
                message = ""

        responseObj = {
            "data": rs,
            "status_code": response.status_code,
            "message": message
        }
        response.content = json.dumps(responseObj)
        return response

    def request_logger(self, request, response):
        if(request.user.is_anonymous is False):
            print(uuid.uuid4().hex)
        time_start = datetime.now()
        time_end = datetime.now()
        print(time_end-time_start, request.path)
