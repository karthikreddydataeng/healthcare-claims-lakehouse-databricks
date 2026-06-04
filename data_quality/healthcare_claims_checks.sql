-- Null check for required claim identifiers
SELECT
    claim_id,
    member_id
FROM silver_claims_cleaned
WHERE claim_id IS NULL
   OR member_id IS NULL;

-- Duplicate claim check
SELECT
    claim_id,
    COUNT(*) AS duplicate_count
FROM silver_claims_cleaned
GROUP BY claim_id
HAVING COUNT(*) > 1;

-- Invalid claim amount check
SELECT
    claim_id,
    claim_amount
FROM silver_claims_cleaned
WHERE claim_amount < 0;

-- Claim status distribution
SELECT
    claim_status,
    COUNT(*) AS claim_count
FROM silver_claims_cleaned
GROUP BY claim_status;

-- High value claims review
SELECT
    claim_id,
    member_id,
    claim_amount,
    claim_status
FROM silver_claims_cleaned
WHERE claim_amount >= 10000;
