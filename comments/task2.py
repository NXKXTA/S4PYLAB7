from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget
from PySide6.QtCharts import QChart, QChartView, QScatterSeries, QBarSeries, QBarSet
from PySide6.QtGui import QPainter, Qt
import csv


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # Настройка главного окна
        self.setWindowTitle("Деревья")
        self.setGeometry(100, 100, 900, 600)

        # Чтение данных из CSV
        csv_data = self.read_csv()  # {1: {'Girth': 8.3, 'Height': 70.0, 'Volume': 10.3},...}

        # Создание виджета с вкладками
        tab_widget = QTabWidget()

        # Первая вкладка - точечная диаграмма
        scatter_tab = QWidget()
        scatter_layout = QVBoxLayout()

        # Создание точечной диаграммы
        scatter_chart = self.scatter_chart(csv_data)
        scatter_chart_view = QChartView(scatter_chart)
        scatter_chart_view.setRenderHint(QPainter.Antialiasing)  # Сглаживание

        scatter_layout.addWidget(scatter_chart_view)
        scatter_tab.setLayout(scatter_layout)

        # Вторая вкладка - столбчатая диаграмма
        bar_tab = QWidget()
        bar_layout = QVBoxLayout()

        # Создание столбчатой диаграммы
        bar_chart = self.bar_chart(csv_data)
        bar_chart_view = QChartView(bar_chart)
        bar_chart_view.setRenderHint(QPainter.Antialiasing)

        bar_layout.addWidget(bar_chart_view)
        bar_tab.setLayout(bar_layout)

        # Добавление вкладок
        tab_widget.addTab(scatter_tab, "Точечная диаграмма")
        tab_widget.addTab(bar_tab, "Столбчатая диаграмма")
        self.setCentralWidget(tab_widget)

    def scatter_chart(self, csv_data):
        """Создание точечной диаграммы зависимости высоты от обхвата"""
        chart = QChart()
        scatter_series = QScatterSeries()  # Серия точек
        scatter_series.setName("Точечная диаграмма")
        scatter_series.setMarkerSize(10)  # Размер точек

        # Заполнение данными
        for tree_id, tree_data in csv_data.items():
            girth = tree_data['Girth']  # Обхват (X)
            height = tree_data['Height']  # Высота (Y)
            scatter_series.append(girth, height)

        chart.addSeries(scatter_series)
        chart.createDefaultAxes()  # Автоматическое создание осей
        chart.axes(Qt.Horizontal)[0].setTitleText("Girth")  # Подпись оси X
        chart.axes(Qt.Vertical)[0].setTitleText("Height")  # Подпись оси Y

        return chart

    def bar_chart(self, csv_data):
        """Создание столбчатой диаграммы объемов деревьев"""
        chart = QChart()
        bar_series = QBarSeries()  # Серия столбцов

        bar_set = QBarSet("Столбчатая диаграмма")  # Набор данных
        for tree_data in csv_data.values():
            bar_set.append(tree_data['Volume'])  # Добавление объема

        bar_series.append(bar_set)
        chart.addSeries(bar_series)
        chart.createDefaultAxes()
        chart.axes(Qt.Horizontal)[0].setTitleText("Tree ID")  # ID дерева по X
        chart.axes(Qt.Vertical)[0].setTitleText("Volume")  # Объем по Y

        return chart

    def read_csv(self):
        """Чтение данных из CSV-файла"""
        csv_data = {}
        with open("C:/Users/user/PycharmProjects/QTLabs/Lab7/trees.csv", 'r', encoding="utf-8") as file:
            data = csv.reader(file, delimiter=',')
            next(data)  # Пропуск заголовка

            for row in data:
                if row:
                    tree_id = int(row[0])
                    csv_data[tree_id] = {
                        'Girth': float(row[1]),  # Обхват
                        'Height': float(row[2]),  # Высота
                        'Volume': float(row[3])  # Объем
                    }
        return csv_data


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()