



def builder(submission_list):
    
    top = []
    second = []
    scores = []
    scores2 = []
    compounds = []
    neg = []
    pos = []
    neu = []
    compounds2 = []
    neg2 = []
    pos2 = []
    neu2 = []
    
    df = pd.DataFrame()
    df2 = pd.DataFrame()
    
    count=0
    
    for link in submission_list:
        
        submission = reddit.submission(url='https://www.reddit.com'+link)
    
    
        time1 = datetime.now()

        submission.comments.replace_more(limit=None)
        for top_level_comment in submission.comments:
            top.append(top_level_comment.body)

        time2 = datetime.now()

        print "Scraping finished in:", (time2-time1), "at", time2
    
        time3 = datetime.now()
    
        submission.comments.replace_more(limit=None)
        for top_level_comment in submission.comments:
            for second_level_comment in top_level_comment.replies:
                second.append(second_level_comment.body)
    
        time4 = datetime.now()
    
        print "Scraping finished in:", (time2-time1), "at", time2
    
    
        Count +=1
        df = pd.DataFrame(top, columns=['Comments'])
        df['Index'] = Count
        index = list(np.array(df['Index']))
    
        
        df2 = pd.DataFrame(second, columns=['Comments2'])
        df2['Index2'] = Count
        index2 = list(np.array(df['Index2']))
    
        for sentence in df['Comments']:
            vs = analyzer.polarity_scores(sentence)
            scores.append(vs)
        
        for sentence in df['Comments2']:
            vs = analyzer.polarity_scores(sentence)
            scores2.append(vs)
        
        
        for line in scores:
            compounds.append(line['compound'])
            neg.append(line['neg'])
            pos.append(line['pos'])
            neu.append(line['neu'])
            
        for line in scores2:
            compounds2.append(line['compound'])
            neg2.append(line['neg'])
            pos2.append(line['pos'])
            neu2.append(line['neu'])
        
        my_dict ={'Comment': top, 'Index': index 'Compounds': compounds, 'Neg': neg, 'Pos': pos, 'Neu': neu}
        
        my_dict2 = {'Comment': top, 'Index': index 'Compounds': compounds, 'Neg': neg, 'Pos': pos, 'Neu': neu}
    
        pd.concat([df, pd.DataFrame(my_dict.values(), columns=df.columns)], ignore_index=True)
        pd.concat([df2, pd.DataFrame(my_dict2.values(), columns=df2.columns)], ignore_index=True)
    
        print "Finished compiling dataframe at:", datetime.now()
        return df, df2