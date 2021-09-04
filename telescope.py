from orchestator import OrchestatorCommon
import os

class Telescope(OrchestatorCommon):

    def __init__(self, server=None, user=None, password=None, ini_path=None, apikey=None):
        super().__init__(server, user, password, ini_path, apikey)
        self.get_authorization_token()
        self.FILES_SUPPORTED = ('.jpg', '.jpeg', '.pdf', 'png')

    def upload_document(self, document_path, template_id):
        data = {'template_token': template_id}
        file_handle = open(document_path, 'rb')
        response = self.request('post', '/process/async', data, {'Authorization': "Bearer " + self.apikey}, files=file_handle)
        file_handle.close()
        return response

    def upload_documents(self, document_folder, template_id):
        files = {}
        documents = [file for file in os.listdir(document_folder) if file.endswith(self.FILES_SUPPORTED)]
        data = {'template_token': template_id}
        for document in documents:
            document_name = os.path.splitext(document)[0]
            document_path = os.path.join(document_folder, document)
            files[document_name] = open(document_path, 'rb')
        
        response = self.request("post", "/api/process/batch", data, {'Authorization': "Bearer " + self.apikey}, files)
        for file in files:
            files[file].close()
        return response

    def get_status(self, token):
        endpoint = 'api/result/check/' + token
        return self.request("post", endpoint, None, {'Authorization': "Bearer " + self.apikey})
    
    def get_result(self, token):
        endpoint = 'api/result/get/' + token
        return self.request("post", endpoint, None, {'Authorization': "Bearer " + self.apikey} )