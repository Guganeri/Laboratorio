package main

import (
	"fmt"

	"github.com/Guganeri/Laboratorio/AluraGo/src/contas"
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

	contaDoGustavo := contas.ContaCorrente{Titular: "Gustavo", Saldo: 300.0}
	contaDaSilvia := contas.ContaCorrente{Titular: "Silvida", Saldo: 100.0}

	//status := contaDaSilvia.Transferir(50, &contaDoGustavo)
	//fmt.Println(status)

	fmt.Println(contaDoGustavo)
	fmt.Println(contaDaSilvia)

	status := contaDoGustavo.Transferir(100, &contaDaSilvia)
	fmt.Println(status)
	fmt.Println(contaDaSilvia)
	fmt.Println(contaDoGustavo)

}
