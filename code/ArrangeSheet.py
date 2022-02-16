from contextlib import nullcontext
import pandas as pd
import re

class ArrangeSheet:
    # construtor da classe
    def __init__(self, filepath: str, indexCol: int, headerRow: int, colRange: int, nrows: int, delimiter) -> None:
        self.__filepath = filepath
        self.indexCol = indexCol
        self.headerRow = headerRow
        self.colRange = colRange
        self.nrows = nrows
        self.dataFrame = ''
        self.delimiter = delimiter

    @property
    def filepath(self):
        return self.__filepath


    def setDataFrame(self):
        if self.filepath.endswith('.csv'):
            self.dataFrame = pd.read_csv(self.filepath, header=self.headerRow, index_col=self.indexCol, delimiter=self.delimiter, nrows=self.nrows)   
        elif self.filepath.endswith('.xls') or self.filepath.endswith('.xlsx'):
            self.dataFrame = pd.read_excel(self.filepath, header=self.headerRow, index_col=self.indexCol, nrows=self.nrows)
        else:
            raise ValueError('O arquivo não apresenta o formato correto!')
    

    def getDataset(self, avoidColumns):
        listDataset = []
        
        for index, row in self.dataFrame.iterrows():
            cols = row.to_list()
            condition = (x for x in range(len(cols)) if x not in avoidColumns)
            for x in condition:
                y = re.findall('[0-9]+', str(self.dataFrame.columns[x]))
                listDataset.append([index, y[0], cols[x]])
        
        return listDataset


    def arrToDataFrame(self, list, labels):
        return pd.DataFrame(list, columns=labels)

'''
======================================================================================================================================================
'''
