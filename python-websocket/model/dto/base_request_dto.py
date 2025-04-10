from dataclasses import dataclass

@dataclass
class BaseRequestDTO():
    route: str
    request: any