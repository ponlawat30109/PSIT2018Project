import pandas,numpy,pygal
def main():
    df = pandas.read_csv('Data/BNK48_stat_15.12.2018_14.38.csv',encoding = "UTF-8",index_col=0)
    df = df.sort_values('dislikeCount',ascending=False)
    
    vid_name = numpy.array(df['title']).tolist()
    dislikecount = numpy.array(df['dislikeCount']).tolist()
    
    chart = pygal.Bar()
    chart.title = 'Top 10 Video Sort By Dislike maximum to minimum'
    for i in range(10):
        chart.add(vid_name[i], [{'value': dislikecount[i], 'label':'{:.2f}%'.format((dislikecount[i]*100)/sum(dislikecount))}])
    chart.legend_at_bottom = True
    chart.render_to_file('Data/Pic/Top 10 Sort by dislike max to min.svg')
main()
