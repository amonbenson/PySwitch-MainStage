from pyswitch.clients.local.actions.encoder_button import ENCODER_BUTTON
from pyswitch.clients.local.actions.custom import CUSTOM_MESSAGE
from pyswitch.controller.actions.AnalogAction import AnalogAction
from pyswitch.colors import Colors
from pyswitch.clients.kemper.mappings.pedals import MAPPING_WAH_PEDAL
from pyswitch.clients.kemper.mappings.pedals import MAPPING_VOLUME_PEDAL
from display import DISPLAY_HEADER_1
from display import DISPLAY_HEADER_2
from pyswitch.hardware.devices.pa_midicaptain_10 import *

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
                message = [176, 102, 127],
                message_release = [176, 102, 0],
                color = (64, 0, 0),
                text = 'Panic (CC 102)'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_2,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 103, 127],
                message_release = [176, 103, 0],
                color = Colors.BLACK,
                text = 'CC 103'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_3,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 104, 127],
                message_release = [176, 104, 0],
                color = Colors.BLACK,
                text = 'CC 104'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_4,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 105, 127],
                message_release = [176, 105, 0],
                color = Colors.BLACK,
                text = 'CC 105'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_UP,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 119, 127],
                message_release = [176, 119, 0],
                color = (64, 32, 0),
                text = 'Previous Patch (CC 119)'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_A,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 106, 127],
                message_release = [176, 106, 0],
                color = Colors.BLACK,
                text = 'CC 106'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_B,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 107, 127],
                message_release = [176, 107, 0],
                color = Colors.BLACK,
                text = 'CC 107'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_C,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 108, 127],
                message_release = [176, 108, 0],
                color = Colors.BLACK,
                text = 'CC 108'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_D,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 109, 127],
                message_release = [176, 109, 0],
                color = Colors.BLACK,
                text = 'CC 109'
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_DOWN,
        "actionsHold": [],
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 118, 127],
                message_release = [176, 118, 0],
                color = (64, 32, 0),
                text = 'Next Patch (CC 118)'
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
                mapping = MAPPING_WAH_PEDAL(),
                change_display = DISPLAY_HEADER_1
            ),

        ],

    },
    {
        "assignment": PA_MIDICAPTAIN_10_EXP_PEDAL_2,
        "actions": [],

    },

]
