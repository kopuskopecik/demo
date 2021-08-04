import json
import base64

from services.models import Service, ImageTypes
from smart_screen.utils.send_request import send_request
from smart_screen.utils.is_valid_uuid import is_valid_uuid
from smart_screen.settings import BASE_URL


"""
:param image: image in base64 format
:return: {
    id: "image id",
    "etag": "etag"
}, status_code
"""
def create_image(image):
    if not image:
        return None, None
    url = BASE_URL + "/images"
    headers = {
        "Content-Type": "application/octet-stream"
    }
    image = base64.b64decode(image)
    return send_request("POST", url, headers=headers, data=image)

"""
:param image_id: id of an image
:return: image in byte format, status_code
"""
def get_image(image_id):
    headers = {
        "accept": "image/*"
    }
    url = BASE_URL + "/images/" + image_id

    return send_request("GET", url, headers=headers)

"""
:param full_path: it is being used for getting the query params
:return: [Service class], status_code
"""
def get_services(full_path):
    try:
        url = BASE_URL + "/services?" + full_path.split("?")[1]
    except:
        url = BASE_URL + "/services"

    headers = {
        "Content-Type": "application/json"
    }

    return send_request("GET", url, headers=headers)

"""
:param service_id: service id to retrieve a service
:return: Service class, status_code
"""
def get_service(service_id):
    url = BASE_URL + "/services/" + service_id
    return send_request("GET", url)

"""
:param service_id: service id to delete a service
:return: "", status_code
"""
def delete_service(service_id):
    url = BASE_URL + "/services/" + service_id
    return send_request("DELETE", url)

"""
:param service_id: service id to update a service
:param data: new data to update a particular service
:return: Service class, status_code
"""
def update_service(service_id, data):
    service = Service(data)
    images = service.get_images()
    for image in images:
        if images.get(image):
            if image == ImageTypes.LOGO.value:
                image_id_or_base64 = images.get(image).get("id")
                if is_valid_uuid(image_id_or_base64):
                    continue
                else:
                    data, status_code = create_image(images.get(image).get("id"))
                    if status_code == 201:
                        service.setter({image: data})
                    else:
                        return data, status_code
            else:
                image_id_or_base64 = images.get(image).get("default").get("id")
                locales = images.get(image).get("locales")
                if is_valid_uuid(image_id_or_base64):
                    continue
                else:
                    data, status_code = create_image(images.get(image).get("default").get("id"))
                    if status_code == 201:
                        service.setter({image: {"default": data, "locales": locales}})
                    else:
                        return data, status_code
                if locales:
                    for index in range(len(locales)):
                        image_id_or_base64 = locales[index].get("value").get("id")
                        if is_valid_uuid(image_id_or_base64):
                            continue
                        else:
                            data, status_code = create_image(locales[index].get("value").get("id"))
                            if status_code == 201:
                                attribute = service.getter(image)
                                new_locales = {
                                    "language": locales[index].get("language"),
                                    "value": data
                                }
                                attribute["locales"][index] = (new_locales)
                                service.setter({image: attribute})
                            else:
                                return data, status_code

    # return service.__dict__, 200
    url = BASE_URL + "/services/" + service_id

    headers = {
        "Content-Type": "application/json"
    }

    return send_request("POST", url, headers=headers, data=json.dumps(data))


"""
:param data: [Service class]
:return: [Service class], status_code
"""
def create_service(data):
    service = Service(data)
    images = service.get_images()
    for image in images:
        if images.get(image):
            if image == ImageTypes.LOGO.value:
                data, status_code = create_image(images.get(image).get("id"))
                if status_code == 201:
                    service.setter({image: data})
                else:
                    return data, status_code
            else:
                data, status_code = create_image(images.get(image).get("default").get("id"))
                locales = images.get(image).get("locales")
                if status_code == 201:
                    service.setter({image: {"default": data, "locales": locales}})
                else:
                    return data, status_code
                if locales:
                    for index in range(len(locales)):
                        data, status_code = create_image(locales[index].get("value").get("id"))
                        if status_code == 201:
                            attribute = service.getter(image)
                            new_locales = {
                                "language": locales[index].get("language"),
                                "value": data
                            }
                            attribute["locales"][index] = (new_locales)
                            service.setter({image: attribute})
                        else:
                            return data, status_code

    url = BASE_URL + "/services"

    headers = {
        "Content-Type": "application/json"
    }

    return send_request("POST", url, headers=headers, data=json.dumps(service.__dict__))

