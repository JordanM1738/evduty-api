from datetime import datetime, timedelta, timezone
from typing import Any, Dict
try:
    from zoneinfo import ZoneInfo
    HAS_ZONEINFO = True
except ImportError:
    HAS_ZONEINFO = False

from .. import ChargingSession


class ChargingSessionResponse:
    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> ChargingSession:
        try:
            if HAS_ZONEINFO:
                tz = ZoneInfo('US/Eastern')
            else:
                tz = timezone(timedelta(hours=-5))
            start_date = datetime.fromtimestamp(data['chargeStartDate'], tz)
        except Exception:
            start_date = datetime.fromtimestamp(data['chargeStartDate'], timezone.utc)
        
        return ChargingSession(
            is_active=data['isActive'],
            is_charging=data['isCharging'],
            volt=data['volt'],
            amp=data['amp'],
            power=data['power'],
            energy_consumed=data['energyConsumed'],
            start_date=start_date,
            duration=timedelta(seconds=data['duration']),
            cost=ChargingSessionResponse.cost_from_json(data),
            session_id=data.get('sessionId'),
        )

    @classmethod
    def cost_from_json(cls, data):
        return round((data['station']['terminal']['costLocal'] or 0) * data['energyConsumed'] / 1000, 2)
