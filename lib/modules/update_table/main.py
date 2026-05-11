from ..sql import Databricks

class Update_Table(Databricks):



    def __init__(self, datadict: dict):

        self.batchid = datadict['batchid']
        self.wo_number = datadict['wo_number']
        self.bin_sequence = datadict['bin_sequence']
        self.bin_start = datadict['bin_start']
        self.processing_minutes = datadict['processing_minutes']
        self.operator = datadict['operator']
        self.sample_lot = datadict['sample_lot']
        self.delay_category = datadict['delay_category']
        self.delay_step = datadict['delay_step']
        self.resource = datadict['resource']
        self.delay_description = datadict['delay_description']
        self.delay_action = datadict['delay_action']
        self.equipment_id = datadict['equipment_id']

        with open('lib/modules/update_table/_query_update_table.sql', 'r') as file:
            query = file.read().format(
                batchid=self.batchid,
                wo_number=self.wo_number,
                bin_sequence=self.bin_sequence,
                bin_start=self.bin_start,
                processing_minutes=self.processing_minutes,
                operator=self.operator,
                sample_lot=self.sample_lot,
                delay_category=self.delay_category,
                delay_step=self.delay_step,
                resource=self.resource,
                delay_description=self.delay_description,
                delay_action=self.delay_action,
                equipment_id=self.equipment_id
            )
            print(query)
        super().__init__(query=query)

    def update(self):      
        return self.run_query()

