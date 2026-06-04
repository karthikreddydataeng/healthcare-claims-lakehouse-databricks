import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = BASE_DIR / "data" / "sample_claims.csv"


def read_claims(file_path):
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def validate_claims(claims):
    total_claims = len(claims)
    invalid_amounts = []
    high_value_claims = []

    for claim in claims:
        amount = float(claim["claim_amount"])

        if amount < 0:
            invalid_amounts.append(claim["claim_id"])

        if amount >= 10000:
            high_value_claims.append(claim["claim_id"])

    print("Healthcare Claims Validation Summary")
    print("------------------------------------")
    print(f"Total claims reviewed: {total_claims}")
    print(f"Invalid claim amounts: {len(invalid_amounts)}")
    print(f"High value claims: {len(high_value_claims)}")

    print("\nInvalid amount claims:")
    for claim_id in invalid_amounts:
        print(claim_id)

    print("\nHigh value claims:")
    for claim_id in high_value_claims:
        print(claim_id)


def main():
    claims = read_claims(INPUT_FILE)
    validate_claims(claims)


if __name__ == "__main__":
    main()
