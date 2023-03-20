import pandas as pd

ed_path = '../Data/edu/EdStatsData.csv'
ed_enhance_path = '../Data/enhanceData/EdStatsNew.csv'
edStatsData = pd.read_csv(ed_path, encoding='utf-8')

index_selected = ['GDP at market prices (current US$)',
                  'GDP per capita (current US$)',
                  'GNI (current US$)',
                  'Population, total',
                  'Internet users (per 100 people)',
                  'Government expenditure on education as % of GDP (%)',
                  'Duration of compulsory education (years)',
                  'Adult literacy rate, population 15+ years, both sexes (%)',
                  ]
col_selected = ["Country Name", "Country Code", "Indicator Name", "Indicator Code",
                "1970","1971","1972","1973","1974","1975","1976","1977","1978","1979",
                "1980","1981","1982","1983","1984","1985","1986","1987","1988","1989",
                "1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
                "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
                "2010","2011","2012","2013","2014","2015","2016","2017",
                "2020","2025"]

if __name__ == '__main__':
    data = pd.DataFrame(edStatsData)
    idx = data[data["Indicator Name"].isin(index_selected)]
    new = idx[col_selected]
    res = new.fillna("NaN")
    res.to_csv(ed_enhance_path)
    # data = data.
    # data = data[data["Indicator Name"].isin(index_selected)]
    # print(data.shape())