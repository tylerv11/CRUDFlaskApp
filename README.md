# Delay CRUD App
### Writeback Tool for Technicians on Cycle Time Data

A lightweight Flask web application that allows technicians to log and edit delay reasons directly against cycle time records stored in Databricks. Records are pre-filled from a URL link — no manual data entry required to identify the lot.

---

## The Problem

In manufacturing and processing environments, cycle time data is monitored in **PowerBI**. When a lot's cycle time is flagged as too high, there is often no easy way for technicians on the floor to record *why* the delay happened without going through a separate system or emailing someone.

This app closes that gap.

---

## How It Works

### User Flow

```mermaid
flowchart TD
    A[Technician reviews cycle time\ndashboard in PowerBI] --> B{Cycle time flagged\nas too high?}
    B -- No --> C[No action needed]
    B -- Yes --> D[Clicks URL link embedded\nin the PowerBI report]
    D --> E[Flask app reads record\nfrom Databricks processing view]
    E --> F[Form loads pre-filled\nwith Batch ID, WO Number,\nBin Sequence, Duration, Operator]
    F --> G[Technician selects delay\ncategory and resource\nfrom dropdowns]
    G --> H[Technician types delay\ndescription and action taken]
    H --> I[Submit]
    I --> J[Flask writes delay record\nto Databricks delay table]
    J --> K[Technician can return\nto same URL to edit\nthe record at any time]
```

---

### Architecture

```mermaid
flowchart LR
    PBI[PowerBI Dashboard\nCycle Time Report]
    URL[URL Link\ne.g. /bin-1/wo-123/batch-456]
    FLASK[Flask App\napp.py]
    READ[Read Module\nall_data_read]
    WRITE[Write Module\nupdate_table]
    DB1[(Databricks\nprocessing_view\nCycle Time Data)]
    DB2[(Databricks\nDelay Table\nWriteback Target)]

    PBI -->|Technician clicks link| URL
    URL --> FLASK
    FLASK --> READ
    READ -->|SELECT query| DB1
    DB1 -->|Pre-fills form| FLASK
    FLASK -->|Technician submits| WRITE
    WRITE -->|UPDATE query| DB2
```

---

### URL Structure

Records are accessed via a structured URL. This URL can be embedded directly in PowerBI reports as a clickable link on any flagged cycle time row:

```
/batch_id/<batch_id>/bin_sequence/<bin_sequence>/wo_number/<wo_number>
```

**Example:**
```
/batch_id/batch-456/bin_sequence/1/wo_number/wo-123
```

When a technician visits this URL, the form is automatically populated with all known data for that record — they only need to fill in the delay details.

---

### The Form

The form presents:

| Field | Type | Editable |
|---|---|---|
| Batch ID | Text | Read-only |
| Work Order Number | Text | Read-only |
| Bin Sequence | Text | Read-only |
| Bin Start Time | Text | Read-only |
| Processing Duration | Text | Read-only |
| Operator | Text | Read-only |
| Sample Lot | Text | Read-only |
| Delay Category | Dropdown | ✅ |
| Delay Step | Dropdown | ✅ |
| Resource | Dropdown | ✅ |
| Equipment ID | Text | ✅ |
| Delay Description | Text area | ✅ |
| Action Taken | Text area | ✅ |

Read-only fields are pulled from the cycle time source table. Editable fields are written to the delay table on submit.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Python / Flask |
| Database | Databricks SQL |
| Data Layer | Databricks SQL Connector |
| Data Processing | Pandas |
| Frontend | Jinja2 HTML Templates |
| Deployment Config | app.yaml |

---

## Project Structure

```
CRUDFlaskApp/
├── app.py                          # Flask routes
├── app.yaml                        # Deployment config / env vars
├── requirements.txt
├── templates/
│   ├── add_delay.html              # Main delay entry form
│   └── update_submitted.html       # Confirmation page
└── lib/
    └── modules/
        ├── sql/
        │   └── main.py             # Databricks connection class
        ├── all_data_read/
        │   ├── main.py             # Read module
        │   └── _query_delay_info.sql
        └── update_table/
            ├── main.py             # Write module
            └── _query_update_table.sql
```

---

## Configuration

Set the following environment variables before running:

```bash
export DATABRICKS_SERVER_HOSTNAME="your-workspace.cloud.databricks.com"
export DATABRICKS_HTTP_PATH="/sql/1.0/warehouses/your-warehouse-id"
export DATABRICKS_ACCESS_TOKEN="enter-your-databricks-token"
```

Or configure them in `app.yaml` for container-based deployment.

---

## Running Locally

```bash
pip install -r requirements.txt
python app.py
```
