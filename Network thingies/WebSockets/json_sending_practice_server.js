const ws = require("ws");
let wss = new ws.Server({
    port: 8080
});

wss.on("connection", ws => {
    ws.send("The server is ready to receive data.");
    
    ws.on("message", msg => {
        try {
            console.log(JSON.parse(msg));
        } catch(e) {
            console.log("Something went wrong. Perhaps the JSON data was incorrectly formatted.");
        }
    });
});