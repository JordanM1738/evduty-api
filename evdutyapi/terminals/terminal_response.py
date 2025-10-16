from typing import Any, Dict
from .. import ChargingProfile, NetworkInfo, AccessMode


class TerminalResponse:
    @classmethod
    def from_json_to_network_info(cls, data: Dict[str, Any]) -> NetworkInfo:
        return NetworkInfo(
            wifi_ssid=data['wifiSSID'],
            wifi_rssi=data['wifiRSSI'],
            mac_address=data['macAddress'],
            ip_address=data['localIPAddress'],
        )

    @classmethod
    def from_json_to_charging_profile(cls, data: Dict[str, Any]) -> ChargingProfile:
        current_max = data['amperage']
        power_limitation = 'chargingProfile' in data
        current_limit = data['chargingProfile']['chargingRate'] if power_limitation else current_max
        return ChargingProfile(power_limitation=power_limitation, current_limit=current_limit, current_max=current_max)

    @classmethod
    def from_json_to_access_mode(cls, data: Dict[str, Any]) -> AccessMode | None:
        access_mode_str = data.get('accessMode')
        if access_mode_str is None:
            return None
        try:
            return AccessMode(access_mode_str)
        except ValueError:
            return None
