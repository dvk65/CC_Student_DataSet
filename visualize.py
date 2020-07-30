import numpy as np
from numpy import unique
import plotly.express as px


unique, freq = np.unique(list(data['Areas of interest']),return_counts=True)
np.asarray((unique,freq))

x=unique
y=freq
figa=px.bar(data,x,y)
figa.show()

data.loc[(data['Areas of interest']=='Data Science ') & (data['Programming Language Known other than Java (one major)']=='Python'),'decision'] = 'DataScience&Python'
data.loc[(data['Areas of interest']=='Data Science ') & (data['Programming Language Known other than Java (one major)']!='Python'),'decision'] = 'DataScience_No_Python'
data.loc[data['Areas of interest']!='Data Science ', 'decision'] = 'Nope'

courses, nums = np.unique(list(data['decision']),return_counts=True)
np.asarray((courses,nums))

x=courses[0:2]
y=nums[0:2]
figb=px.bar(data,x,y)
figb.show()

methods, num = np.unique(list(data['How Did You Hear About This Internship?']), return_counts=True)
np.asarray((methods, num))

x=methods
y=num
figc=px.bar(data,x,y)
figc.show()

data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['CGPA/ percentage']>=8.0),'graph_make'] = 'FourthY_CGPA_both'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['CGPA/ percentage']<=8.0),'graph_make'] = 'FourthY_Low_CGPA'
data.loc[data['Which-year are you studying in?']!='Fourth-year', 'graph_make'] = 'Nope'

platform, traffic = np.unique(list(data['graph_make']), return_counts=True)
np.asarray((platform, traffic))

x=platform[0:2]
y=traffic[0:2]
figd=px.bar(data,x,y)
figd.show()

data.loc[(data['Areas of interest']=='Digital Marketing ') & (data['Rate your written communication skills [1-10]']>=8.0) & (data['Rate your verbal communication skills [1-10]']>=8.0),'bar_graph'] = 'DM_communication&verbal'
data.loc[(data['Areas of interest']=='Digital Marketing ') & (data['Rate your written communication skills [1-10]']<=8.0) | (data['Rate your verbal communication skills [1-10]']<=8.0),'bar_graph'] = 'DM_not_communication_verbal'
data.loc[data['Areas of interest']!='Digital Marketing ', 'bar_graph'] = 'Nope'

digital_communication, verbal_written = np.unique(list(data['bar_graph']), return_counts=True)
np.asarray((digital_communication, verbal_written))

x=digital_communication[0:2]
y=verbal_written[0:2]
fige=px.bar(data,x,y)
fige.show()

