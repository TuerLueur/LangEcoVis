import math

import pandas as pd

pd.options.mode.chained_assignment = None

ed_path = '../Data/edu/EdStatsData.csv'
ed_enhance_path = '../Data/enhanceData/EdStatsNew.csv'
edStatsData = pd.read_csv(ed_path, encoding='utf-8')

lang_path = '../Data/glottolog-glottolog-cldf-6aaf60b/cldf/languages.csv'
names_path = '../Data/glottolog-glottolog-cldf-6aaf60b/cldf/names.csv'
code_path = '../Data/countries_codes_and_coordinates.csv'
lang_enhance_data = '../Data/enhanceData/Lang.csv'
lang_data = pd.read_csv(lang_path, encoding='utf-8')
names_data = pd.read_csv(names_path)
code_data = pd.read_csv(code_path)

is3 = code_data.set_index(['Alpha-2 code'])['Alpha-3 code'].to_dict()


def edPrep():
    index_selected = ['GDP at market prices (current US$)',
                      'GDP per capita (current US$)',
                      'GNI (current US$)',
                      'GNI per capita, Atlas method (current US$)',
                      'Internet users (per 100 people)',
                      'Government expenditure on education as % of GDP (%)',
                      'Duration of compulsory education (years)',
                      'Adult literacy rate, population 15+ years, both sexes (%)',
                      'PIAAC: Mean Adult Literacy Proficiency. Total',
                      'PIAAC: Mean Adult Numeracy Proficiency. Total'
                      ]
    col_selected = ["Country Name", "Country Code", "Indicator Name", "Indicator Code",
                    "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009",
                    "2010", "2011", "2012", "2013", "2014"]
    data = pd.DataFrame(edStatsData)
    idx = data[data["Indicator Name"].isin(index_selected)]
    new = idx[col_selected]
    res = new.fillna("NaN")
    res.to_csv(ed_enhance_path)


def is2tois3(is2):
    if is2 == 'NA' or is2 == 'nan' or type(is2) == float:
        return 'NAM'
    else:
        if is2 not in is3.keys():
            return ""
        else:
            return str(is3[is2])


def code2name(id):
    row = lang_data.loc[lang_data['ID'] == id]
    if len(row) != 0:
        return row['Name'].values.tolist()[0]
    else:
        return ''


def langPrep():
    df = lang_data
    for index, row in df.iterrows():
        country_code_list = row['Countries']
        row['Family_ID'] = code2name(row['Family_ID'])
        row['Language_ID'] = code2name(row['Language_ID'])
        if type(country_code_list) == float and pd.isna(country_code_list):
            row['Countries'] = ''
        else:
            cc_l = ''
            for cc in country_code_list.split(';'):
                cc_l = cc_l + is2tois3(cc) + ';'
            print(cc_l[:-1])
            row['Countries'] = cc_l[:-1]
        df.iloc[index] = row
    print(df['Countries'])
    ndf = df.drop(['Glottocode', 'Closest_ISO369P3code'], axis=1)
    res = ndf.fillna('NaN')
    res.to_csv(lang_enhance_data)


if __name__ == '__main__':
    edPrep()
    # langPrep()
