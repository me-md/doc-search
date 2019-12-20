class Doctor:
    def __init__(self, data):
        self.practice = load_practice(data)
        self.profile = load_profile(data)

    def load_practice(data):
        result = {}
        result['name'] = data['practices'][0]['name']
        result['location'] = data['practices'][0]['location_slug']
        result['lat'] = data['practices'][0]['lat']
        result['lon'] = data['practices'][0]['lon']
        result['city'] = data['practices'][0]['visit_address']['city']
        result['state'] = data['practices'][0]['visit_address']['state']
        result['street'] = data['practices'][0]['visit_address']['street']
        result['street2'] = data['practices'][0]['visit_address']['street2']
        result['zip'] = data['practices'][0]['visit_address']['zip']
        result['uid'] = data['practices'][0]['uid']
        result['accepts_new_patients'] = data['practices'][0]['accepts_new_patients']
        result['insurance_uids'] = data['practices'][0]['insurance_uids']
        return result

    def load_profile(data):
        result = {}
        result['first_name'] = data['profile']['first_name']
        result['middle_name'] = data['profile']['middle_name']
        result['last_name'] = data['profile']['last_name']
        result['title'] = data['profile']['title']
        result['school'] = data['educations'][0]['school']
        result['image_url'] = data['profile']['image_url']
        result['gender'] = data['profile']['gender']
        result['bio'] = data['profile']['bio']
        return result
