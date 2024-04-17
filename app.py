



play1 = input('Digite sua jogada(pedra, papel ou tesoura)').lower()
play2 = input('Digite sua jogada(pedra, papel ou tesoura)').lower()

tesoura = 'tesoura'
papel = 'papel'
pedra = 'pedra'

if play1 == tesoura and play2 == papel:
    print(f'{play1} é o vencedor')
elif play1 == pedra and play2 == tesoura:
    print(f'{play1} vencedor !')
elif play1 == papel and play2 == pedra:
    print('O {play1} venceu ' )  
elif play2 == tesoura and play1 == papel:
    print(f'{play2} é o vencedor')
elif play2 == pedra and play1 == tesoura:
    print(f'{play2} vencedor !')
elif play2 == papel and play1 == pedra:
    print('O {play2} venceu ' )            
    

"""
if play1 == play2:
    print('Empate!')
elif play1 == 'pedra':
    if play2 == 'tesoura':
        print('O Player 1 ganhou')
elif play1 == 'papel':
    if play2 == 'pedra':
        print('Papel ganhou')



"""




















