package main

import (
	"fmt"

	"github.com/Guganeri/Laboratorio/AluraGO/pkg/contas"
)

func PagarBoleto(conta vertificarConta, valorBoleto float64) {
	conta.Sacar(valorBoleto)
}

type vertificarConta interface {
	Sacar(valor float64) string
}

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

	//contaExemplos := clientes.Titular{"Bruno", "1213123", "212312312"}

	//fmt.Println(contaExemplos)

	//contaExemplo := contas.ContaCorrente{}
	//contaExemplo.Depositar(100)

	//fmt.Println(contaExemplo.ObterSaldo())

	contaDoDenis := contas.ContaPoupanca{}
	contaDoDenis.Depositar(100)
	PagarBoleto(&contaDoDenis, 60)

	//contaDaPati := contas.ContaCorrente{}

	fmt.Println(contaDoDenis.ObterSaldo())
	//fmt.Println(contaDaPati)
}
