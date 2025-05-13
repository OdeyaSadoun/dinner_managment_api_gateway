from fastapi import HTTPException, Response, UploadFile
import csv
from io import StringIO

from globals.enums.response_status import ResponseStatus
from globals.consts.consts import Consts
from globals.consts.const_strings import ConstStrings
from globals.consts.zmq_const_strings import ZMQConstStrings
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.person import Person
from models.data_classes.zmq_request import Request


class PersonController(IControllerManager):
    def __init__(self, zmq_client: IZMQClientManager) -> None:
        super().__init__()
        self._zmq_client = zmq_client

    def get_all_people(self):
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.get_all_people_operation
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
    
    def get_manual_people(self):
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.get_manual_people_operation
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
            
    def get_person_by_id(self, person_id: str):
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.get_person_by_id_operation,
                data={ConstStrings.person_id_key: person_id}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def import_people_from_csv(self, file: UploadFile):
        try:
            print("import_people_from_csv")
            contents = file.file.read().decode("cp1255")  # קידוד עברי של אקסל
            csv_reader = csv.DictReader(StringIO(contents))

            people = []
            for row in csv_reader:
                name = row.get("משפחה ופרטי", "").strip()
                location = row.get("מיקום", "").strip()
                try:
                    table_number = 0 if location == "בימת כבוד" else int(location)
                except ValueError:
                    table_number = -1                
                is_male = row.get("מגיע ג", "").strip().upper() == "TRUE"
                is_female = row.get("מגיע נ", "").strip().upper() == "TRUE"
                gender = "male" if is_male else "female" if is_female else None

                if gender is None:
                    continue

                is_reach = row.get("מגיעים תשפה", "").strip().upper() == "TRUE"

                people.append({
                    "name": name,
                    "table_number": table_number,
                    "gender": gender,
                    "add_manual": False,
                    "is_reach_the_dinner": is_reach,
                    "is_active": True
                })

            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.import_people_from_csv_operation,
                data={ConstStrings.people_key: people}
            )
            return self._zmq_client.send_request(request)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"שגיאה בייבוא: {str(e)}")

    def create_person(self, person: Person):
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.create_person_operation,
                data={
                    ConstStrings.person_key: person
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def update_person(self, person_id: str, person: Person):
        try:
            print("person", person)
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.update_person_operation,
                data={
                    ConstStrings.person_id_key: person_id,
                    ConstStrings.person_key: person
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def seat_person(self, person_id: str, table_id: str):
        try:
            print("seat")
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.seat_and_add_person_to_table_operation,
                data={ConstStrings.person_id_key: person_id,
                      ConstStrings.table_id_key: table_id}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
            
    def unseat_person(self, person_id: str, table_id: str):
        try:
            print("unseat person in api")
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.unseat_and_remove_person_from_table_operation,
                data={ConstStrings.person_id_key: person_id,
                      ConstStrings.table_id_key: table_id}
            )
            print("request", request)
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def delete_person(self, person_id: str, table_number: int, is_reach_the_dinner: bool):
        try:
            request = Request(
                resource=ZMQConstStrings.person_resource,
                operation=ZMQConstStrings.delete_person_operation,
                data={ConstStrings.person_id_key: person_id, 
                      ConstStrings.table_number_key: table_number, 
                      ConstStrings.is_reach_the_dinner_key: is_reach_the_dinner}
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
