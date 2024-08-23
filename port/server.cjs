
const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

app.listen(PORT, (error) => 
{
	if(!error)
		console.log('Listen pal')
	else
		console.log("error", error)
});
app.use("/assets", express.static(__dirname + "/assets"));
app.get("/assets/get_waves.js", function(req, res) 
{
	res.sendFile(__dirname + '/assets/get_waves.js');});
app.get("/assets/test", function(req, res) 
{
	res.sendFile(__dirname + '/assets/test.html');});

app.get('/api/getwaves', (req, res) => {
	const result = console.log('function called', req.body);
	res.json({success: true});
});
app.get('/', (req,res) => {
	res.sendFile(path.join(__dirname, '/assets/index.html'));
});	
app.get('/favicon.ico', (req,res) => {
	res.sendFile(path.join(__dirname, '/assets/favicon.ico'));
});
