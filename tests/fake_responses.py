# All fake responses where collected from chromedriver responses


class Dictionary:
    def __init__(self, dictionary) -> None:
        self.dictionary = dictionary

    def json(self):
        return self.dictionary

    def get(self, key):
        return self.dictionary.get(key)


def dict_to_json(dictionary):
    return Dictionary(dictionary)


DEFAULT = dict_to_json(
    {
        "sessionId": "4358a5b53794586af59678fc1653dc40",
        "status": 0,
        "value": {"ELEMENT": "0.8851292311864847-1"},
    }
)

FIND_ELEMENT = DEFAULT
SEND_KEYS = DEFAULT
CLICK = DEFAULT
CLOSE_SESSION = DEFAULT
GO_TO_PAGE = DEFAULT

GET_URL = dict_to_json(
    {
        "sessionId": "af67b8ef665d30a687f37365d229fb53",
        "status": 0,
        "value": "file:///html/playground.html",
    }
)
GET_TIMEOUTS = dict_to_json(
    {
        "sessionId": "10754c8ec2e19133235223f1914ea376",
        "status": 0,
        "value": {"implicit": 0, "pageLoad": 300000, "script": 30000},
    }
)


GET_STATUS = dict_to_json(
    {
        "value": {
            "build": {
                "version": "113.0.5672.63 (0e1a4471d5ae5bf128b1bd8f4d627c8cbd55f70c-refs/branch-heads/5672@{#912})"
            },
            "message": "ChromeDriver ready for new sessions.",
            "os": {"arch": "x86_64", "name": "Linux", "version": "5.4.0-150-generic"},
            "ready": True,
        }
    }
)

GET_TITLE = dict_to_json(
    {
        "sessionId": "07b00b2e94be84920495d83890c82b60",
        "status": 0,
        "value": "Sample page",
    }
)

FIND_ELEMENTS = dict_to_json(
    {
        "sessionId": "9be93a374d185216134bf0c3fafee52e",
        "status": 0,
        "value": [
            {"ELEMENT": "C230605181E69CB2C4C36B8E83FE1245_element_1"},
            {"ELEMENT": "C230605181E69CB2C4C36B8E83FE1245_element_2"},
            {"ELEMENT": "C230605181E69CB2C4C36B8E83FE1245_element_3"},
        ],
    }
)

GET_PROPERTY_VALUE = dict_to_json(
    {
        "sessionId": "5be82d4cd17af92d7ea53a36900d78cb",
        "status": 0,
        "value": "any_value",
    }
)

GET_TEXT = dict_to_json(
    {"sessionId": "5be82d4cd17af92d7ea53a36900d78cb", "status": 0, "value": "any"}
)

GET_SESSION = dict_to_json(
    {
        "sessionId": "4358a5b53794586af59678fc1653dc40",
        "status": 0,
        "value": {
            "acceptInsecureCerts": True,
            "acceptSslCerts": True,
            "applicationCacheEnabled": False,
            "browserConnectionEnabled": False,
            "browserName": "chrome",
            "chrome": {
                "chromedriverVersion": "94.0.4606.41 (333e85df3c9b656b518b5f1add5ff246365b6c24-refs/branch-heads/4606@{#845})",
                "userDataDir": "/tmp/.com.google.Chrome.4zKpeQ",
            },
            "cssSelectorsEnabled": True,
            "databaseEnabled": False,
            "goog:chromeOptions": {"debuggerAddress": "localhost:43565"},
            "handlesAlerts": True,
            "hasTouchScreen": False,
            "javascriptEnabled": True,
            "locationContextEnabled": True,
            "mobileEmulationEnabled": False,
            "nativeEvents": True,
            "networkConnectionEnabled": False,
            "pageLoadStrategy": "normal",
            "platform": "Linux",
            "proxy": {},
            "rotatable": False,
            "setWindowRect": True,
            "strictFileInteractability": False,
            "takesHeapSnapshot": True,
            "takesScreenshot": True,
            "timeouts": {"implicit": 0, "pageLoad": 300000, "script": 30000},
            "unexpectedAlertBehaviour": "ignore",
            "version": "94.0.4606.54",
            "webStorageEnabled": True,
            "webauthn:extension:credBlob": True,
            "webauthn:extension:largeBlob": True,
            "webauthn:virtualAuthenticators": True,
        },
    }
)
