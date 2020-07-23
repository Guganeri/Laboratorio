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

	contaDoBruno := contas.ContaCorrente{Titular: clientes.Titular{
		Nome:      "Bruno",
		CPF:       "123.123.123.12",
		Profissao: "Desenvolvedor"}, NumeroAgencia: 123, NumeroConta: 123123123, Saldo: 1000}

	fmt.Println(contaDoBruno)
}
