import matplotlib.pyplot
import pandas
data={'time':[1,2,3,4,5,6,7,8,9,10],'points':[10,20,30,40,50,60,70,80,90,100]}
data_frame = pandas.DataFrame(data)

matplotlib.pyplot.title('scatter plot')
matplotlib.pyplot.xlabel('Время')
matplotlib.pyplot.ylabel('Баллы за экзамен')
matplotlib.pyplot.scatter(data['time'],data['points'])

# Показываем график
matplotlib.pyplot.show()