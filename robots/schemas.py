from pydantic import BaseModel, field_validator
from datetime import datetime


class RobotInput(BaseModel):
    model: str
    version: str
    created: datetime

    @field_validator('model', 'version')
    def validate_length(cls, value, info):
        """
        Валидатор проверяет, что длина 'model' и 'version' соответствует требованиям.
        """
        if info.field_name == 'model' and len(value) != 2:
            raise ValueError("Model must be exactly 2 characters long.")
        if info.field_name == 'version' and len(value) != 2:
            raise ValueError("Version must be exactly 2 characters long.")
        return value

    @field_validator('created', mode='before')
    def validate_created(cls, value):
        """
        Валидатор проверяет, что 'created' является корректной датой.
        """
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValueError("Invalid datetime format. Use 'YYYY-MM-DD HH:MM:SS'.")
        return value
