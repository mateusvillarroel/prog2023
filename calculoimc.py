peso = float (input('Digite o seu peso (kg): '))
altura = float (input('Digite a sua altura (m): '))
imc = peso/(altura**2)
print ("Seu IMC é: ", imc)
print ('Estou muito abaixo do peso?', imc < 17)
print ('Estou abaixo do peso normal?', imc >= 17 and imc < 18.5)