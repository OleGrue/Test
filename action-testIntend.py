#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import io

CONFIGURATION_ENCODING_FORMAT = "utf-8"
CONFIG_INI = "config.ini"

class SnipsConfigParser(configparser.SafeConfigParser):
    def to_dict(self):
        return {section : {option_name : option for option_name, option in self.items(section)} for section in self.sections()}


def read_configuration_file(configuration_file):
    try:
        with io.open(configuration_file, encoding=CONFIGURATION_ENCODING_FORMAT) as f:
            conf_parser = SnipsConfigParser()
            conf_parser.readfp(f)
            return conf_parser.to_dict()
    except (IOError, configparser.Error) as e:
        return dict()

def subscribe_intent_callback(hermes, intentMessage):
    hermes.publish_end_session(intentMessage.session_id, 'test')
    # conf = read_configuration_file(CONFIG_INI)
    # action_wrapper(hermes, intentMessage, conf)


def action_wrapper(hermes, intentMessage, conf):
    {{#each action_code as |a|}}{{a}}
    {{/each}}


if __name__ == "__main__":
    mqtt_opts = MqttOptions()
    with Hermes(mqtt_options=mqtt_opts) as h:
        h.subscribe_intent("testIntend", subscribe_intent_callback) \
         .start()

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
