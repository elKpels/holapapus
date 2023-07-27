const readline = require("readline");
const readl = readline.createInterface({ input: process.stdin, output: process.stdout, escapeCodeTimeout: 200})
function final() {console.log("Agarro mi mochila"), console.log("Me subo al carro")}
console.log("Me levanto")
readl.question("¿Me bañe?: ´Y/N´", (respuesta) => { if(respuesta == "Y"){console.log("Me cambio"), readl.question("¿Tengo mas de medio hora?: ´Y/N´", (respuesta) => { if (respuesta == "Y"){console.log("desayuno")} final()})} else {console.log("Me baño"), console.log("Me cambio"), readl.question("¿Tengo mas de medio hora?: ´Y/N´", (respuesta) => { if (respuesta == "Y"){console.log("desayuno")} final()})}})