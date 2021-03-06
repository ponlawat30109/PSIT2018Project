import pandas,numpy,pygal
def main():
    df = pandas.read_csv('Data/BNK48_stat_15.12.2018_14.38.csv',encoding = "UTF-8",index_col=0)
    df = df.sort_values('viewCount',ascending=False)
    
    vid_name = numpy.array(df['title']).tolist()
    viewcount = numpy.array(df['viewCount']).tolist()
    
    chart = pygal.Bar()
    chart.title = 'Sort By View Count maximum to minimum'
    for i in range(len(viewcount)):
        chart.add(vid_name[i], [{'value': viewcount[i], 'label':'{:.2f}%'.format((viewcount[i]*100)/sum(viewcount))}])
    chart.legend_at_bottom = True
    chart.render_to_file('Data/Pic/All Data Sort By View Count Max to Min.svg')
main()
