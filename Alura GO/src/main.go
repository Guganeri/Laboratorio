package main

import "fmt"

type ContaCorrente struct {
	titular       string
	numeroAgencia int
	numeroConta   int
	saldo         float64
}

func main() {
	//var contaDoGustavo ContaCorrente = ContaCorrente{}
	contaDoGustavo := ContaCorrente{titular: "Gustavo", numeroAgencia: 001, numeroConta: 123456, saldo: 125.50}

	contaBruna := ContaCorrente{"Bruna", 222, 11122, 120}

	fmt.Println(contaDoGustavo)
	fmt.Println(contaBruna)

	var contaDaCris *ContaCorrente //* -> alocar espaço na memoria para variável
	contaDaCris = new(ContaCorrente)
	contaDaCris.titular = "Cris"
	contaDaCris.saldo = 500

	fmt.Println(contaDaCris)

}
