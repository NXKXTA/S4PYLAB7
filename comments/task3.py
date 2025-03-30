from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtGui import QPainter, QColor
import csv


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Настройка главного окна
        self.setWindowTitle("Ураганы")
        self.setGeometry(100, 100, 1050, 600)

        # Создание виджета с вкладками
        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Чтение данных из CSV
        csv_data = self.read_csv()

        # Создание круговых диаграмм
        self.pie_2007(csv_data)  # Диаграмма за 2007 год
        self.pie_chart_by_year(csv_data)  # Диаграмма по годам

    def pie_2007(self, csv_data):
        """Круговая диаграмма ураганов за 2007 год по месяцам"""
        hurricanes = []
        valid_months = []

        # Сбор данных за 2007 год (индекс 2 в данных)
        for month, hurricanes_data in csv_data.items():
            value = hurricanes_data[2]  # Данные за 2007 год
            if value > 0:  # Только месяцы с ураганами
                hurricanes.append(value)
                valid_months.append(month)

        if hurricanes:
            # Нахождение месяца с максимальным количеством ураганов
            max_hurricanes = max(hurricanes)
            max_month = valid_months[hurricanes.index(max_hurricanes)]

            series = QPieSeries()  # Серия для круговой диаграммы
            total_hurricanes = sum(hurricanes)  # Общее количество ураганов

            # Добавление данных в диаграмму
            for month, count in zip(valid_months, hurricanes):
                slice_ = series.append(month, count)
                slice_.setLabelVisible(True)  # Показ подписей
                # Расчет процента и форматирование подписи
                percentage = (count / total_hurricanes) * 100
                slice_.setLabel(f"{month}: {percentage:.1f}%")

                # Выделение максимального месяца
                if month == max_month:
                    slice_.setBrush(QColor("red"))  # Красный цвет
                    slice_.setExploded(True)  # Выдвижение сегмента

            # Настройка и отображение диаграммы
            chart = QChart()
            chart.addSeries(series)
            chart.setTitle("Количество ураганов по месяцам за 2007 год")

            chart_view = QChartView(chart)
            chart_view.setRenderHint(QPainter.Antialiasing)

            # Создание вкладки для диаграммы
            chart_widget = QWidget()
            layout = QVBoxLayout(chart_widget)
            layout.addWidget(chart_view)
            self.tabs.addTab(chart_widget, "Ураганы 2007 года")

    def pie_chart_by_year(self, csv_data):
        """Круговая диаграмма ураганов по годам"""
        years = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
        hurricanes_by_year = {year: 0 for year in years}

        # Суммирование ураганов по годам
        for id_year, year in enumerate(years):
            for hurricane in csv_data.values():
                hurricanes_by_year[year] += hurricane[id_year]

        hurricanes = list(hurricanes_by_year.values())
        valid_years = list(hurricanes_by_year.keys())

        # Нахождение года с минимальным количеством ураганов
        min_hurricanes = min(hurricanes)
        min_years = [year for year, count in zip(valid_years, hurricanes)
                     if count == min_hurricanes]

        series = QPieSeries()
        total_hurricanes = sum(hurricanes)

        # Добавление данных в диаграмму
        for year, count in zip(valid_years, hurricanes):
            slice_ = series.append(str(year), count)
            slice_.setLabelVisible(True)
            percentage = (count / total_hurricanes) * 100
            slice_.setLabel(f"{year}: {percentage:.1f}%")

            # Выделение года с минимальным количеством ураганов
            if year in min_years:
                slice_.setBrush(QColor("red"))
                slice_.setExploded(True)

        # Настройка и отображение диаграммы
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Количество ураганов по годам")

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Создание вкладки для диаграммы
        chart_widget = QWidget()
        layout = QVBoxLayout(chart_widget)
        layout.addWidget(chart_view)
        self.tabs.addTab(chart_widget, "Ураганы по годам")

    def read_csv(self):
        """Чтение данных об ураганах из CSV-файла"""
        csv_data = {}
        with open("C:/Users/user/PycharmProjects/QTLabs/Lab7/hurricanes.csv", 'r', encoding="utf-8") as file:
            data = csv.reader(file, delimiter=',')
            next(data)  # Пропуск заголовка

            for row in data:
                if row:
                    month = row[0]
                    # Преобразование данных об ураганах в числа
                    hurricanes_per_month = list(map(int, row[2:]))
                    csv_data[month] = hurricanes_per_month
        return csv_data


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()

# Общие замечания
# Различия между PyQt6 и PySide6:
#
# Обе библиотеки предоставляют Python-привязки к Qt, но PyQt6 разрабатывается Riverbank Computing, а PySide6 - The Qt Company.
#
# API практически идентичны, но есть небольшие различия в именовании (например, PyQt6.QtCore.Qt vs PySide6.QtCore.Qt).
#
# Структура приложений:
#
# Все три примера следуют стандартной структуре Qt-приложений: создание QApplication, главного окна и запуск цикла событий.
#
# Используется наследование от QMainWindow для создания главного окна.
#
# Графики:
#
# В первом примере используются QSplineSeries для плавных кривых.
#
# Во втором - QScatterSeries для точечной и QBarSeries для столбчатой диаграммы.
#
# В третьем - QPieSeries для круговых диаграмм с возможностью выделения сегментов.
#
# Работа с данными:
#
# Данные читаются из CSV-файлов с помощью стандартного модуля csv.
#
# В примерах показаны разные подходы к обработке и визуализации данных.