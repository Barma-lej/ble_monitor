"""Parser for HolyIOT BLE advertisements"""
import logging
from struct import unpack

from .helpers import (
    to_mac,
    to_unformatted_mac,
)

_LOGGER = logging.getLogger(__name__)


def parse_holyiot(self, data, source_mac, rssi):
    """HolyIOT parser"""
    msg_length = len(data)
    firmware = "HolyIOT"
    result = {"firmware": firmware}

    if msg_length == 17:
        device_type = "HolyIOT BLE tracker"
        holyiot_mac = data[6:12]
        if holyiot_mac != source_mac:
            _LOGGER.debug(
                "HolyIOT MAC address doesn't match data MAC address. Data: %s with source mac: %s and HolyIOT mac: %s",
                data.hex(),
                source_mac,
                holyiot_mac,
            )
            return None
        batt = data[5]
        meas_type = data[14]
        meas_value, = unpack(">H", data[15:17])

        if meas_type == 4:
            measurement_type = "vibration"
        elif meas_type == 6:
            measurement_type = "remote single press"
        else:
            return None
        result.update(
            {
                measurement_type: meas_value,
                "battery": batt
            }
        )
    else:
        if self.report_unknown == "HolyIOT":
            _LOGGER.info(
                "BLE ADV from UNKNOWN HolyIOT DEVICE: RSSI: %s, MAC: %s, ADV: %s",
                rssi,
                to_mac(source_mac),
                data.hex()
            )
        return None

    # check for MAC presence in sensor whitelist, if needed
    if self.discovery is False and holyiot_mac.lower() not in self.sensor_whitelist:
        _LOGGER.debug("Discovery is disabled. MAC: %s is not whitelisted!", to_mac(holyiot_mac))
        return None

    result.update({
        "rssi": rssi,
        "mac": to_unformatted_mac(holyiot_mac),
        "type": device_type,
        "packet": "no packet id",
        "firmware": firmware,
        "data": True
    })
    return result