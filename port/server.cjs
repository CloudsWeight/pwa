
const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;
const { spawn } = require('child_process');

app.listen(PORT, (error) => 
{
	if(!error)
		console.log('Listen pal')
	else
		console.log("Error Found in Application: ", error)
});
app.use("/assets", express.static(__dirname + "/assets"));
app.get("/assets/get_waves.js", function(req, res) 
{
	res.sendFile(__dirname + '/assets/get_waves.js');});
app.get("/assets/test", function(req, res) 
{
	res.sendFile(__dirname + '/assets/test.html');});

app.get('/api/getRates', (req, res) => {
	//const result = console.log('function called', req.body);
	const pyProc = spawn('python', ['./assets/Rate.py']);
	pyProc.stdout.on('data', (data) => {
		console.log(data);
		res.json(data.toString());
	});
	pyProc.stderr.on('data', (data) => {
		console.error(data);
		res.status(500).json(data.toString());
	});
	pyProc.on('close', (data) =>{
		console.log('close');
	});
});

app.get('/api/getNews', (req, res) => {
	//const result = console.log('function called', req.body);
	const pyProc = spawn('python', ['./assets/get_news.py']);
	pyProc.stdout.on('data', (data) => {
		console.log(data);
		//res.json(data.toString());
	});
	pyProc.stderr.on('data', (data) => {
		console.error(data);
		res.status(500).json(data.toString());
	});
	pyProc.on('close', (data) =>{
		console.log('close');
	});
});

app.get
app.get('/', (req,res) => {
	res.sendFile(path.join(__dirname, '/assets/index.html'));
});	
app.get('/favicon.ico', (req,res) => {
	res.sendFile(path.join(__dirname, '/assets/favicon.ico'));
});
