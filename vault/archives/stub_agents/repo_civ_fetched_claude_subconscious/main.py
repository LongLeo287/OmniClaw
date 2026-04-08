import json
from data_processing_module import process_subconscious_data, update_system_with_processed_data
from subconscious_analysis_algorithms import analyze_subconscious_data

def main():
    with open('subconscious_input.json', 'r') as f:
        subconscious_data = json.load(f)

    processed_data = process_subconscious_data(subconscious_data)
    analysis_result = analyze_subconscious_data(processed_data)

    update_system_with_processed_data(analysis_result)
