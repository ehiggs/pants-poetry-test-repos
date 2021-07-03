from pydantic.dataclasses import dataclass

@dataclass
class Greeting:
    greet: str
    name: str
