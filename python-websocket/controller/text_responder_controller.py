from model.dto.text_responder.text_responder_request_dto import TextResponderRequestDTO
from model.dto.text_responder.text_responder_response_dto import TextResponderResponseDTO

def controller(request: TextResponderRequestDTO) -> TextResponderResponseDTO:
    raise Exception(f"Controller Not implemented. Request: {request}")


def handler():
    raise Exception("Handler Not implemented")
