from capsule import SunnyDAY

def main():
    
    filepath = 'weather_prediction_dataset.csv'
    
    
    sunny_stats = SunnyDAY(filepath)
    sunny_stats.day_data()
    
   
    sunny_stats.paint()

if __name__ == "__main__":
    main()