import pandas,numpy,pygal
def main():
    df = pandas.read_csv('BNK48_stat_15.12.2018_14.38.csv',encoding = "UTF-8",index_col=0)
    df = df.sort_values('likeCount',ascending=True)
    
    vid_name = numpy.array(df['title']).tolist()
    likecount = numpy.array(df['likeCount']).tolist()
    
    chart = pygal.Bar()
    chart.title = 'Sort By Like minimum to maximum'
    for i in range(len(likecount)):
        chart.add(vid_name[i], [{'value': likecount[i], 'label':'{:.2f}%'.format((likecount[i]*100)/sum(likecount))}])
    chart.legend_at_bottom = True
    chart.render_to_file('All Data Sort By Llike Min to Max.svg')
main()