data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Artificial Intelligence '),'scatter_graph'] = 'FirstY_AI'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Big Data '),'scatter_graph'] = 'FirstY_BD'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Blockchain '),'scatter_graph'] = 'FirstY_Block'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Cloud Computing '),'scatter_graph'] = 'FirstY_CC'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Cyber Security '),'scatter_graph'] = 'FirstY_Cyber'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Data Science '),'scatter_graph'] = 'FirstY_DS'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='DevOps '),'scatter_graph'] = 'FirstY_DevOps'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Digital Marketing '),'scatter_graph'] = 'FirstY_DigMarketing'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Information Security'),'scatter_graph'] = 'FirstY_InfoSecure'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='IoT '),'scatter_graph'] = 'FirstY_IoT'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Machine Learning'),'scatter_graph'] = 'FirstY_ML'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Mobility'),'scatter_graph'] = 'FirstY_Mobility'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Python '),'scatter_graph'] = 'FirstY_Python'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='QMS/Testing '),'scatter_graph'] = 'FirstY_QMS/Test'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='RPA '),'scatter_graph'] = 'FirstY_RPA'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Areas of interest']=='Web Development '),'scatter_graph'] = 'FirstY_WebDev'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Artificial Intelligence '),'scatter_graph'] = 'SecondY_AI'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Big Data '),'scatter_graph'] = 'SecondY_BD'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Blockchain '),'scatter_graph'] = 'SecondY_Block'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Cloud Computing '),'scatter_graph'] = 'SecondY_CC'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Cyber Security '),'scatter_graph'] = 'SecondY_Cyber'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Data Science '),'scatter_graph'] = 'SecondY_DS'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='DevOps '),'scatter_graph'] = 'SecondY_DevOps'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Digital Marketing '),'scatter_graph'] = 'SecondY_DigMarketing'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Information Security'),'scatter_graph'] = 'SecondY_InfoSecure'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='IoT '),'scatter_graph'] = 'SecondY_IoT'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Machine Learning'),'scatter_graph'] = 'SecondY_ML'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Mobility'),'scatter_graph'] = 'SecondY_Mobility'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Python '),'scatter_graph'] = 'SecondY_Python'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='QMS/Testing '),'scatter_graph'] = 'SecondY_QMS/Test'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='RPA '),'scatter_graph'] = 'SecondY_RPA'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Areas of interest']=='Web Development '),'scatter_graph'] = 'SecondY_WebDev'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Artificial Intelligence '),'scatter_graph'] = 'ThirdY_AI'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Big Data '),'scatter_graph'] = 'ThirdY_BD'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Blockchain '),'scatter_graph'] = 'ThirdY_Block'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Cloud Computing '),'scatter_graph'] = 'ThirdY_CC'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Cyber Security '),'scatter_graph'] = 'ThirdY_Cyber'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Data Science '),'scatter_graph'] = 'ThirdY_DS'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='DevOps '),'scatter_graph'] = 'ThirdY_DevOps'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Digital Marketing '),'scatter_graph'] = 'ThirdY_DigMarketing'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Information Security'),'scatter_graph'] = 'ThirdY_InfoSecure'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='IoT '),'scatter_graph'] = 'ThirdY_IoT'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Machine Learning'),'scatter_graph'] = 'ThirdY_ML'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Mobility'),'scatter_graph'] = 'ThirdY_Mobility'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Python '),'scatter_graph'] = 'ThirdY_Python'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='QMS/Testing '),'scatter_graph'] = 'ThirdY_QMS/Test'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='RPA '),'scatter_graph'] = 'ThirdY_RPA'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Areas of interest']=='Web Development '),'scatter_graph'] = 'ThirdY_WebDev'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Artificial Intelligence '),'scatter_graph'] = 'FourthY_AI'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Big Data '),'scatter_graph'] = 'FourthY_BD'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Blockchain '),'scatter_graph'] = 'FourthY_Block'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Cloud Computing '),'scatter_graph'] = 'FourthY_CC'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Cyber Security '),'scatter_graph'] = 'FourthY_Cyber'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Data Science '),'scatter_graph'] = 'FourthY_DS'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='DevOps '),'scatter_graph'] = 'FourthY_DevOps'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Digital Marketing '),'scatter_graph'] = 'FourthY_DigMarketing'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Information Security'),'scatter_graph'] = 'FourthY_InfoSecure'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='IoT '),'scatter_graph'] = 'FourthY_IoT'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Machine Learning'),'scatter_graph'] = 'FourthY_ML'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Mobility'),'scatter_graph'] = 'FourthY_Mobility'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Python '),'scatter_graph'] = 'FourthY_Python'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='QMS/Testing '),'scatter_graph'] = 'FourthY_QMS/Test'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='RPA '),'scatter_graph'] = 'FourthY_RPA'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Areas of interest']=='Web Development '),'scatter_graph'] = 'FourthY_WebDev'

year_interest, how_many = np.unique(list(data['scatter_graph']), return_counts=True)
np.asarray((year_interest, how_many))

figf = px.scatter(x=year_interest, y=how_many)
figf.show()

college, num =np.unique(list(data['College name']), return_counts=True)
np.asarray((college, num))

x=college
y=num
figag=px.bar(data,x,y)
figag.show()

city, students=np.unique(list(data['City']),return_counts=True)
np.asarray((city,students))

x=city
y=students
figbg=px.bar(data,x,y)
figbg.show()

data.groupby(['CGPA/ percentage', 'Label'], as_index=False).count()

x=data['CGPA/ percentage']
y=data['Label']
figh=px.bar(data,x,y)
figh.show()

data.groupby(['Areas of interest','Label'],as_index=False).count()

x=data['Areas of interest']
y=data['Label']
figi=px.bar(data,x,y)
figi.show()

data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Major/Area of Study']=='Computer Engineering') & (data['Label']=='eligible'), 'graph3']='first_eli_com'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Major/Area of Study']=='Computer Engineering') & (data['Label']=='ineligible'), 'graph3']='first_ineli_comp'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Major/Area of Study']=='Electrical Engineering') & (data['Label']=='eligible'), 'graph3']='first_eli_elec'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Major/Area of Study']=='Electrical Engineering') & (data['Label']=='ineligible'), 'graph3']='first_ineli_elec'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Major/Area of Study']=='Electronics and Telecommunication') & (data['Label']=='eligible'), 'graph3']='first_eli_elec&tele'
data.loc[(data['Which-year are you studying in?']=='First-year') & (data['Major/Area of Study']=='Electronics and Telecommunication') & (data['Label']=='ineligible'), 'graph3']='first_ineli_elec&tele'
data.loc[(data['Which-year are you studying in?']!='First-year'), 'graph3']='Nope'

