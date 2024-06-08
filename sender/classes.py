from openpyxl import load_workbook
from datetime import datetime

from sender.models import NicOnSurname


class MessageBuilder:

    def __init__(self, dst, str_number_data, green, red):
        """
        Собирает сообщение по данным из файла
        :param dst: имя файла
        :param str_number_data: номер строки с числами месяца
        :param green: rgb для зеленого цвета
        :param red: rgb для красного
        """
        # инициализируем объект книги из файла в dst
        wb = load_workbook(dst)
        # ищем в книге имя листа, в котором содержится текущий месяц
        sheet_name = self.get_sheet_name(self.get_current_name_month(), wb.sheetnames)
        self.ws = wb[sheet_name]
        self.str_number_data = str_number_data
        # цвета в rgb для поиска
        self.green = green
        self.red = red

    def get_one_message(self, color):
        ws_row = self.ws[self.str_number_data]
        # получаем букву столбца по сегодняшнему дню
        column_letter = self.get_cell_column_letter_by_day(ws_row)
        # получаем номер ячейки по цвету текста
        chell_number = self.get_cell_row_by_font_color(color, self.ws[column_letter])
        if chell_number:
            employer = 'B' + str(chell_number)
            employer = str(self.ws[employer].value).split()

            # Если ник есть в таблице, используем его
            nic = NicOnSurname.objects.filter(surname__istartswith=employer[0]).first()
            if nic:
                return f'{nic}, сегодня ты дежурный по '

            return f'{" ".join(employer[:2])}, сегодня ты дежурный по '

    def build(self):

        green_message = self.get_one_message(self.green)
        if green_message:
            green_message += '#ncc-call-tech'
        else:
            green_message = 'по #ncc-call-tech сегодня дежурных нет'

        red_message = self.get_one_message(self.red)
        if red_message:
            red_message += '#DomainsDuty'
        else:
            red_message = 'по #DomainsDuty сегодня дежурных нет'

        return green_message, red_message

    @staticmethod
    def get_sheet_name(keyword: str, sheets_names: list) -> str:
        for name in sheets_names:
            if keyword in name.lower():
                return name
        return 'нет такого листа'

    @staticmethod
    def get_cell_row_by_font_color(color: str, ws_col) -> int:
        for cell in ws_col:
            if cell.font.color.rgb == color:
                return cell.row

    @staticmethod
    def get_cell_column_letter_by_day(row) -> str:
        day = datetime.now().day
        for cell in row:
            if str(day) in str(cell.value):
                return cell.column_letter
        return 'столбец не найден'

    @staticmethod
    def get_current_name_month() -> str:
        month_list = [
            'январь', 'февраль', 'март',
            'апрель', 'май', 'июнь',
            'июль', 'август', 'сентябрь',
            'октябрь', 'ноябрь', 'декабрь']

        return month_list[datetime.now().month - 1]
