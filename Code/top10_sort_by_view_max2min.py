import pandas,numpy,pygal
def main():
    df = pandas.read_csv('BNK48_stat_15.12.2018_14.38.csv',encoding = "UTF-8",index_col=0)
    df = df.sort_values('viewCount',ascending=False)
    
    vid_name = numpy.array(df['title']).tolist()
    viewcount = numpy.array(df['viewCount']).tolist()
    
    chart = pygal.Bar()
    chart.title = 'Top 10 Video Sort By View Count maximum to minimum'
    for i in range(10):
        chart.add(vid_name[i], [{'value': viewcount[i], 'label':'{:.2f}%'.format((viewcount[i]*100)/sum(viewcount))}])
    chart.legend_at_bottom = True
    chart.render_to_file('Top 10 Sort by view count max to min.svg')
main()
