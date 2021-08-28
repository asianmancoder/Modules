const express = require("express");
const got = require("got");

const app = express();


app.get("/", (req, res) => {
    res.send("home");
});

app.get("/api/:version/:api/:res_content_type", async function(req, res) {
    try {
        const response = await got(`https://nodejs.org/dist/${req.params.version}/docs/api/${req.params.api}.${req.params.res_content_type}`);
        res.send(response.body);
    } catch(e) {
        res.send(e);
    }
});


app.listen(3000);
