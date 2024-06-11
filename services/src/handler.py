
"""Класс FastApiHandler, который обрабатывает запросы API."""

from joblib import load
import pandas as pd



class ModelHandler:
    """Класс Model, который обрабатывает запрос и возвращает предсказание."""

    def __init__(self):
        """Инициализация переменных класса."""
        

        self.model_path = "models/pipeline.joblib"
        self.load_model(model_path=self.model_path)
        
        # необходимые параметры для предсказаний модели оттока
        self.required_model_params = [
            'floor', 'kitchen_area', 'living_area', 'rooms', 'is_apartment',
            'studio', 'total_area', 'build_year', 'building_type_int',
            'latitude', 'longitude', 'ceiling_height', 'flats_count',
            'floors_total', 'has_elevator'
        ]

    def load_model(self, model_path: str):
        """Загружаем обученную модель.
        Args:
            model_path (str): Путь до модели.
        """
        try:
            self.model = load(model_path)
        except Exception as e:
            print(f"Failed to load model: {e}")


    def predict(self, model_params: dict) -> float:
        """Предсказываем вероятность оттока.

        Args:
            model_params (dict): Параметры для модели.

        Returns:
            float — Предсказанная цена квартиры
        """
        return self.model.predict(pd.DataFrame([model_params]))

