# System Health Monitoring & Application Health Checker

This project contains two scripts written in Python:

1. **System Health Monitoring Script (`health.py`)**  
   - Monitors CPU, Memory, Disk usage, and Running Processes.  
   - Logs warnings if usage exceeds predefined thresholds.  
   - Stores results in `system_health.log`.  

2. **Application Health Checker (`app_health.py`)**  
   - Checks if a given application (via URL) is up and responding.  
   - Verifies by HTTP status codes.  
   - Logs results in `app_health.log`.  

---

## 🚀 Requirements
- Python 3.x  
- Required packages:  
  - `psutil` (for system monitoring)  
  - `requests` (for application health checking)  

Install them using:

```bash
# Install psutil
sudo apt install python3-psutil -y

# Install requests
sudo apt install python3-requests -y
