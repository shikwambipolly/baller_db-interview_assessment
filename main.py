from fastapi import FastAPI, Body, HTTPException, status, Header, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List, Optional
from uuid import uuid4
import motor.motor_asyncio

from model import PlayerModel, UpdatePlayerModel

app = FastAPI()

mongo_details = "mongodb://mongodb:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(mongo_details)

database = client.ballers_db

player_collection = database.get_collection("players")

API_KEY: Optional[str] = None

def serialize_player(player):
    player["_id"] = str(player["_id"])
    return player

@app.post("/auth", response_description="Generate API Key")
async def get_api_key():
    global API_KEY
    API_KEY = str(uuid4())
    return {"api_key": API_KEY}

async def verify_api_key(x_api_key: str = Header(...)):
    if API_KEY is None or x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")

@app.post("/createPlayer", response_description="Add new player", response_model=PlayerModel, dependencies=[Depends(verify_api_key)])
async def create_player(player: PlayerModel = Body(...)):
    player = jsonable_encoder(player)
    new_player = await player_collection.insert_one(player)
    created_player = await player_collection.find_one({"_id": new_player.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_player)

@app.get("/getPlayers", response_description="List all players", response_model=List[PlayerModel], dependencies=[Depends(verify_api_key)])
async def list_players():
    players = await player_collection.find().to_list(1000)
    return [serialize_player(player) for player in players]

@app.get("/getPlayer/{id}", response_description="Get a single player", response_model=PlayerModel, dependencies=[Depends(verify_api_key)])
async def show_player(id: str):
    if (player := await player_collection.find_one({"_id": id})) is not None:
        return serialize_player(player)

    raise HTTPException(status_code=404, detail=f"Player {id} not found")

@app.put("/updatePlayer{id}", response_description="Update a player", response_model=PlayerModel, dependencies=[Depends(verify_api_key)])
async def update_player(id: str, player: UpdatePlayerModel = Body(...)):
    player = {k: v for k, v in player.dict().items() if v is not None}

    if len(player) >= 1:
        update_result = await player_collection.update_one({"_id": id}, {"$set": player})

        if update_result.modified_count == 1:
            if (
                updated_player := await player_collection.find_one({"_id": id})
            ) is not None:
                return serialize_player(updated_player)

    if (existing_player := await player_collection.find_one({"_id": id})) is not None:
        return serialize_player(existing_player)

    raise HTTPException(status_code=404, detail=f"Player {id} not found")

@app.delete("/deletePlayer{id}", response_description="Delete a player", dependencies=[Depends(verify_api_key)])
async def delete_player(id: str):
    delete_result = await player_collection.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Player {id} not found")
