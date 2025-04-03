import pandas as pd
import matplotlib.pyplot as plt
from loggi import loging

class SunnyDAY:
    @loging
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath)


    @loging
    def preprocess_data(self):
       
        self.data['DATE'] = self.data['DATE'].astype(str)
        self.data = self.data[self.data['DATE'].str.startswith('2000')][['MONTH', 'BASEL_sunshine']].dropna()
        self.data['SunnyDay'] = self.data['BASEL_sunshine'] > 0
        self.data = self.data.groupby('MONTH')['SunnyDay'].sum().reset_index()

        
        month_names = {
            1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель',
            5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
            9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'
        }


        self.data['MONTH'] = self.data['MONTH'].map(month_names)


    @loging
    def paint(self):

        month_names_order = [
            'Январь', 'Февраль', 'Март', 'Апрель',
            'Май', 'Июнь', 'Июль', 'Август',
            'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        ]

        grouped_data = self.data.set_index('MONTH').reindex(month_names_order)

        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('blue')
        ax.set_facecolor('blue')
        bars = ax.barh(grouped_data.index, grouped_data['SunnyDay'], color='white', edgecolor='black', hatch='///', height=0.5)
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.set_title('Количество солнечных дней в 2000 году по месяцам', color='white')
        ax.set_xlabel('Солнечные дни', color='white')
        ax.set_ylabel('Месяц', color='white')

        for bar, value in zip(bars, grouped_data['SunnyDay']):
            ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value:.0f}', 
                    ha='left', va='center', color='white')

        plt.tight_layout()
        plt.show()