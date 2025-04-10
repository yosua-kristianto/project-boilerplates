from dataclasses import dataclass


@dataclass
class TextToEmotionResponseDTO:
    text: str
    emotion_id: int
    emotion: str