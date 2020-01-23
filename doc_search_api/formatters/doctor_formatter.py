import json

class DoctorFormatter:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Doctor Formatter'

    def practice(self):
        result = {}
        data = self.data
        result['name'] = data['practices'][0]['name']
        result['location'] = data['practices'][0]['location_slug']
        result['lat'] = data['practices'][0]['lat']
        result['lon'] = data['practices'][0]['lon']
        result['city'] = data['practices'][0]['visit_address']['city']
        result['state'] = data['practices'][0]['visit_address']['state']
        result['street'] = data['practices'][0]['visit_address']['street']
        if 'street2' in data['practices'][0]['visit_address']:
            result['street2'] = data['practices'][0]['visit_address']['street2']
        else:
            result['street2'] = 'N/A'
        result['zip'] = data['practices'][0]['visit_address']['zip']
        result['phone'] = data['practices'][0]['phones'][0]['number']
        result['uid'] = data['practices'][0]['uid']
        result['accepts_new_patients'] = data['practices'][0]['accepts_new_patients']
        result['insurance_uids'] = data['practices'][0]['insurance_uids']
        return result

    def profile(self):
        result = {}
        data = self.data
        result['first_name'] = data['profile']['first_name']
        if 'middle_name' in data['profile']:
            result['middle_name'] = data['profile']['middle_name']
        else:
            result['middle_name'] = 'N/A'
        result['last_name'] = data['profile']['last_name']
        result['title'] = data['profile']['title']
        result['school'] = data['educations']
        result['image_url'] = data['profile']['image_url']
        if 'gender' in data['profile']:
            result['gender'] = data['profile']['gender']
        else:
            result['gender'] = 'N/A'
        result['bio'] = data['profile']['bio']
        return result
