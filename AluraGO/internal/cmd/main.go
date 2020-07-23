package main

import (
	"fmt"

	"github.com/Guganeri/Laboratorio/AluraGO/pkg/clientes"
	"github.com/Guganeri/Laboratorio/AluraGO/pkg/contas"
)

func main() {
	//var contaDoGustavo ContaCorrente = ContaCorrente{}

	//fmt.Println(contaDoGustavo)

	//var contaDaCris *ContaCorrente //* -> alocar espaço na memoria para variável
	//contaDaCris = new(ContaCorrente)
	//contaDaCris.titular = "Cris"
	//contaDaCris.saldo = 500

	//contaDaSilva := ContaCorrente{}
	//contaDaSilva.titular = "Silvia"
	//contaDaSilva.saldo = 500

	//fmt.Println(contaDaSilva.saldo)
	//status, valor := contaDaSilva.Depositar(2000)
	//fmt.Println(status, valor)

	clienteBruno := clientes.Titular{"Bruno", "123.123.123.12", "Desenvolvedor GO"}
	contaDoBruno := contas.ContaCorrente{clienteBruno, 123, 123123, 100}
	fmt.Println(contaDoBruno)
}
