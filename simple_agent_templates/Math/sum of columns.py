#no_permutation

class cls_agent_{id}:
    import warnings
    warnings.filterwarnings("ignore")
    
    import pandas as pd

    col_definition1 = "{random_field_numeric}"
    col1 = col_definition1.split("|")[0]
    file1 = col_definition1.split("|")[1]
    col_definition2 = "{random_field_numeric}"
    col2 = col_definition2.split("|")[0]
    file2 = col_definition2.split("|")[1]

    result_id = {id}
    field_prefix = "field_"
    output_column = field_prefix + str(result_id)
    output_filename = output_column + ".csv"

    def run_on(self, df_run):
        df_run[self.output_column] = df_run[self.col1] + df_run[self.col2]

    def run(self, mode):
        print ("enter run mode " + str(mode))
        self.df = self.pd.read_csv(workdir+self.file1)[[self.col1]]
        self.df = self.df.merge(self.pd.read_csv(workdir+self.file2)[[self.col2]], left_index=True, right_index=True)
        
        self.run_on(self.df)
        
        self.df[[self.output_column]].to_csv(workdir+self.output_filename)
        print (self.col1 + "+" + self.col2)
        print ("#add_field:"+self.output_column+",N,"+self.output_filename+","+str(len(self.df)))
    
    def apply(self, df_add):
        self.run_on(df_add)

agent_{id} = cls_agent_{id}()
