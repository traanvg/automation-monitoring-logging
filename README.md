# ⚡ Automation Monitoring & Logging System  

## 📌 Project Overview  
This project simulates **device health monitoring** by generating temperature and voltage sensor readings in real time.  
The system logs data to CSV, detects anomalies (overheating, undervoltage), and visualizes issue trends.  

---

## 🛠 Tools & Libraries  
- Python: Pandas, Matplotlib  
- Data Storage: CSV  
- Environment: Jupyter / VS Code / CLI  

---

## 📂 Files  
- `device_sim.py` → generates simulated temperature/voltage readings  
- `test_controller.py` → controls tests, applies thresholds for anomaly detection  
- `plot_results.py` → visualizes trends with Matplotlib  
- `run_test.sh` → shell script to automate test execution  
- `device_log.txt` → sample log of simulated data  

---

## 🔧 Features  
- **Simulated Data Generation** for device monitoring  
- **Automated Logging** to text/CSV files  
- **Anomaly Detection** → flags overheat/undervoltage events  
- **Visualization** → plots historical trends with Pandas + Matplotlib  

---

## 🚀 How to Run  

Run device simulation:  
```bash
python device_sim.py
Run test controller:

python test_controller.py


Visualize results:

python plot_results.py


Run automated test script:

sh run_test.sh

📎 Credits

Author: Tran Vuong
