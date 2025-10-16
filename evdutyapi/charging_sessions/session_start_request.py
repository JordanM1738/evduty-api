from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class SessionStartRequest:
    """Request model for starting a charging session"""
    station_id: str
    terminal_id: str
    connector_id: int = 1
    duration: int = 0
    target_duration: int = 86400
    target_energy: int = 80000
    target_percentage: int = 100
    time_remaining: int = 0

    def to_json(self) -> Dict[str, Any]:
        return {
            "duration": self.duration,
            "station": {
                "hasPlans": False,
                "id": self.station_id,
                "isOwner": False,
                "isPartialOwner": False,
                "isRoot": False,
                "levels": [],
                "links": [],
                "status": "unknown",
                "terminal": {
                    "connector": {
                        "id": self.connector_id
                    },
                    "id": self.terminal_id
                },
                "terminals": []
            },
            "targetDuration": self.target_duration,
            "targetEnergy": self.target_energy,
            "targetPercentage": self.target_percentage,
            "terminalStatus": {},
            "timeRemaining": self.time_remaining
        }
