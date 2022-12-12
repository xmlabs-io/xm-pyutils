import datetime
import typing
import boto3


def get_objects_by_date(
    bucket: str, end_date: datetime.datettime, start_date: datetime.datetime = None
) -> typing.List:
    """
    Get objects from S3 bucket by date.
    """

    # Convert dates to strings because jmespath doesn't support datetime objects
    end_date_str = end_date.strftime("%Y-%m-%d")
    start_date_str = start_date.strftime("%Y-%m-%d") if start_date else None

    client = boto3.client("s3")
    paginator = client.get_paginator("list_objects")
    page_iterator = paginator.paginate(Bucket=bucket)
    if start_date_str:
        return page_iterator.search(
            f"Contents[?LastModified >= `{start_date_str}` && LastModified < `{end_date_str}`]"
        )

    return page_iterator.search(f"Contents[?LastModified < `{end_date_str}`]")
