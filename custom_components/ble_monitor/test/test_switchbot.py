"""The tests for the Switchbot ble_parser."""
from ble_monitor.ble_parser import BleParser


class TestSwitchbot:
    """Tests for the Switchbot parser"""
    def test_meter_th_s1(self):
        """Test Switchbot parser for Meter TH S1."""
        data_string = "043e2802010401f269352207ce1c11071bc5d5a50200b89fe6114d22000da2cb0916000d54006400990ec7"
        data = bytes(bytearray.fromhex(data_string))
        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Switchbot"
        assert sensor_msg["type"] == "Meter TH S1"
        assert sensor_msg["mac"] == "CE07223569F2"
        assert sensor_msg["packet"] == "no packet id"
        assert sensor_msg["data"]
        assert sensor_msg["temperature"] == 25.0
        assert sensor_msg["humidity"] == 14
        assert sensor_msg["battery"] == 100
        assert sensor_msg["rssi"] == -57

    def test_meter_th_plus(self):
        """Test Switchbot parser for Meter TH plus."""
        data_string = "043e160201040122df7526f9c40a09163dfd6900640098a6ac"
        data = bytes(bytearray.fromhex(data_string))
        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Switchbot"
        assert sensor_msg["type"] == "Meter TH plus"
        assert sensor_msg["mac"] == "C4F92675DF22"
        assert sensor_msg["packet"] == "no packet id"
        assert sensor_msg["data"]
        assert sensor_msg["temperature"] == 24.0
        assert sensor_msg["humidity"] == 38
        assert sensor_msg["battery"] == 100
        assert sensor_msg["rssi"] == -84

    def test_meter_th_plus_neg_temp(self):
        """Test Switchbot parser for Meter TH plus with negative temperature."""
        data_string = "043e280201040122df7526f9c41c0201060EFF6909C4F92675DF22DC030096A909163DFD6900ba031938C7"
        data = bytes(bytearray.fromhex(data_string))
        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Switchbot"
        assert sensor_msg["type"] == "Meter TH plus"
        assert sensor_msg["mac"] == "C4F92675DF22"
        assert sensor_msg["packet"] == "no packet id"
        assert sensor_msg["data"]
        assert sensor_msg["temperature"] == -25.3
        assert sensor_msg["humidity"] == 56
        assert sensor_msg["battery"] == 58
        assert sensor_msg["rssi"] == -57

    def test_meter_tho_battery(self):
        """Test Switchbot parser for Meter THO."""
        data_string = "043e1302010401f269352207ce0706163dfd7700e4c7"
        data = bytes(bytearray.fromhex(data_string))
        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Switchbot"
        assert sensor_msg["type"] == "Meter THO"
        assert sensor_msg["mac"] == "CE07223569F2"
        assert sensor_msg["packet"] == "no packet id"
        assert sensor_msg["data"]
        assert sensor_msg["battery"] == 228
        assert sensor_msg["rssi"] == -57

    def test_meter_tho_temp_humi(self):
        """Test Switchbot parser for Meter THO."""
        data_string = "043e1c02010401f269352207ce100fff6909d65d706dc117c70300973b00c7"
        data = bytes(bytearray.fromhex(data_string))
        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Switchbot"
        assert sensor_msg["type"] == "Meter THO"
        assert sensor_msg["mac"] == "CE07223569F2"
        assert sensor_msg["packet"] == "no packet id"
        assert sensor_msg["data"]
        assert sensor_msg["temperature"] == -0.7
        assert sensor_msg["humidity"] == 59
        assert sensor_msg["rssi"] == -57
