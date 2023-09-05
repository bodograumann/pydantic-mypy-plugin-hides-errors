from pydantic import BaseModel


class ModelA(BaseModel):
    field: int


class ModelB(BaseModel):
    field: dict[str, str]


def type_violation(obj_a: ModelA) -> ModelB:
    return ModelB(field=obj_a.field)
