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


class ChronicKidneyModel(BaseModel):
    id: Optional[PydanticObjectId] = Field(None, alias="_id")
    aga: int
    bp: int | float
    sg: int | float
    al: int | float
    su: int | float
    rbc: int | float
    pc: int | float
    pcc: int | float
    ba: int | float
    bgr: int | float
    bu: int | float
    sc: int | float
    sod: int | float
    pot: int | float
    hemo: int | float
    pcv: int | float
    wc: int | float
    rc: int | float
    htn: int | float
    dm: int | float
    cad: int | float
    appet: int | float
    pe: int | float
    ane: int | float
    result: str


ENCODERS_BY_TYPE[PydanticObjectId] = str
