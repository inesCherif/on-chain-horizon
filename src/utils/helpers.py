from datetime import datetime
import json

def export_analysis(competitor_data):
    export_data = {
        'analysis_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'competitors': competitor_data
    }
    return json.dumps(export_data, indent=2)
