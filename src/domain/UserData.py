from dataclasses import dataclass, fields


@dataclass()
class UserData:
    user_id: str
    name: str
    start_date: str
    start_balance: float
    api_key: str
    api_secret: str
    max_risk_percent: int

    def __post_init__(self):
        for field in fields(self):
            if getattr(self, field.name) is None:
                raise ValueError(f"{field.name} must have a value.")

    def validate_fields(self):
        for field in fields(self):
            if field.name not in self.__dict__:
                raise AttributeError(
                    f"{field.name} is missing from the {type(self).__name__} instance.")
            if not getattr(self, field.name):
                raise ValueError(
                    f"{field.name} cannot be empty in the {type(self).__name__} instance.")
