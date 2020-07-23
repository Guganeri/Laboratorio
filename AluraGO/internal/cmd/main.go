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

	contaExemplos := clientes.Titular{"Bruno", "1213123", "212312312"}

	fmt.Println(contaExemplos)

	contaExemplo := contas.ContaCorrente{}
	contaExemplo.Depositar(100)

	fmt.Println(contaExemplo.ObterSaldo())
}
