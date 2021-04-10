var http = require("http");
const criticalcss = require("criticalcss");
const penthouse = require('penthouse');

http.createServer(function (request, response) {
	console.log(request);
	console.log(response);
   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   
   //Send the response body as "Hello World"

   //response.end('Hello World\n');
}).listen(8081);

// Console will print the message
console.log('Server running at http://127.0.0.1:8081/');
