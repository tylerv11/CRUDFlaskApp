from flask import Flask, request, render_template
from lib.modules.all_data_read import Read_Current_Lots
from lib.modules.update_table import Update_Table


app = Flask(__name__)


@app.route('/batch_id/<batch_id>/bin_sequence/<bin_sequence>/wo_number/<wo_number>', methods=['GET'])
def get_record(batch_id, bin_sequence, wo_number):
    obj = Read_Current_Lots(batchid=batch_id, wo_number=wo_number, bin_sequence=bin_sequence).read_current_lots()   
    return render_template('add_delay.html', data=obj.to_dict(orient='records')[0])

@app.route('/add_delay', methods=['POST'])
def add_delay():
    data = request.form.to_dict()
    Update_Table(data).update()
    return render_template('update_submitted.html')


if __name__ == '__main__':
    app.run(debug=True)
