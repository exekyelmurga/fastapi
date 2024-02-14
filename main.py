from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = 'resnet'
    lenet = 'lenet'

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


#ejemplo simple de un GET de 'Hola Mundo'

@app.get("/")
async def read_root():
    return {"Hola": "Mundo"}

#ejemplo de un GET un poco mas complejo con un id

@app.get("/items/{item_id}")
def read_time(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# ejemplo con el parametro PUT y con params

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

#ejemplo con ENUM

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

#ejemplo de Path convertor, devuelve la ruta en si misma.

@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}