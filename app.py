from flask import Flask, Response, request, render_template
from faker import Faker
import csv
import io

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_data', methods=['GET'])
def generate_data():
    selected_fields = request.args.getlist('fields')
    num_records = int(request.args.get('num_records', 50))  # Get num_records from query, default to 50 if not specified

    # Create a Faker instance
    fake = Faker()

    # Generate data as per selected fields
    csv_data = io.StringIO()
    writer = csv.DictWriter(csv_data, fieldnames=selected_fields)
    writer.writeheader()
    for x in range(num_records):
        data = {}
        for field in selected_fields:
            if hasattr(fake, field.lower().replace('-', '_')):
                data[field] = getattr(fake, field.lower().replace('-', '_'))()
            else:
                data[field] = ""
        writer.writerow(data)

    # Create a response with CSV data
    response = Response(csv_data.getvalue(), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=fake_data.csv'
    return response

if __name__ == '__main__':
    app.run(debug=True)
