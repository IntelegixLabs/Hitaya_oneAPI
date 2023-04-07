from pydantic import BaseModel


class heart_disease(BaseModel):
    Age: int
    Gender_Female: int
    Gender_Male: int
    Total_Bilirubin: float
    Direct_Bilirubin: float
    Alkaline_Phosphotase: int
    Alamine_Aminotransferase: int
    Aspartate_Aminotransferase: int
    Total_Protiens: float
    Albumin: float
    Albumin_and_Globulin_Ratio: float
