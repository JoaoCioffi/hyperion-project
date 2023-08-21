from invokeBuckets import Banks,\
                          Complaints,\
                          Employees

# Calling methods
def etlProcedures():

    # extract (loading raw dataframes)
    df_banks=Banks.loadBucketContent()
    df_compliants=Complaints.loadBucketContent()
    df_employees=Employees.loadBucketContent()

etlProcedures()