
from dataclasses import dataclass


@dataclass
class TextResponderResponseDTO:
    text: str
    response: str