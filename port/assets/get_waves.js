const https = require('https');

const getWaves = function() {
	https.get("https://www.ndbc.noaa.gov/data/realtime2/46277.txt", function(res) {
	console.log(res.statusCode);
	res.setEncoding('utf-8');
	res.on('data', function(data) {
		const dataret = toString(data);
	console.log(dataret);
	
	});
	}).on('error', function(err){
		console.log(err);
	});
	return dataret;
};

const waveData = getWaves();
//console.log(waveData);