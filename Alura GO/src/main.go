package main

import "fmt"

type ContaCorrente struct {
	titular       string
	numeroAgencia int
	numeroConta   int
	saldo         float64
}

func (c *ContaCorrente) Sacar(valorDoSaque float64) string {
	podeSacar := valorDoSaque > 0 && valorDoSaque <= c.saldo
	if podeSacar {
		c.saldo -= valorDoSaque
		return "Saque realizado com sucessso"
	} else {
		return "Saldo insuficiente"
	}

}

func main() {
	//var contaDoGustavo ContaCorrente = ContaCorrente{}
	//contaDoGustavo := ContaCorrente{titular: "Gustavo", numeroAgencia: 001, numeroConta: 123456, saldo: 125.50}
	//fmt.Println(contaDoGustavo)

	//var contaDaCris *ContaCorrente //* -> alocar espaço na memoria para variável
	//contaDaCris = new(ContaCorrente)
	//contaDaCris.titular = "Cris"
	//contaDaCris.saldo = 500

	contaDaSilva := ContaCorrente{}
	contaDaSilva.titular = "Silvia"
	contaDaSilva.saldo = 500

	fmt.Println(contaDaSilva.saldo)

	fmt.Println(contaDaSilva.Sacar(-300))
	fmt.Println(contaDaSilva.saldo)

}
