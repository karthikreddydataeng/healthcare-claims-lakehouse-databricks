# Delta Lake Table Design

## Objective

This document describes the Delta Lake table design for processing synthetic healthcare claims data.

## Table Layers

### Bronze Layer

Stores raw claims data exactly as received from the landing zone.

### Silver Layer

Stores cleaned and standardized claims data after applying data quality and schema validation checks.

### Gold Layer

Stores curated analytics-ready data for reporting and downstream dashboards.

## Example Tables

- bronze_claims_raw
- silver_claims_cleaned
- gold_claims_summary
- gold_claims_by_status
- gold_high_value_claims

## Delta Lake Benefits

- ACID transaction support
- Schema enforcement
- Schema evolution
- Time travel
- Reliable batch and streaming support
- Improved data quality and auditability

## Healthcare Data Safety

This project uses only synthetic data and does not store PHI, PII, or production healthcare records.
