# ETL Logging Mechanism  

## 📌 Project Overview
This repository focuses on implementing **logging mechanisms** in ETL pipelines. Logging is essential for tracking data flow, debugging errors, and ensuring the pipeline's reliability.

---

## 📁 **Project Structure**
```
ETL-Logging-Mechanism/
│── README.md                     # Project documentation  
│── src/  
│   ├── etl_pipeline.py            # ETL script with logging  
│   ├── logger.py                  # Custom logging module  
│── logs/  
│   ├── etl_execution.log          # Execution log file  
│── docs/  
│   ├── logging_strategy.md        # Documentation on logging strategy  
```

---

## 🚀 **Key Features**
✅ **Detailed Logging** – Captures each step of the ETL process  
✅ **Logging Levels** – Debug, Info, Warning, Error, Critical  
✅ **Timestamped Logs** – Helps in tracking execution time  
✅ **Log Rotation** – Avoids oversized log files  
✅ **Custom Log Format** – Structured logs for easy analysis  

---

## 🏗 **Logging Strategy**
1️⃣ **Info Logs** – Records normal execution steps.  
2️⃣ **Debug Logs** – Captures detailed information for debugging.  
3️⃣ **Warning Logs** – Flags potential issues that need attention.  
4️⃣ **Error Logs** – Captures failures with details.
5️⃣ **Critical Logs** – Indicates system failure requiring immediate action.  

---

## 🔧 **Installation & Usage**
### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/ETL-Logging-Mechanism.git
cd ETL-Logging-Mechanism
```
### 2️⃣ **Run the ETL Pipeline**
```sh
python src/etl_pipeline.py
```
### 3️⃣ **Check Logs**
```sh
cat logs/etl_execution.log
```

