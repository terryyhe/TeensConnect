from decouple import config
from google.oauth2 import service_account
import googleapiclient.discovery
import datetime
import pytz

#CAL_ID = 'stq3blrn94u6g3b86pj1jotu48@group.calendar.google.com'
CAL_ID = config('CAL_ID')
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = './teensconnect-credentials.json'

def getEvents():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get('items', [])
    return events

def getFutureEvents():
    all_events = getEvents()
    events = []
    now = pytz.UTC.localize(datetime.datetime.now())

    for event in all_events:
        if 'start' in event:
            if 'dateTime' in event['start']:
                if datetime.datetime.strptime(event['start']['dateTime'],'%Y-%m-%dT%H:%M:%S%z') > now \
                        or 'recurrence' in event:
                    events.append(event)
            elif 'date' in event['start']:
                if datetime.datetime.strptime(event['start']['date']+'-07:00','%Y-%m-%d%z') > now \
                        or 'recurrence' in event:
                    events.append(event)
    return events

def test_calendar():
    print("RUNNING TEST_CALENDAR()")

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # CREATE A NEW EVENT
    new_event = {
    'summary': "Ben Hammond Tech's Super Awesome Event",
    'location': 'Denver, CO USA',
    'description': 'https://benhammond.tech',
    'start': {
        'date': f"{datetime.date.today()}",
        'timeZone': 'America/New_York',
    },
    'end': {
        'date': f"{datetime.date.today() + datetime.timedelta(days=3)}",
        'timeZone': 'America/New_York',
    },
    }
    service.events().insert(calendarId=CAL_ID, body=new_event).execute()
    print('Event created')

 # GET ALL EXISTING EVENTS
    events_result = service.events().list(calendarId=CAL_ID, maxResults=2500).execute()
    events = events_result.get('items', [])

    # LOG THEM ALL OUT IN DEV TOOLS CONSOLE
    for e in events:

        print(e)

    #uncomment the following lines to delete each existing item in the calendar
    #event_id = e['id']
        # service.events().delete(calendarId=CAL_ID, eventId=event_id).execute()


    return events
