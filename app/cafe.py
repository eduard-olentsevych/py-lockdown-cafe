import datetime

from typing import Union

from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError
)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> Union[
        str, NotVaccinatedError,
        OutdatedVaccineError, NotWearingMaskError
    ]:
        if "vaccine" not in visitor:
            raise NotVaccinatedError("The visitor is not vaccinated!")
        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError(
                "The visitor's vaccine has been expired!"
            )
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError("The visitor does not wear a mask!")
        return f"Welcome to {self.name}"