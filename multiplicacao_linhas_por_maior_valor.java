/*
    Elabore um programa que preencha uma matriz 6 x 4, desenvolva: 

    a) recalcule a matriz digitada onde cada linha deverá ser multiplicada pelo 
       maior elemento da linha em questao; 
    b) mostre a matriz inicial e a matriz resultante.

 */
package exercicio6feito;

// Para usar a ferramenta de ler a entrada do teclado, precisamos importá-la.
import java.util.Scanner;

public class Exercicio6Feito {


    public static void main(String[] args) {
      
        // --- Passo 1: Definir o tamanho e criar a matriz ---

        // É uma boa prática definir os tamanhos em variáveis. 'final' significa que o valor não pode mudar.
        final int NUMERO_DE_LINHAS = 6;
        final int NUMERO_DE_COLUNAS = 4;

        // Criamos nossa matriz com o tipo 'int' e os tamanhos definidos.
        int[][] matrizOriginal = new int[NUMERO_DE_LINHAS][NUMERO_DE_COLUNAS];

        // Criamos a ferramenta (objeto) Scanner para ler o que o usuário vai digitar.
        Scanner teclado = new Scanner(System.in);

        System.out.println("--- Preenchimento da Matriz 6x4 ---");
        System.out.println("Por favor, digite 24 números inteiros.");

        // O primeiro 'for' percorre as LINHAS (de 0 a 5)
        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            // O segundo 'for' percorre as COLUNAS (de 0 a 3) para cada linha
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                // System.out.print() mostra a mensagem sem pular para a próxima linha.
                System.out.print("Digite o valor para a Linha " + (i + 1) + ", Coluna " + (j + 1) + ": ");
                // teclado.nextInt() espera o usuário digitar um número e o guarda na matriz.
                matrizOriginal[i][j] = teclado.nextInt();
            }
        }

        // --- Passo 2: Calcular a matriz resultante ---

        // a) Primeiro, criamos uma cópia da matriz original.
        // É importante fazer isso para não perdermos os valores originais.
        int[][] matrizResultante = new int[NUMERO_DE_LINHAS][NUMERO_DE_COLUNAS];
        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                matrizResultante[i][j] = matrizOriginal[i][j];
            }
        }
        
        // b) Agora vamos modificar a matrizResultante, linha por linha.
        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            // Encontrar o maior elemento da linha atual
            // Java não tem uma função 'max()' simples para arrays como Python,
            // então, fazemos isso manualmente com um 'for'.
            int maiorElemento = matrizResultante[i][0]; // Começamos assumindo que o primeiro é o maior.
            for (int j = 1; j < NUMERO_DE_COLUNAS; j++) { // Depois, comparamos com os outros (a partir do segundo).
                if (matrizResultante[i][j] > maiorElemento) {
                    maiorElemento = matrizResultante[i][j]; // Se acharmos um maior, ele vira o novo maior.
                }
            }

            // Multiplicar cada elemento da linha pelo maior encontrado
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                matrizResultante[i][j] = matrizResultante[i][j] * maiorElemento;
            }
        }

        // --- Passo 3: Mostrar as duas matrizes ---
        
        System.out.println("\n=============================================");
        System.out.println("--- Matriz Original (Como foi digitada) ---");
        
        // Loop para imprimir a matriz original
        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                // O "\t" adiciona um espaço de tabulação para alinhar os números
                System.out.print(matrizOriginal[i][j] + "\t");
            }
            System.out.println(); // Pula para a próxima linha no final de cada linha da matriz
        }

        System.out.println("\n--- Matriz Resultante (Após os cálculos) ---");

        // Loop para imprimir a matriz resultante
        for (int i = 0; i < NUMERO_DE_LINHAS; i++) {
            for (int j = 0; j < NUMERO_DE_COLUNAS; j++) {
                System.out.print(matrizResultante[i][j] + "\t");
            }
            System.out.println();
        }
        System.out.println("=============================================");

        // É uma boa prática fechar a ferramenta 'Scanner' quando não for mais usá-la.
        teclado.close();
    }
    
}
