def extractQuo(df):
    response = {"status": ""}
    try:
        row, colume = getSize(df)
        keys = getKeys(df)
        result = []
        for i in range(row):
            doc = {}
            for j in keys:
                doc[j] = str(df[j].values[i])
            result.append(doc)
        response['status'] = "Okay"
        response['body'] = result
        return response
    except:
        response['status'] = "Extract Error"
        return response












#------------------Self Functions------------------
def getSize(df):
    return (df.shape[0], df.shape[1])

def getKeys(df):
    keys = []
    for i in df:
        keys.append(i)
    return keys