courses, who =np.unique(list(data['graph3']),return_counts=True)
np.asarray((courses,who))

figaj = px.bar(data, x=courses[1:4], y=who[1:4])
figaj.show()

data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Major/Area of Study']=='Computer Engineering') & (data['Label']=='eligible'), 'graph2']='second_eli_com'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Major/Area of Study']=='Computer Engineering') & (data['Label']=='ineligible'), 'graph2']='second_ineli_comp'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Major/Area of Study']=='Electrical Engineering') & (data['Label']=='eligible'), 'graph2']='second_eli_elec'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Major/Area of Study']=='Electrical Engineering') & (data['Label']=='ineligible'), 'graph2']='second_ineli_elec'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Major/Area of Study']=='Electronics and Telecommunication') & (data['Label']=='eligible'), 'graph2']='second_eli_elec&tele'
data.loc[(data['Which-year are you studying in?']=='Second-year') & (data['Major/Area of Study']=='Electronics and Telecommunication') & (data['Label']=='ineligible'), 'graph2']='second_ineli_elec&tele'
data.loc[(data['Which-year are you studying in?']!='Second-year'), 'graph2']='Nope'

courses, who = np.unique(list(data['graph2']),return_counts=True)
np.asarray((courses,who))

x=courses[1:7]
y=who[1:7]
figbj=px.bar(data,x,y)
figbj.show()

data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Major/Area of Study']=='Computer Engineering') & (data['Label']=='eligible'), 'graph1']='third_eli_com'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Major/Area of Study']=='Computer Engineering') & (data['Label']=='ineligible'), 'graph1']='third_ineli_comp'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Major/Area of Study']=='Electrical Engineering') & (data['Label']=='eligible'), 'graph1']='third_eli_elec'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Major/Area of Study']=='Electrical Engineering') & (data['Label']=='ineligible'), 'graph1']='third_ineli_elec'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Major/Area of Study']=='Electronics and Telecommunication') & (data['Label']=='eligible'), 'graph1']='third_eli_elec&tele'
data.loc[(data['Which-year are you studying in?']=='Third-year') & (data['Major/Area of Study']=='Electronics and Telecommunication') & (data['Label']=='ineligible'), 'graph1']='third_ineli_elec&tele'
data.loc[(data['Which-year are you studying in?']!='Third-year'), 'graph1']='Nope'

courses, who = np.unique(list(data['graph1']),return_counts=True)
np.asarray((courses,who))

x=courses[1:7]
y=who[1:7]
figcj=px.bar(data,x,y)
figcj.show()

data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Major/Area of Study']=='Computer Engineering') & (data['Label']=='eligible'), 'graph4']='Fourth_eli_com'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Major/Area of Study']=='Computer Engineering') & (data['Label']=='ineligible'), 'graph4']='Fourth_ineli_comp'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Major/Area of Study']=='Electrical Engineering') & (data['Label']=='eligible'), 'graph4']='Fourth_eli_elec'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Major/Area of Study']=='Electrical Engineering') & (data['Label']=='ineligible'), 'graph4']='Fourth_ineli_elec'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Major/Area of Study']=='Electronics and Telecommunication') & (data['Label']=='eligible'), 'graph4']='Fourth_eli_elec&tele'
data.loc[(data['Which-year are you studying in?']=='Fourth-year') & (data['Major/Area of Study']=='Electronics and Telecommunication') & (data['Label']=='ineligible'), 'graph4']='Fourth_ineli_elec&tele'
data.loc[(data['Which-year are you studying in?']!='Fourth-year'), 'graph4']='Nope'

courses, who = np.unique(list(data['graph1']),return_counts=True)
np.asarray((courses,who))

x=courses[1:7]
y=who[1:7]
figdj=px.bar(data,x,y)
figdj.show()

data.drop(['graph1','graph2','graph3','graph4'], axis=1, inplace=True)

with open('p_graph.html', 'a') as f:
    f.write(figa.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figb.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figc.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figd.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(fige.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figf.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figag.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figbg.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figh.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figi.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figaj.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figbj.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figcj.to_html(full_html=False, include_plotlyjs='cdn'))
    f.write(figdj.to_html(full_html=False, include_plotlyjs='cdn'))

from xhtml2pdf import pisa


def convert_html_to_pdf(p_graph, visualization_output):
    result_file = open(visualization_output, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
        p_graph,  # the HTML to convert
        dest=result_file)  # file handle to recieve result

    # close output file
    result_file.close()  # close output file

    # return True on success and False on errors
    return pisa_status.err

convert_html_to_pdf(p_graph, 'visualization_output.pdf')