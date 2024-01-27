# coding: utf-8

import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine
import os


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    # download parquet file from website
    file_name = "output.parquet"
    os.system(f"wget {url} -O {file_name}")

    df = pd.read_parquet(file_name)

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    engine.connect()
    df.to_sql(name=table_name, con=engine, if_exists="replace")
    print("ingest finished")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest parquet file to Postgres")

    parser.add_argument("--user", help="user name for postgres")
    parser.add_argument("--password", help="password name for postgres")
    parser.add_argument("--host", help="host for postgres")
    parser.add_argument("--port", help="port for postgres")
    parser.add_argument("--db", help="db for postgres")
    parser.add_argument("--table_name", help="table_name for postgres")
    parser.add_argument("--url", help="url for parquet source file")

    args = parser.parse_args()

    main(args)
