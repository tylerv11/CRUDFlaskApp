select batchid, wo_number, sample_lot, bin_sequence, bin_start, processing_minutes, operator, delay_step, delay_category, resource, delay_description, action_taken, equipment_id from company_analytics.processing_view
WHERE batchid = '{batchid}'
AND wo_number = '{wo_number}'
and bin_sequence = '{bin_sequence}'