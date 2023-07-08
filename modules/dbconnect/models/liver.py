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


class LiverModel(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    Age: int
    Gender_Female: int
    Gender_Male: int
    Total_Bilirubin: int | float
    Direct_Bilirubin: int | float
    Alkaline_Phosphotase: int | float
    Alamine_Aminotransferase: int | float
    Aspartate_Aminotransferase: int | float
    Total_Protiens: int | float
    Albumin: int | float
    Albumin_and_Globulin_Ratio: int | float
    result: str


ENCODERS_BY_TYPE[PydanticObjectId] = str
