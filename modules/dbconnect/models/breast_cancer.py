from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field
from pydantic.json import ENCODERS_BY_TYPE


class PydanticObjectId(ObjectId):
    """
    ObjectId field. Compatible with Pydantic.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        return PydanticObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema: dict):
        field_schema.update(
            type="string",
            examples=["5eb7cf5a86d9755df3a6c593", "5eb7cfb05e32e07750a1756a"],
        )


class BreastCancerModel(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: int
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float
    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float
    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float
    result: str


ENCODERS_BY_TYPE[PydanticObjectId] = str
