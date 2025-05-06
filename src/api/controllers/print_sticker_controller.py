import win32print
import win32ui


class PrintStickerController:
    def print_sticker(self, data):
        name = data.full_name
        gender = "נשים" if data.gender == "female" else "גברים"
        table_number = f"שולחן {data.table_number}"

        self._print_to_printer(name, gender, table_number)
        return {"status": "success", "message": "Sticker printed successfully"}

    def _print_to_printer(self, name, gender, table_number):
        printer_name = "LABEL"
        pdc = win32ui.CreateDC()
        pdc.CreatePrinterDC(printer_name)

        pdc.StartDoc("Participant Label")
        pdc.StartPage()

        # פונטים
        font_name = win32ui.CreateFont({
            "name": "Arial",
            "height": -50,
            "weight": 700,
        })

        font_details = win32ui.CreateFont({
            "name": "Arial",
            "height": -40,
            "weight": 400,
        })

        font_footer = win32ui.CreateFont({
            "name": "Arial",
            "height": -15,
            "weight": 300,
        })

        center_x = 200  # מתאים לרוחב של כ-400px — אמצע (תשני אם צריך)

        # שורה 1 – שם
        pdc.SelectObject(font_name)
        name_size = pdc.GetTextExtent(name)
        pdc.TextOut(center_x - name_size[0] // 2, 30, name)

        # שורה 2 – מספר שולחן
        pdc.SelectObject(font_details)
        table_text = f"{table_number}"
        table_size = pdc.GetTextExtent(table_text)
        pdc.TextOut(center_x - table_size[0] // 2, 90, table_text)

        # שורה 3 – מגדר
        gender_size = pdc.GetTextExtent(gender)
        pdc.TextOut(center_x - gender_size[0] // 2, 140, gender)

        # שורה 4 – חתימה תחתונה
        pdc.SelectObject(font_footer)
        footer_text = "נוצר על ידי אודיה מימון 0542943408"
        footer_size = pdc.GetTextExtent(footer_text)
        pdc.TextOut(center_x - footer_size[0] // 2, 200, footer_text)

        pdc.EndPage()
        pdc.EndDoc()
        pdc.DeleteDC()
