from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, when


def create_spark_session():
    return (
        SparkSession.builder
        .appName("HealthcareClaimsLakehouse")
        .getOrCreate()
    )


def clean_claims_data(claims_df):
    """
    Cleans and standardizes synthetic healthcare claims data.
    """

    cleaned_df = (
        claims_df
        .withColumn("claim_id", trim(col("claim_id")))
        .withColumn("member_id", trim(col("member_id")))
        .withColumn("claim_status", upper(trim(col("claim_status"))))
        .withColumn(
            "claim_category",
            when(col("claim_amount") >= 10000, "HIGH_VALUE_CLAIM")
            .when(col("claim_amount") >= 1000, "STANDARD_CLAIM")
            .otherwise("LOW_VALUE_CLAIM")
        )
    )

    return cleaned_df


def main():
    spark = create_spark_session()

    sample_claims = [
        ("CLM1001", "MBR1001", "medical", 12500.50, "approved"),
        ("CLM1002", "MBR1002", "pharmacy", 250.75, "paid"),
        ("CLM1003", "MBR1003", "medical", 3400.00, "denied"),
        ("CLM1004", "MBR1004", "dental", 850.25, "approved")
    ]

    columns = [
        "claim_id",
        "member_id",
        "claim_type",
        "claim_amount",
        "claim_status"
    ]

    claims_df = spark.createDataFrame(sample_claims, columns)

    cleaned_claims_df = clean_claims_data(claims_df)

    cleaned_claims_df.show(truncate=False)


if __name__ == "__main__":
    main()
