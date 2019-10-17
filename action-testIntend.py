#!/usr/bin/env python3

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes

CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


class testIntend(object):
    """Class used to wrap action code with mqtt connection
       Please change the name referring to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except Exception:
            self.config = None

        # start listening to MQTT
        self.start_blocking()

    @staticmethod
    def intent_1_callback(hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(
            intent_message.intent.intent_name))

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(
            intent_message.site_id,
            "Action 1", "Test")

    @staticmethod
    def intent_2_callback(hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")

        # action code goes here...
        print('[Received] intent: {}'.format(
            intent_message.intent.intent_name))

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(
            intent_message.site_id,
            "Action 2", "")

    # --> Register callback function and start MQTT
    def start_blocking(self):
        print('online')
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intent('OleGrue:testIntent', self.intent_1_callback) \
            .start()


if __name__ == "__main__":
    testIntend()

# {
#   "input": "test this",
#   "intent": {
#     "intentName": "OleGrue:testIntend",
#     "confidenceScore": 1
#   },
#   "slots": [
#     {
#       "rawValue": "test this",
#       "value": {
#         "kind": "Custom",
#         "value": "test this"
#       },
#       "range": {
#         "start": 0,
#         "end": 9
#       },
#       "entity": "snips/default--test_slot",
#       "slotName": "test_slot"
#     }
#   ]
# }
