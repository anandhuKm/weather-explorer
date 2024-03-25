#!/usr/bin/env python3

from pathlib import Path
import polars as pl
from wetterdienst import Settings
from wetterdienst.provider.dwd.observation import DwdObservationRequest

root_path = Path(__file__).resolve(strict=True).parents[1]
data_path = Path(root_path, "static")
data_path.mkdir(parents=True, exist_ok=True)
stations_data_path = Path(data_path, "stations")
stations_data_path.mkdir(parents=True, exist_ok=True)

settings = Settings(
    ts_shape="long",
    ts_humanize=True,
    ts_si_units=True,
    ts_skip_empty=True,
    ts_skip_threshold=0.95,  # max 95% of data missing
    ts_dropna=True,
)

request = DwdObservationRequest(
    parameter=[
        "temperature_air_min_200",
        "temperature_air_mean_200",
        "temperature_air_max_200",
    ],
    resolution="daily",
    period="recent",
)

stations = request.all()

# retrieve the actual values
df = stations.values.all().df.drop("dataset")

# use date resolution
df = df.with_columns(date=df["date"].dt.date())

# pivot values into columns
df = df.pivot(index=["station_id", "date"], columns="parameter", values="value")

# filter out rows with nulls
df = df.drop_nulls()

# convert temperature from Kelvin to Celsius
df = df.with_columns(df.select(pl.selectors.starts_with("temperature")) - 273.15)

# filter out stations that don't have any measurements at all and export to CSV
stations.df.filter(pl.col("station_id").is_in(df["station_id"].unique())).write_csv(
    Path(data_path, "stations.csv"), float_precision=4
)

# export each station separately to a CSV file
for station_df in df.partition_by(by="station_id", maintain_order=True):
    station_id = station_df.row(0)[0]
    station_df.drop("station_id").write_csv(
        Path(stations_data_path, f"{station_id}.csv"), float_precision=1
    )
