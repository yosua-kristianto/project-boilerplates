from model.dto.base_request_dto import BaseRequestDTO

from controller.text_responder_controller import controller as TextResponderController
from controller.text_to_emotion_controller import controller as TextToEmotionController


def routes(raw_request: BaseRequestDTO) -> any:

    command: str = raw_request.route

    if command == "text-responder":
        return TextResponderController(raw_request.request)
    elif command == "text-to-emotion":
        return TextToEmotionController(raw_request.request)
    else:
        raise Exception("Command not found!")