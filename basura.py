from bokeh.io import curdoc
from bokeh.models import Select, Column
import pandas as pd

df = pd.DataFrame()
df['France'] = ['Paris', 'Lione', 'Marseille']
df['Italy'] = ['Rome','Milan', 'Rimini']
df['Spain'] = ['Madrid', 'Barcelona', 'Bilbao']
df['Country']   = ['France', 'Italy', 'Spain']

select_country = Select(title="Country",  options=list(df['Country']), value = 'France')
select_city = Select(title = 'Cities', value = 'Paris', options = list(df['France']))

def update_layout(attr, old, new):
    country_selected = select_country.value
    select_city.options = list(df[country_selected].values)

select_country.on_change('value', update_layout)
select_city.on_change('value', update_layout)
layout = Column(select_country, select_city)
curdoc().add_root(layout)

