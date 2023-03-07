const express = require("express");
const app = express();
const port = 3333;

app.get("/", (req, res) => {
  console.log("Endpoint executado");
  res.status(200).send("Hello World!");
});

app.listen(port, () => {
  console.log(`O servidor está rodando na porta ${port}`);
});
