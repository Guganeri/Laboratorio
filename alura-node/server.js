import http from "http";

const PORT = 3000;

const rotas = {
    "/": "Curso de Node.js!!",

    "/livros": "Entrei na rota Livros",

    "/autores": "Entrei na rota Autores",
};

const server = http.createServer((req, res)=>{
    res.writeHead(200, {"Content-Type": "text/plain"});
    res.end(rotas[req.url]);
});

server.listen(PORT,() => {
    console.log("Server on port 3000!")
});