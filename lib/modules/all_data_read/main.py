from ..sql import Databricks

class Read_Current_Lots(Databricks):

    def __init__(self, batchid, wo_number, bin_sequence):
        with open('lib/modules/all_data_read/_query_delay_info.sql', 'r') as file:
            query = file.read().format(
                batchid=batchid,
                wo_number=wo_number,
                bin_sequence=bin_sequence
            )
            print(query)
        super().__init__(query=query)
        self.batchid = batchid
        self.wo_number = wo_number
        self.bin_sequence = bin_sequence

    def read_current_lots(self):      
            return self.run_query()

# Read_Current_Lots().read_current_lots()