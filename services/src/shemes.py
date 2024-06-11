from pydantic import BaseModel



class ModelParams(BaseModel):
    floor: int
    kitchen_area: float
    living_area: float
    rooms: int
    is_apartment: bool
    studio: bool
    total_area: float
    build_year: int
    building_type_int: int
    latitude: float
    longitude: float
    ceiling_height: float
    flats_count: int
    floors_total: int
    has_elevator: bool


class RequestModel(BaseModel):
    user_id: str
    params_model: ModelParams


class ResponseModel(BaseModel):
    score: float
