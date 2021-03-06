import pandas,numpy,pygal
def main():
    df = pandas.read_csv('Data/BNK48_stat_15.12.2018_14.38.csv',encoding = "UTF-8",index_col=0)
    df = df.sort_values('dislikeCount',ascending=True)
    
    vid_name = numpy.array(df['title']).tolist()
    dislikecount = numpy.array(df['dislikeCount']).tolist()
    
    chart = pygal.Bar()
    chart.title = 'Sort By Dislike minimum to maximum'
    for i in range(len(dislikecount)):
        chart.add(vid_name[i], [{'value': dislikecount[i], 'label':'{:.2f}%'.format((dislikecount[i]*100)/sum(dislikecount))}])
    chart.legend_at_bottom = True
    chart.render_to_file('Data/Pic/All Data Sort By Dislike Min to Max.svg')
main()
