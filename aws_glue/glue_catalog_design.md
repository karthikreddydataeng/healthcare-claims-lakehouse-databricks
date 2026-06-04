# AWS Glue Catalog Design

## Objective

This document describes how AWS Glue Catalog can be used to organize and discover healthcare claims datasets in a lakehouse environment.

## Catalog Structure

### Database

healthcare_claims_lakehouse

### Tables

- claims_raw
- claims_cleaned
- claims_summary
- claims_quality_results

## Metadata Captured

- Table name
- Column name
- Data type
- Source layer
- Business description
- Data quality rule
- Refresh frequency
- Ownership

## Benefits

- Centralized metadata management
- Easier dataset discovery
- Better governance and lineage
- Support for analytics and reporting teams
- Improved audit readiness

## Safety Note

This design is based on synthetic portfolio data and does not include PHI, PII, or employer-owned metadata.
