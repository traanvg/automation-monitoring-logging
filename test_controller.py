import time
import csv

def check_device_log():
    try:
        with open("device_log.txt", "r") as f:
            lines = f.readlines()[-5:]  # check last 5 logs
            issues = []
            for line in lines:
                if "Temp" in line:
                    parts = line.split(",")
                    temp = float(parts[1].split(":")[1].strip().replace("°C", ""))
                    voltage = float(parts[2].split(":")[1].strip().replace("V", ""))
                    if temp > 70 or voltage < 3.3:
                        issues.append((line.strip(), "⚠️ Issue detected"))
            return issues
    except FileNotFoundError:
        return [("No log file found", "❌")]

def log_results(issues):
    with open("test_results.csv", "a") as f:
        writer = csv.writer(f)
        for issue in issues:
            writer.writerow([time.ctime(), issue[0], issue[1]])

if __name__ == "__main__":
    issues = check_device_log()
    if issues:
        print("⚠️ Issues found in device log:")
        for issue in issues:
            print(issue)
    else:
        print("✅ All good")
    log_results(issues)
