from homeassistant.const import CONF_ICON, CONF_NAME
from pychonet.lib.epc_functions import _hh_mm

# Panasonic dishwasher-dryers report a countdown in EPC 0xF0, which is past the
# 0xEF the spec defines, so it is proprietary. It is encoded as (hour, minute)
# like the standard time properties: it was observed rolling 0x1600 -> 0x153B,
# i.e. 22:00 -> 21:59, which a plain 16 bit counter would not do. It decrements
# once a minute while the unit is in storage mode (EPC 0xE6 = 0x70) and resets
# to zero when the unit leaves it.


# 0xF0 - Remaining storage (keep) mode time
def _03D5F0(edt):
    return _hh_mm(edt)


QUIRKS = {
    0xF0: {
        "EPC_FUNCTION": _03D5F0,
        "ENL_OP_CODE": {
            CONF_NAME: "Storage mode remaining time",
            CONF_ICON: "mdi:timer-sand",
        },
    },
}
