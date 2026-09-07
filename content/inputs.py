from pyswitch.clients.local.actions.encoder_button import ENCODER_BUTTON
from pyswitch.clients.local.actions.custom import CUSTOM_MESSAGE
from pyswitch.controller.actions.AnalogAction import AnalogAction
from pyswitch.controller.client import ClientParameterMapping
from pyswitch.colors import Colors
from pyswitch.clients.kemper.mappings.pedals import MAPPING_WAH_PEDAL
from pyswitch.clients.kemper.mappings.pedals import MAPPING_VOLUME_PEDAL
from display import DISPLAY_HEADER_1
from display import DISPLAY_HEADER_2
from pyswitch.hardware.devices.pa_midicaptain_10 import *
from adafruit_midi.control_change import ControlChange

_accept = ENCODER_BUTTON()

_cancel = ENCODER_BUTTON()

Inputs = [
    {
        "assignment": PA_MIDICAPTAIN_10_WHEEL_ENCODER,
        "actions": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_1,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 107, 127],
                message_release = [176, 107, 0],
                color = (64, 0, 0),
                text = 'Panic (CC 107)'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_2,
        "actions": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_3,
        "actions": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_4,
        "actions": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_UP,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 108, 127],
                message_release = [176, 108, 0],
                color = (64, 32, 0),
                text = 'Previous Patch (CC 108)'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_A,
        "actions": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_B,
        "actions": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_C,
        "actions": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_D,
        "actions": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_DOWN,
        "actionsHold": [],
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 109, 127],
                message_release = [176, 109, 0],
                color = (64, 32, 0),
                text = 'Next Patch (CC 109)'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_WHEEL_BUTTON,
        "actions": [],
        "actionsHold": [],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_1,
        "actions": [
            AnalogAction(
                mapping = ClientParameterMapping.get(
                    name = "Expression",
                    set = ControlChange(
                        11, 
                        0
                    )
                ),
                change_display = DISPLAY_HEADER_1
            ),
        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_2,
        "actions": [],

    },

]
