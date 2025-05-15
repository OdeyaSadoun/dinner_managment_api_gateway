from fastapi import HTTPException

from globals.enums.response_status import ResponseStatus
from globals.consts.zmq_const_strings import ZMQConstStrings
from globals.consts.consts import Consts
from globals.consts.const_strings import ConstStrings
from infrastructures.interfaces.icontroller_manager import IControllerManager
from infrastructures.interfaces.izmq_client_manager import IZMQClientManager
from models.data_classes.person import Person
from models.data_classes.table import Table
from models.data_classes.zmq_request import Request

from fastapi import UploadFile, HTTPException
import csv
from io import StringIO

class TableController(IControllerManager):
    def __init__(self, zmq_client: IZMQClientManager) -> None:
        self._zmq_client = zmq_client
        
    def get_all_tables(self):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.get_all_tables_operation
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def get_table_by_id(self, table_id: str):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.get_table_by_id_operation,
                data={
                    ConstStrings.table_id_key: table_id
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def create_table(self, table: Table):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.create_table_operation,
                data={
                    ConstStrings.table_key: table
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def import_tables_from_csv(self, file: UploadFile):
        try:
            contents = file.file.read().decode("cp1255")  # קידוד עברי
            csv_reader = csv.DictReader(StringIO(contents))

            tables = []
            for idx, row in enumerate(csv_reader):
                try:
                    table_number = int(row.get("מספר שולחן", "").strip())
                    raw_type = row.get("סוג שולחן", "").strip()
                    chairs = int(row.get("כמות כסאות", "").strip())
                except Exception:
                    continue  # דלג על שורה לא תקינה

                # 🟡 קביעה חכמה של מגדר
                if any(term in raw_type for term in ["בימת כבוד", "רזרבה", "VIP", "גברים"]):
                    gender = "male"
                else:
                    gender = "female"

                # ברירות מחדל
                shape = "square"

                # מיפוי לפי סוג שולחן
                if "בימת כבוד" in raw_type:
                    shape = "bima"
                elif "רזרבה" in raw_type:
                    shape = "reserva"
                elif "VIP" in raw_type:
                    shape = "vip"
                elif "אבירים" in raw_type:
                    shape = "rectangle"

                tables.append({
                    "table_number": table_number,
                    "chairs": chairs,
                    "shape": shape,
                    "gender": gender,
                    "position": {"x": (idx % 20) * 130, "y": (idx // 20) * 120},
                    "people_list": [],
                    "is_active": True
                })
            print(f"✅ נקלטו {len(tables)} שולחנות מתוך הקובץ")
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.import_tables_from_csv_operation,
                data={ConstStrings.tables_key: tables}
            )
            return self._zmq_client.send_request(request)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"שגיאה בייבוא השולחנות: {str(e)}")

    def update_table_position(self, table_id: str, position: dict):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.update_table_position_operation,
                data={
                    ConstStrings.table_id_key: table_id,
                    ConstStrings.position_key: position
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
            
    def update_table(self, table_id: str, table: dict):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.update_table_operation,
                data={
                    ConstStrings.table_id_key: table_id,
                    ConstStrings.table_key: table
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))

    def delete_table(self, table_id: str):
        try:
            request = Request(
                resource=ZMQConstStrings.table_resource,
                operation=ZMQConstStrings.delete_table_operation,
                data={
                    ConstStrings.table_id_key: table_id
                }
            )
            return self._zmq_client.send_request(request)
        except Exception as e:
            raise HTTPException(
                status_code=Consts.error_status_code, detail=str(e))
