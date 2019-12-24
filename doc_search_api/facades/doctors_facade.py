from doc_search_api.services.better_doctor_service import DocService

class DoctorsFacade:
    def doctors(self, location):
        service = DocService()
        return service.all_docs(location)
