#build three tear looks 2010-2012

df_2010_2012 = df_new[[i for i in df_new.columns if ('2010' in i) | ('2011' in i)|('2012' in i)]]

df_2010_2012 = df_2010_2012.join(df_new['W_standings_2013'])

df_2010_2012.index = [i + ' (2010-2012)' for i in df_2010_2012.index]

df_2010_2012.columns = df_2010_2012.columns.map(lambda x: x.replace('2010','py_2').replace('2011','py_1').replace('2012','py').replace('2013','next'))

#build three tear looks 2011-2013
df_2011_2013 = df_new[[i for i in df_new.columns if ('2011' in i) | ('2012' in i)|('2013' in i)]]

df_2011_2013 = df_2011_2013.join(df_new['W_standings_2014'])

df_2011_2013.index = [i + ' (2011-2013)' for i in df_2011_2013.index]

df_2011_2013.columns = df_2011_2013.columns.map(lambda x: x.replace('2011','py_2').replace('2012','py_1').replace('2013','py').replace('2014','next'))

#build three year looks 2012-2014
df_2012_2014 = df_new[[i for i in df_new.columns if ('2012' in i) | ('2013' in i)|('2014' in i)]]

df_2012_2014 = df_2012_2014.join(df_new['W_standings_2015'])

df_2012_2014.index = [i + ' (2012-2014)' for i in df_2012_2014.index]

df_2012_2014.columns = df_2012_2014.columns.map(lambda x: x.replace('2012','py_2').replace('2013','py_1').replace('2014','py').replace('2015','next'))

#build three year looks 2013-2015

df_2013_2015 = df_new[[i for i in df_new.columns if ('2013' in i) | ('2014' in i)|('2015' in i)]]

df_2013_2015 = df_2013_2015.join(df_new['W_standings_2016'])

df_2013_2015.index = [i + ' (2013-2015)' for i in df_2013_2015.index]

df_2013_2015.columns = df_2013_2015.columns.map(lambda x: x.replace('2013','py_2').replace('2014','py_1').replace('2015','py').replace('2016','next'))

df_three_year = pd.concat([df_2010_2012,df_2011_2013,df_2012_2014])

print df_three_year.shape
df_three_year.head()
