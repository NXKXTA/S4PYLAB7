import math
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCharts import QChart, QChartView, QSplineSeries, QValueAxis
from PySide6.QtCore import Qt


class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики синуса и косинуса")
        self.setGeometry(100, 100, 700, 600)

        # Создаем график
        chart = QChart()
        chart.setTitle("Графики синуса и косинуса")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        # Создаем серии данных
        sin_series = QSplineSeries()
        sin_series.setName("sin(x)")

        cos_series = QSplineSeries()
        cos_series.setName("cos(x)")

        # Заполняем данными (30 точек)
        for i in range(31):
            x = i * math.pi / 5
            sin_series.append(x, math.sin(x))
            cos_series.append(x, math.cos(x))

        # Добавляем серии на график
        chart.addSeries(sin_series)
        chart.addSeries(cos_series)

        # Настраиваем оси
        axis_x = QValueAxis()
        axis_x.setTitleText("X")
        axis_x.setRange(0, 6 * math.pi)
        axis_x.setTickCount(7)

        axis_y = QValueAxis()
        axis_y.setTitleText("Y")
        axis_y.setRange(-1.20, 1.20)

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        sin_series.attachAxis(axis_x)
        sin_series.attachAxis(axis_y)
        cos_series.attachAxis(axis_x)
        cos_series.attachAxis(axis_y)

        # Создаем view для графика
        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)
