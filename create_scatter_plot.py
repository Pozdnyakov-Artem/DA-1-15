import matplotlib.pyplot as plt
import pandas

def create_scatter_plot(
        data:pandas.DataFrame,
        x_column:str,
        y_column:str,
        x_label:str=None,
        y_label:str=None,
        title:str='Scatter plot'
,):
    if not isinstance(data, pandas.DataFrame):
        raise TypeError('должен быть DataFrame')

    if x_column not in data.columns:
        raise ValueError(f'Колонка {x_column} отсутствует в данных')

    if y_column not in data.columns:
        raise ValueError(f'Колонка {y_column} отсутствует в данных')

    plt.title(title)

    plt.xlabel(x_label if x_label else x_column)
    plt.ylabel(y_label if y_label else y_column)

    plt.scatter(data[x_column], data[y_column])

    plt.show()


if __name__=='__main__':

    data = {'time': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'points': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}

    data_frame = pandas.DataFrame(data)

    create_scatter_plot(data_frame, 'points', 'time',title='Points scatter')