from pydantic import BaseModel


class chronic_kidney_disease(BaseModel):
    age: float
    bp: float
    sg: float
    al: float
    su: float
    rbc: float
    pc: float
    pcc: float
    ba: float
    bgr: float
    bu: float
    sc: float
    sod: float
    pot: float
    hemo: float
    pcv: int
    wc: int
    rc: float
    htn: float
    dm: int
    cad: int
    appet: float
    pe: float
    ane: float
