import asyncio
from dataclasses import asdict
import json
import websockets

from model.dto.base_request_dto import BaseRequestDTO
from model.dto.base_response_dto import BaseResponseDTO
from routes.routes import routes

# TODO:
# 1. Convert text to Emotion
# 2. Reply text with its emotion
async def echo(websocket):
    async for message in websocket:

        try:
            raw_request: BaseRequestDTO = BaseRequestDTO(**json.loads(message))

            response: any = routes(raw_request)
            response_json = json.dumps(asdict(response))
        
        except Exception as e:
            response: BaseResponseDTO = BaseResponseDTO(
                status = False, 
                message = str(e), 
                code = "???", 
                data = None
            )

            response_json = json.dumps(asdict(response))
            
        await websocket.send(response_json.encode())


async def socket_runner():
    async with websockets.serve(echo, "localhost", 61102):
            print("WebSocket Server running at ws://localhost:61102")
            await asyncio.Future()

def socket_initializr():
    asyncio.run(socket_runner())