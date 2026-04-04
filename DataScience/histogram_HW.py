import plotly.express as px
import numpy as np

marks = np.random.randint(0, 101, 50)

ranges = []
for m in marks:
    if m <= 30:   ranges.append('0-30')
    elif m <= 50: ranges.append('31-50')
    elif m <= 70: ranges.append('51-70')
    elif m <= 90: ranges.append('71-90')
    else:         ranges.append('91-100')

graph = px.histogram(x=ranges, title='Student Marks Distribution')
graph.write_html('Student_Marks.html', auto_open=True)

above_75 = np.sum(marks>75)
print(f'The number of students scoring above 75 is {above_75}') 
