import * as d3 from "d3";

export type Station = {
	id: string;
	startDate: Date;
	endDate: Date;
	latitude: number;
	longitude: number;
	height: number;
	name: string;
	state: string;
};

export type TemperatureMeasurement = {
	station: string;
	date: Date;
	temperatureAirMax200: number;
	temperatureAirMean200: number;
	temperatureAirMin200: number;
};

export async function loadStations(): Promise<Station[]> {
	const rows = await fetch("/stations.csv")
		.then((r) => r.text())
		.then((text) => d3.csvParse(text));

	return rows.map(
		(row) =>
			({
				id: row.station_id,
				startDate: d3.isoParse(row.start_date)!,
				endDate: d3.isoParse(row.end_date)!,
				latitude: +row.latitude,
				longitude: +row.longitude,
				height: +row.height,
				name: row.name,
				state: row.state
			}) satisfies Station
	);
}

export async function loadStation(id: string): Promise<TemperatureMeasurement[]> {
	const rows = await fetch(`/stations/${id}.csv`)
		.then((r) => r.text())
		.then((text) => d3.csvParse(text));

	return rows.map(
		(row) =>
			({
				station: row.station_id,
				date: d3.isoParse(row.date)!,
				temperatureAirMin200: +row.temperature_air_min_200,
				temperatureAirMean200: +row.temperature_air_mean_200,
				temperatureAirMax200: +row.temperature_air_max_200
			}) satisfies TemperatureMeasurement
	);
}
