from dataclasses import dataclass, fields


@dataclass()
class Validate:
    def validate_fields(self):
        for field in fields(self):
            if field.name not in self.__dict__:
                raise AttributeError(
                    f"{field.name} is missing from the {type(self).__name__} instance.")
            if not getattr(self, field.name):
                raise ValueError(
                    f"{field.name} cannot be empty in the {type(self).__name__} instance.")
