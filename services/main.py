from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Counter

from src.shemes import RequestModel, ResponseModel
from src.handler import ModelHandler


app = FastAPI()
model_handler = ModelHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)


main_app_predictions = Histogram(
    "main_app_predictions",
    "Гистограмма прогнозов",
    buckets=(8_500_000, 10_800_000, 14_000_000)
) 

mian_app_more_avg_predictions = Counter("mian_app_more_avg_predictions", "Количество предсказаний больше среднего")


@app.post("/", response_model=ResponseModel)
def model_predict(request_model: RequestModel):
    model_params_dict = dict(request_model.params_model)
    score = model_handler.predict(model_params_dict)

    main_app_predictions.observe(score) 

    if score >= 0:
        mian_app_more_avg_predictions.inc()

    return {"score": score}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=4555)