update company_analytics.processing_view
SET processing_minutes = '{processing_minutes}',
bin_start = '{bin_start}',
operator = '{operator}',
delay_step = '{delay_step}',
delay_category = '{delay_category}',
resource = '{resource}',
delay_description = '{delay_description}',
action_taken = '{delay_action}',
equipment_id = '{equipment_id}'
WHERE batchid = '{batchid}'
and bin_sequence = '{bin_sequence}'
AND wo_number = '{wo_number}'