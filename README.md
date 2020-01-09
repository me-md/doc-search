# Doc Search API 

**Production URL** = https://memd-doc-search.herokuapp.com

This API contains two endpoints that support the MeMD application (https://github.com/me-md/me-md). The **Doctors** endpoint supplies a list of doctors for a given location. The **Providers** endpoint supplies a list of insurance plans with UIDs that can be supplied to the **Doctors** endpoint.

## Endpoints 

### 1. `api/v1/doctors?location=<LOCATION>&provider=<UID>`
* This endpoint returns a list of doctors for a given location

**REQUIREMENTS**
* Must supply a location in query parameters, provider uid is optional
* locations for states must be provided in Postal Abbrievation format i.e (Colorado = 'co', Florida = 'fl')
* locations for cities must include state abbrievation i.e (Denver = 'co-denver', Tama = 'fl-tampa')
* The Providers query param is optional, when using the Providers parameters you must use a valid UID.
* Provider UIDs can be obtained through the `api/v1/providers` endpoint.

**Example Request**
* `https://memd-doc-search.herokuapp.com/api/v1/doctors/?location=co-denver`

**Example Response**
* ``` 
  {
    "practice": {
      "name": "Alan Hanson, MD",
      "location": "co-denver",
      "lat": 39.720454,
      "lon": -104.898461,
      "city": "Denver",
      "state": "CO",
      "street": "130 Rampart Way",
      "street2": "Ste 300B",
      "zip": "80230",
      "phone": "3033274700",
      "uid": "05ece3dc328a4ccdcf1381b9ca0b1440",
      "accepts_new_patients": true,
      "insurance_uids": [
        "aetna-aetnachoiceposii",
        "cigna-cignahmo",
        "aetna-aetnamanagedchoiceposopenaccess",
        "cigna-cignaopenaccessplus",
        "aetna-aetnawholehealthcoloradofrontrange",
        "cigna-cignappo",
        "aetna-aetnasignatureadministratorsppo",
        "aetna-aetnahmo",
        "gwhcigna-greatwestppo",
        "unitedhealthcare-uhcchoicepluspos",
        "unitedhealthcare-uhcnavigatehmo",
        "unitedhealthcare-uhcnavigatepos",
        "unitedhealthcare-uhcoptionsppo"
      ]
    },
    "profile": {
      "first_name": "Alan",
      "middle_name": "S",
      "last_name": "Hanson",
      "title": "MD",
      "school": [
        {
          "school": "University Of Colorado",
          "degree": "residency"
        }
      ],
      "image_url": "https://asset3.betterdoctor.com/assets/general_doctor_male.png",
      "gender": "male",
      "bio": "Dr. Alan Hanson, MD practices medicine at Denver, Colorado and Aurora, Colorado and specializes in internal medicine and nephrology.\n\nDr. Hanson is licensed to practice medicine at Colorado.\n\nDr. Hanson has been found during an automated background check to be clear of any malpractice history and holds one or more active medical licenses."
    }
  },
  {
    "practice": {
      "name": "Metropolitan Ob/gyn",
      "location": "co-denver",
      "lat": 39.73094,
      "lon": -104.93483,
      "city": "Denver",
      "state": "CO",
      "street": "4500 E 9th Ave",
      "street2": "Ste 470",
      "zip": "80220",
      "phone": "3033208499",
      "uid": "f4806250415bdf960f8a39da784a2fa2",
      "accepts_new_patients": true,
      "insurance_uids": [
        "aetna-aetnawholehealthcoloradofrontrange",
        "cigna-cignalocalplus",
        "anthem-anthemcopathway",
        "cigna-cignaopenaccessplus",
        "cigna-cignappo",
        "multiplan-multiplanppo",
        "anthem-anthemppo",
        "multiplan-phcsppo",
        "anthem-anthemcobluepriorityppo",
        "aetna-aetnachoiceposii",
        "aetna-aetnamanagedchoiceposopenaccess",
        "anthem-anthemcopathwayxenhancedinddirectaccess",
        "cigna-cignahmo",
        "aetna-aetnahmo",
        "bcbsbluecard-bcbsbluecardppo",
        "aetna-aetnasignatureadministratorsppo",
        "medicare-medicare",
        "medicaid-medicaid",
        "aetna-aetnamdbronzesilverandgoldhmo",
        "cofinity-cofinityppo",
        "premerabluecross-premeraheritagesignature",
        "premerabluecross-premeralifewiseconnect",
        "gwhcigna-greatwestppo",
        "unitedhealthcare-uhcchoicepluspos",
        "unitedhealthcare-uhcnavigatehmo",
        "unitedhealthcare-uhcnavigatepos",
        "unitedhealthcare-uhcoptionsppo",
        "firsthealthcoventryhealthcare-firsthealthppo",
        "rockymountainhealthplans-rockymountainsummitgroup"
      ]
    },
    "profile": {
      "first_name": "Kristina",
      "middle_name": "B",
      "last_name": "Fraser",
      "title": "MD",
      "school": [
        {
          "school": "University Of Colorado",
          "graduation_year": "Complete in 2003",
          "degree": "residency"
        }
      ],
      "image_url": "https://asset1.betterdoctor.com/assets/general_doctor_female.png",
      "gender": "female",
      "bio": "Dr. Kristina Fraser, MD, specialist in gynecology, obgyn nurse practitioner, obstetrics, and obstetrics & gynecology, currently sees patients in Boulder, Colorado and Denver, Colorado.\n\nDr. Fraser is licensed to practice medicine at Colorado.\n\nIn addition to having active medical licenses, Dr. Fraser has been found during an automated background check to be clear of any malpractice history and holds one or more active medical licenses."
    }
  },

### 2. `api/v1/providers`
* This endpoint returns a list of insurance providers and their UIDs, Names, and Nick Names

**REQUIREMENTS**
* None

**Example Request**
* `https://memd-doc-search.herokuapp.com/api/v1/providers`

**Example Response**
* ``` [
    {
        "uid": "cigna-cignaopenaccessplus",
        "name": "CIGNA Open Access Plus",
        "nick_name": "Cigna"
    },
    {
        "uid": "cigna-cignalocalplus",
        "name": "CIGNA LocalPlus",
        "nick_name": "Cigna"
    },
    {
        "uid": "cigna-cignappo",
        "name": "CIGNA PPO",
        "nick_name": "Cigna"
    },
    {
        "uid": "cigna-cignahmo",
        "name": "CIGNA HMO",
        "nick_name": "Cigna"
    },
    {
        "uid": "aetna-aetnachoiceposii",
        "name": "Aetna Choice POS II",
        "nick_name": "Aetna"
    },
    {
        "uid": "aetna-aetnahmo",
        "name": "Aetna HMO",
        "nick_name": "Aetna"
    },
    {
        "uid": "multiplan-phcsppo",
        "name": "PHCS PPO",
        "nick_name": "Multiplan"
    },
    {
        "uid": "aetna-aetnamanagedchoiceposopenaccess",
        "name": "Aetna Managed Choice POS Open Access",
        "nick_name": "Aetna"
    },
    {
        "uid": "aetna-aetnasignatureadministratorsppo",
        "name": "etna Signature Administrators PPO",
        "nick_name": "Aetna"
    },
    {
        "uid": "multiplan-multiplanppo",
        "name": "Multiplan PPO",
        "nick_name": "Multiplan"
    },
    {
        "uid": "humana-humanacohmoxhix",
        "name": "Colorado - HMOx  HIX",
        "nick_name": "Humana"
    },
    {
        "uid": "medicare-medicare",
        "name": "Medicare",
        "nick_name": "Medicare"
    },
    {
        "uid": "medicaid-medicaid",
        "name": "Medicaid",
        "nick_name": "Medicaid"
    },
    {
        "uid": "aetna-aetnamdbronzesilverandgoldhmo",
        "name": "MD Bronze Silver  Gold - HMO",
        "nick_name": "Aetna"
    },
    {
        "uid": "cofinity-cofinityppo",
        "name": "Cofinity PPO",
        "nick_name": "Aetna"
    },
    {
        "uid": "premerabluecross-premeralifewiseconnect",
        "name": "Premera LifeWise Connect",
        "nick_name": "Blue Cross Blue Shield"
    },
    {
        "uid": "gwhcigna-greatwestppo",
        "name": "Great West PPO",
        "nick_name": "Cigna"
    },
    {
        "uid": "unitedhealthcare-uhcchoicepluspos",
        "name": "UHC Choice Plus POS",
        "nick_name": "United Healthcare"
    },
    {
        "uid": "unitedhealthcare-uhcnavigatehmo",
        "name": "UHC Navigate HMO",
        "nick_name": "United Healthcare"
    },
    {
        "uid": "unitedhealthcare-uhcnavigatepos",
        "name": "UHC Navigate POS",
        "nick_name": "United Healthcare"
    },
    {
        "uid": "unitedhealthcare-uhcoptionsppo",
        "name": "UHC Optioins PPO",
        "nick_name": "United Healthcare"
    },
    {
        "uid": "anthem-anthemcopathway",
        "name": "Anthem CO Pathway",
        "nick_name": "Blue Cross Blue Shield"
    },
    {
        "uid": "anthem-anthemppo",
        "name": "Anthem PPO",
        "nick_name": "Blue Cross Blue Shield"
    }
] 
