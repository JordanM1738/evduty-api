from dataclasses import dataclass
from typing import Dict, Any


@dataclass(frozen=True)
class SessionStartResponse:
    id: str
    connecting_time_remaining: float
    target_duration: int
    target_percentage: int
    connector_id: int | None = None
    connector_name: str | None = None
    connector_status: str | None = None

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'SessionStartResponse':
        connector_id = None
        connector_name = None
        connector_status = None
        
        if 'station' in data and 'terminal' in data['station']:
            terminal = data['station']['terminal']
            if 'connector' in terminal:
                connector = terminal['connector']
                connector_id = connector.get('id')
                connector_name = connector.get('name')
                connector_status = connector.get('status')
        
        return cls(
            id=data['id'],
            connecting_time_remaining=data.get('connectingTimeRemaining', 0.0),
            target_duration=data.get('targetDuration', 0),
            target_percentage=data.get('targetPercentage', 0),
            connector_id=connector_id,
            connector_name=connector_name,
            connector_status=connector_status,
        )
