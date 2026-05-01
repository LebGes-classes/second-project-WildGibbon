
import json
from typing import Any


class FileManager:
    """
    Класс для управления файлами.
    """
    def save_json(self, json_data: Any, file_path: str) -> None:
        """
        Сохраняет данные в формате JSON в файл.

        Args:
            json_data: Данные для сохранения в формате JSON.
            file_path (str): Путь к файлу для сохранения.
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, ensure_ascii=False, indent=4)
