from doc_search_api.services.better_doctor_service import DocService

class DoctorsFacade:
    def doctors(self, data):
        service = DocService()
        return service.all_docs(data)
