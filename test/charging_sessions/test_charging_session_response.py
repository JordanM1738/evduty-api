import unittest
from datetime import datetime, timedelta, timezone
try:
    from zoneinfo import ZoneInfo
    HAS_ZONEINFO = True
except ImportError:
    HAS_ZONEINFO = False

from evdutyapi.charging_sessions.charging_session_response import ChargingSessionResponse
from .charging_session_response_builder import ChargingSessionResponseBuilder


class ChargingSessionResponseTest(unittest.TestCase):
    def test_parses_response(self):
        response = ChargingSessionResponseBuilder.default().build()

        session = ChargingSessionResponse.from_json(response)

        if HAS_ZONEINFO:
            try:
                expected_start_date = datetime.fromtimestamp(response['chargeStartDate'], ZoneInfo('US/Eastern'))
            except Exception:
                expected_start_date = datetime.fromtimestamp(response['chargeStartDate'], timezone(timedelta(hours=-5)))
        else:
            expected_start_date = datetime.fromtimestamp(response['chargeStartDate'], timezone(timedelta(hours=-5)))

        self.assertEqual(session.is_active, response['isActive'])
        self.assertEqual(session.is_charging, response['isCharging'])
        self.assertEqual(session.volt, response['volt'])
        self.assertEqual(session.amp, response['amp'])
        self.assertEqual(session.power, response['power'])
        self.assertEqual(session.energy_consumed, response['energyConsumed'])
        self.assertEqual(session.start_date, expected_start_date)
        self.assertEqual(session.duration, timedelta(seconds=response['duration']))
        self.assertEqual(session.cost, round(response['station']['terminal']['costLocal'] * (response['energyConsumed'] / 1000), 2))
        self.assertEqual(session.session_id, response['id'])

    def test_parses_response_without_cost_local(self):
        response = ChargingSessionResponseBuilder.default().with_cost(None).build()

        session = ChargingSessionResponse.from_json(response)

        self.assertEqual(session.cost, 0)
