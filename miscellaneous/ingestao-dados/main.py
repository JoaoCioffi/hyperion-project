from serviceInfo import screenContent
from invokeBuckets import Banks,\
                          Complaints,\
                          Employees

# Calling methods
def etlProcedures():

    print('_'*35)
    print(screenContent())
    print('_'*35)

    # extract (loading raw dataframes)
    df_banks=Banks.loadBucketContent()
    df_compliants=Complaints.loadBucketContent()
    df_employees=Employees.loadBucketContent()

etlProcedures()