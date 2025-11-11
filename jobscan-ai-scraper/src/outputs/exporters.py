thonimport json
import csv

class DataExporter:
    def __init__(self, output_format):
        self.output_format = output_format

    def export_data(self, job_data):
        if self.output_format == 'json':
            self.export_json(job_data)
        elif self.output_format == 'csv':
            self.export_csv(job_data)
        else:
            raise ValueError("Unsupported format")

    def export_json(self, job_data):
        with open('data/output.json', 'w') as f:
            json.dump(job_data, f, indent=4)

    def export_csv(self, job_data):
        keys = job_data[0].keys()
        with open('data/output.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(job_data)