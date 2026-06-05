# Healthcare Claims Lakehouse with Databricks

## Overview

This project demonstrates a healthcare claims lakehouse pattern using synthetic claims data, Databricks concepts, PySpark processing logic, Delta Lake table design, AWS S3 landing zone concepts, AWS Glue Catalog concepts, SQL, and data quality checks.

The project shows how healthcare claims data can be ingested, cleaned, validated, organized into lakehouse layers, and prepared for downstream analytics.

This is a portfolio project created using synthetic data only. It does not contain PHI, PII, employer-owned code, production data, credentials, or confidential architecture.

## Business Problem

Healthcare organizations process large volumes of claims and clinical data for reporting, quality measurement, care coordination, value based care analytics, and operational decision making.

Traditional ETL workflows can be slow, harder to audit, and difficult to scale. A lakehouse architecture helps improve reliability, schema control, data quality, and analytics readiness.

## Architecture

Synthetic Healthcare Claims Data  
→ AWS S3 Landing Zone Concept  
→ Databricks PySpark Processing  
→ Data Cleansing and Standardization  
→ Delta Lake Bronze Layer  
→ Delta Lake Silver Layer  
→ Delta Lake Gold Layer  
→ Data Quality Checks  
→ Claims Analytics Output  
→ Healthcare Reporting Dashboard

## Tools and Technologies

- Python for local claims validation logic
- Databricks concept for scalable healthcare data processing
- PySpark concept for distributed transformations
- Delta Lake concept for bronze, silver, and gold table design
- AWS S3 concept for landing zone storage
- AWS Glue Catalog concept for metadata management
- SQL for healthcare claims data quality checks
- CSV files for sample input and output data
- Markdown documentation for architecture, quality rules, and HIPAA-safe design

## Repository Structure

```text
healthcare-claims-lakehouse-databricks/
├── README.md
├── requirements.txt
├── architecture/
│   └── architecture_diagram.md
├── aws_glue/
│   └── glue_catalog_design.md
├── data/
│   └── sample_claims.csv
├── data_quality/
│   └── healthcare_claims_checks.sql
├── delta_lake/
│   └── delta_table_design.md
├── docs/
│   ├── hipaa_safe_design.md
│   └── project_summary_for_recruiters.md
├── notebooks/
│   └── claims_processing_pyspark.py
├── output/
│   ├── claims_quality_results.csv
│   └── claims_summary.csv
└── scripts/
    └── validate_claims.py
```

## How to Run

This project demonstrates the healthcare lakehouse architecture, synthetic claims data flow, Delta Lake layer design, and runnable claims validation logic.

### 1. Review the Project Design

Start with these files:

- `architecture/architecture_diagram.md`
- `delta_lake/delta_table_design.md`
- `aws_glue/glue_catalog_design.md`
- `docs/hipaa_safe_design.md`
- `docs/project_summary_for_recruiters.md`

### 2. Review Sample Input and Output

Input file:

- `data/sample_claims.csv`

Expected output examples:

- `output/claims_quality_results.csv`
- `output/claims_summary.csv`

### 3. Review SQL Data Quality Checks

SQL validation checks are located here:

- `data_quality/healthcare_claims_checks.sql`

These checks cover:

- Required claim identifiers
- Duplicate claim detection
- Invalid claim amount detection
- Claim status distribution
- High value claim review

### 4. Run the Claims Validation Script Locally

This project uses built-in Python libraries only.

From the main project folder, run:

```bash
python scripts/validate_claims.py
```

If your system uses Python 3 separately, run:

```bash
python3 scripts/validate_claims.py
```

The script will:

1. Read synthetic healthcare claims from `data/sample_claims.csv`
2. Validate claim amounts
3. Identify high value claims
4. Print a claims validation summary in the terminal

## Sample Validation Logic

The validation logic is intentionally simple for portfolio review:

- Claims with negative claim amounts are flagged as invalid.
- Claims greater than or equal to 10000 are flagged for high value review.
- Total claims, invalid claims, and high value claims are summarized.

## Sample Output

Example terminal output:

```text
Healthcare Claims Validation Summary
------------------------------------
Total claims reviewed: 8
Invalid claim amounts: 1
High value claims: 2

Invalid amount claims:
CLM1005

High value claims:
CLM1001
CLM1008
```

## Design Decisions

- Databricks and PySpark are represented as lakehouse processing concepts.
- The local runnable validation script uses built-in Python to avoid complex setup for reviewers.
- Delta Lake design is documented using bronze, silver, and gold layers.
- AWS Glue Catalog is documented as the metadata and discovery layer.
- SQL files show how claims data quality checks can be implemented.
- All data is synthetic and safe for public portfolio use.

## Key Features

- Synthetic healthcare claims input data
- Runnable claims validation script
- Claims quality output examples
- Claims summary output examples
- Delta Lake table design
- AWS Glue metadata catalog design
- SQL data quality checks
- HIPAA-safe portfolio documentation
- Recruiter-friendly project summary
- Architecture documentation

## Portfolio Safety Note

This project is a portfolio recreation based on healthcare data engineering patterns. It uses synthetic data only and does not include PHI, PII, employer-owned code, production data, credentials, or confidential healthcare logic.
