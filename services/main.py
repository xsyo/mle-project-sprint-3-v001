from fastapi import FastAPI
from src.shemes import RequestModel, ResponseModel
from src.handler import ModelHandler


app = FastAPI()
model_handler = ModelHandler()


@app.post("/", response_model=ResponseModel)
def model_predict(request_model: RequestModel):
    model_params_dict = dict(request_model.params_model)
    score = model_handler.predict(model_params_dict)

    return {"score": score}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=4555)