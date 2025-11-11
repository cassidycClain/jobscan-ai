thonimport os
import json
from extractors.google_parser import GoogleParser
from outputs.exporters import DataExporter

class JobScanAI:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        self.google_parser = GoogleParser(self.config['search_sites'])
        self.data_exporter = DataExporter(self.config['output_format'])

    def run(self):
        job_data = self.google_parser.scrape_jobs()
        self.data_exporter.export_data(job_data)

if __name__ == "__main__":
    scraper = JobScanAI('src/config/settings.example.json')
    scraper.run()