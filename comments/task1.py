import sys
import math
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCharts import QChart, QChartView, QSplineSeries, QValueAxis
from PyQt6.QtCore import Qt


class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Настройка главного окна
        self.setWindowTitle("Графики синуса и косинуса")
        self.setGeometry(100, 100, 800, 600)  # Позиция и размер окна

        # Создание объекта графика
        chart = QChart()
        chart.setTitle("Графики синуса и косинуса")
        chart.legend().setVisible(True)  # Включение легенды
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)  # Позиция легенды

        # Создание серий данных для синуса и косинуса
        sin_series = QSplineSeries()  # Серия для синуса (гладкие кривые)
        sin_series.setName("sin(x)")

        cos_series = QSplineSeries()  # Серия для косинуса
        cos_series.setName("cos(x)")

        # Заполнение серий данными (31 точка от 0 до 6π)
        for i in range(31):
            x = i * math.pi / 5  # Вычисление x с шагом π/5
            sin_series.append(x, math.sin(x))  # Добавление точки синуса
            cos_series.append(x, math.cos(x))  # Добавление точки косинуса

        # Добавление серий на график
        chart.addSeries(sin_series)
        chart.addSeries(cos_series)

        # Настройка осей графика
        axis_x = QValueAxis()  # Ось X
        axis_x.setTitleText("X")  # Подпись оси
        axis_x.setRange(0, 6 * math.pi)  # Диапазон значений
        axis_x.setTickCount(7)  # Количество делений

        axis_y = QValueAxis()  # Ось Y
        axis_y.setTitleText("Y")
        axis_y.setRange(-1.2, 1.2)  # Диапазон для синуса/косинуса

        # Привязка осей к графику и сериям
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)  # Ось X внизу
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)  # Ось Y слева
        sin_series.attachAxis(axis_x)
        sin_series.attachAxis(axis_y)
        cos_series.attachAxis(axis_x)
        cos_series.attachAxis(axis_y)

        # Создание view для отображения графика
        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)  # Установка view как центрального виджета


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Создание приложения
    window = ChartWindow()  # Создание окна
    window.show()  # Показ окна
    sys.exit(app.exec())  # Запуск цикла обработки событий