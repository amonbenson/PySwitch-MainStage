from pyswitch.clients.local.actions.encoder_button import ENCODER_BUTTON
from pyswitch.clients.local.actions.custom import CUSTOM_MESSAGE
from pyswitch.controller.actions.AnalogAction import AnalogAction
from pyswitch.controller.client import ClientParameterMapping
from pyswitch.colors import Colors, dim_color
from pyswitch.clients.kemper.mappings.pedals import MAPPING_WAH_PEDAL
from pyswitch.clients.kemper.mappings.pedals import MAPPING_VOLUME_PEDAL
from display import DISPLAY_HEADER_1
from display import DISPLAY_HEADER_2
from pyswitch.hardware.devices.pa_midicaptain_10 import *
from adafruit_midi.control_change import ControlChange

SWITCH_BRIGHTNESS = 0.25

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
                color = dim_color(Colors.RED, SWITCH_BRIGHTNESS),
                text = 'Panic (CC 107)'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_2,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 110, 127],
                message_release = [176, 110, 0],
                color = dim_color(Colors.BLACK, SWITCH_BRIGHTNESS),
                text = 'Unassigned'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_3,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 111, 127],
                message_release = [176, 111, 0],
                color = dim_color(Colors.BLACK, SWITCH_BRIGHTNESS),
                text = 'Unassigned'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_4,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 112, 127],
                message_release = [176, 112, 0],
                color = dim_color(Colors.BLACK, SWITCH_BRIGHTNESS),
                text = 'Unassigned'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_UP,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 108, 127],
                message_release = [176, 108, 0],
                color = dim_color(Colors.ORANGE, SWITCH_BRIGHTNESS),
                text = 'Previous Patch (CC 108)'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_A,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 103, 127],
                message_release = [176, 103, 0],
                color = dim_color(Colors.BLACK, SWITCH_BRIGHTNESS),
                text = 'CC 103'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_B,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 104, 127],
                message_release = [176, 104, 0],
                color = dim_color(Colors.BLACK, SWITCH_BRIGHTNESS),
                text = 'CC 104'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_C,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 105, 127],
                message_release = [176, 105, 0],
                color = dim_color(Colors.BLACK, SWITCH_BRIGHTNESS),
                text = 'CC 105'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_D,
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 106, 127],
                message_release = [176, 106, 0],
                color = dim_color(Colors.BLACK, SWITCH_BRIGHTNESS),
                text = 'CC 106'
            ),
        ],
    },
    {
        "assignment": PA_MIDICAPTAIN_10_SWITCH_DOWN,
        "actionsHold": [],
        "actions": [
            CUSTOM_MESSAGE(
                message = [176, 109, 127],
                message_release = [176, 109, 0],
                color = dim_color(Colors.ORANGE, SWITCH_BRIGHTNESS),
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
                    name = "Expr",
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
