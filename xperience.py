
from orchestator import OrchestatorCommon


class Xperience(OrchestatorCommon):

    def __init__(self, server=None, user=None, password=None, ini_path=None, apikey=None):
        super().__init__(server, user, password, ini_path, apikey)
        self.get_authorization_token()

    def add_queue(self, form_token, **kwargs):

        if self.apikey is None:
            self.get_authorization_token()

        headers = {'Content-Type': 'multipart/form-data',
                   'Authorization': "Bearer " + self.apikey}

        return self.request("post", f'/api/formData/addQueue/{form_token}', kwargs, headers)

    def get_queues(self, form_token):
        if self.apikey is None:
            self.get_authorization_token()

        headers = {'Authorization': "Bearer " + self.apikey}
        url = f'/api/formData/get/{form_token}'
        return self.request("post", url, None, headers)

    def set_queue_status(self, form_token, state):
        if self.apikey is None:
            self.get_authorization_token()

        lock = 0
        status = 0
        if state == "processing":
            lock = 1
        if state == "processed":
            status = 1

        data = {'status': status, 'locked': lock}
        headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': "Bearer " + self.apikey}
        url = f'/api/formData/setStatus/{form_token}'
        return self.request("post", url, data, headers)

    def lock_queue(self, form_token):
        return self.set_queue_status(form_token, "processing")

    def process_queue(self, form_token):
        return self.set_queue_status(form_token, "processed")

    def get_queue_data(self, form_token, id_queue):
        if self.apikey is None:
            self.get_authorization_token()

        url = f'/api/formData/getQueue/{id_queue}/{form_token}'
        headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': "Bearer " + self.apikey}
        
        return self.request("post",url, None, headers)

    def download_file(self, id_queue):
        if self.apikey is None:
            self.get_authorization_token()

        # data = {'file': }
        pass

    def send_message_to_form(self, token, message):
        if self.apikey is None:
            self.get_authorization_token()
            
        data = {'xperience': token, 'data': message}
        headers = {'Authorization': "Bearer " + self.apikey}
        return self.request("post", '/api/form/extra', data, headers)


