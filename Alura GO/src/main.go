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

func (c *ContaCorrente) Depositar(valorDoDeposito float64) (string, float64) {
	if valorDoDeposito > 0 {
		c.saldo += valorDoDeposito
		return "Deposito realizado com sucesso", c.saldo
	} else {
		return "O valor do deposito é inválido", c.saldo
	}

}

func (c *ContaCorrente) Transferir(valorDaTransferencia float64, contaDesitno *ContaCorrente) bool {
	if valorDaTransferencia < c.saldo && valorDaTransferencia > 0 {
		c.saldo -= valorDaTransferencia
		contaDesitno.Depositar(valorDaTransferencia)
		return true
	} else {
		return false
	}
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

	contaDoGustavo := ContaCorrente{titular: "Gustavo", saldo: 300.0}
	contaDaSilvia := ContaCorrente{titular: "Silvida", saldo: 100.0}

	//status := contaDaSilvia.Transferir(50, &contaDoGustavo)
	//fmt.Println(status)

	fmt.Println(contaDoGustavo)
	fmt.Println(contaDaSilvia)

	status := contaDoGustavo.Transferir(100, &contaDaSilvia)
	fmt.Println(status)
	fmt.Println(contaDaSilvia)
	fmt.Println(contaDoGustavo)

}
