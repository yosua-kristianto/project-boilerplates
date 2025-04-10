from model.dto.text_to_emotion.text_to_emotion_request_dto import TextToEmotionRequestDTO
from model.dto.text_to_emotion.text_to_emotion_response_dto import TextToEmotionResponseDTO

def controller(request: TextToEmotionRequestDTO) -> TextToEmotionResponseDTO:
    raise Exception(f"Controller Not implemented. Request: {request}")


def handler():
    raise Exception("Handler Not implemented")
