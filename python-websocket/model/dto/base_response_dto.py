from dataclasses import dataclass

@dataclass
class BaseResponseDTO():
    status: bool
    message: str
    code: str
    data: any