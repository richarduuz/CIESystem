import pandas as pd
from datetime import datetime

def extractQuo(df):
    response = {"status": ""}
    try:
        row, colume = getSize(df)
        keys = getKeys(df)
        result = []
        for i in range(row):
            doc = {}
            for j in keys:
                j = j.strip()
                if df[j].dtype == "datetime64[ns]":
                    if j == "询价日期":
                        ts = datetime.today()
                    else:
                        ts = pd.to_datetime(str(df[j].values[i]))
                    d = ts.strftime('%Y.%m.%d')
                    doc[j] = d
                elif j == "接单率":
                    doc[j] = "{:.0%}".format(df[j].values[i])
                else:
                    doc[j] = str(df[j].values[i])
            result.append(doc)
        response['status'] = "Okay"
        response['body'] = result
    except Exception as e:
        response['status'] = "Extract Error"
        response['message'] = str(e)
    finally:
        return response










#------------------Self Functions------------------
def getSize(df):
    return (df.shape[0], df.shape[1])

def getKeys(df):
    keys = []
    for i in df:
        keys.append(i)
    return keys