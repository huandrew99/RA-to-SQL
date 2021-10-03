from rapt.rapt import Rapt

import json

if __name__ == '__main__':
    #load config file
    with open('config.json') as config_file:
        config = json.load(config_file)
    r = Rapt(**config)

    #load schema file
    f = open('schema.json')
    schema = json.load(f)

    #latex string
    latex_string = "LibrBran \leftarrow \s_{State='Indiana' } (LibraryBranch);"

    #use the to_sql function to translate latex
    sql_result = r.to_sql(latex_string, schema)

    #print the result
    print(sql_result)
