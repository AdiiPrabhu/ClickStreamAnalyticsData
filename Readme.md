

# Real-Time Clickstream Analytics using Aiven Kafka & OpenSearch

## Overview

This project demonstrates a **real-time data pipeline** built using Aiven's managed services to simulate, process, and analyze website clickstream activity.

The solution ingests streaming user events into **Aiven for Apache Kafka**, streams them into **Aiven for OpenSearch using Kafka Connect**, and visualizes insights using **OpenSearch Dashboards**.

---

## Problem Statement

Organizations need **real-time visibility into user behavior** to:

* monitor traffic patterns
* detect anomalies and spikes
* analyze user engagement
* optimize product experience

Traditional batch pipelines introduce latency and complexity.

This solution demonstrates how to achieve **low-latency analytics using a streaming architecture**.

---

## Architecture

<!-- ```text
Python Producer
      ↓
Aiven Kafka (clickstream-events topic)
      ↓
Kafka Connect (OpenSearch Sink)
      ↓
Aiven OpenSearch
      ↓
OpenSearch Dashboards
``` -->
![imagearch](/Images/mermaid-diagram.png)
---

## Technologies Used

* **Aiven for Apache Kafka** → real-time data ingestion
* **Aiven Kafka Connect** → managed data pipeline
* **Aiven for OpenSearch** → indexing and analytics
* **OpenSearch Dashboards** → visualization
* **Python (kafka-python)** → clickstream data generator

---

## Use Case

This pipeline simulates a **website analytics system** that captures:

* page visits
* clicks and interactions
* user sessions
* device and browser usage
* geographic distribution



---

## Prerequisites

* Aiven account (optional)
* Aiven CLI installed (optional)
* Python 3.9+

---

## Setup Instructions

---

### 1. Install Aiven CLI


```bash
brew install aiven-client
```

Login:

```bash
avn user login YOUR_EMAIL
```
##### PS - Alternative is to do the complete configuration via UI 
---

### 2. Configure connection details

Update:

#### `producer.py`

```python
bootstrap_servers="KAFKA_HOST:PORT"
```

#### `connector/opensearch-sink.json`

```json
"connection.url": "https://OPENSEARCH_HOST:PORT",
"connection.username": "avnadmin",
"connection.password": "PASSWORD"
```

---

### 3. Create Kafka → OpenSearch connector

```bash
avn service connector create $KAFKA_SERVICE @connector/opensearch-sink.json
```

Verify:

```bash
avn service connector status $KAFKA_SERVICE clickstream-opensearch-sink
```

---

### 4. Install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 5. Run producer

```bash
python producer.py
```

This continuously generates **real-time clickstream events**.

---

##  Sample Event

```json
{
  "event_id": "42f7fcd8-ca66-466a-8f3a-fed14c6b4466",
  "timestamp": "2026-04-01T01:50:20.962000+00:00",
  "user_id": "user_1091",
  "session_id": "sess_45809",
  "page": "/login",
  "referrer": "direct",
  "action": "pageview",
  "device": "mobile",
  "browser": "Edge",
  "country": "CA",
  "duration_ms": 3471
}
```
![](/Images/Screenshot%202026-04-01%20at%203.00.13 AM.png)
---

##  Verify Data in OpenSearch

1. Open OpenSearch Dashboards
2. Go to **Discover**
3. Create data view:

```text
clickstream-events*
```

4. Select time field:

```text
timestamp
```
![](/Images/Screenshot%202026-04-01%20at%203.18.32 AM.png)
---

##  Dashboard Visualizations

The following visualizations were created:

---

###  Events Over Time

* X-axis → `timestamp`
* Y-axis → count
   Shows traffic trends

---

###  Top Pages

* Field → `page.keyword`
   Identifies popular pages

---

###  Device Distribution

* Field → `device.keyword`
   Mobile vs Desktop usage

---

###  Country Distribution

* Field → `country.keyword`
   Geographic insights

---

###  User Actions

* Field → `action.keyword`
   Click vs pageview vs signup

![](/Images/Screenshot%202026-04-01%20at%202.58.52 AM.png)

![](/Images/Screenshot%202026-04-01%20at%202.59.02 AM.png)


##  Troubleshooting

###  JSON parsing error

Fix:

```json
"value.converter.schemas.enable": "false"
```

---

###  OpenSearch connection error

Ensure:

```text
https://HOST:PORT
```

(no credentials in URL)

---

###  Wrong data in dashboard

Check:

* correct topic name
* correct data view
* producer running

---

This implementation demonstrates how **event-driven architectures** can enable **real-time analytics pipelines** using managed cloud services, reducing operational complexity while delivering immediate business insights.


